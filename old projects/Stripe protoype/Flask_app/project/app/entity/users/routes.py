from flask import render_template, url_for,flash,redirect,request,abort,Blueprint
from app.Models import User,Subs,Account,Posts,Posts_access
from flask_login import login_user,current_user,logout_user,login_required,LoginManager
from app import bcrypt,db
from app.entity.users.forms import (RegistrationForm,LoginForm)
import stripe
from app.config import Config
from sqlalchemy import or_, and_, desc,asc
import webbrowser


users =Blueprint('users',__name__)
stripe.api_key = Config.stripe_secret_key

@users.route('/login',methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
       return redirect(url_for('users.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        name=User.query.filter_by(username=form.username.data).first()
        if  name and bcrypt.check_password_hash(name.password,form.password.data):
            login_user(name)
            next_page=request.args.get('next')
            return redirect (next_page) if next_page else  redirect(url_for('users.dashboard'))
        else:
            flash(f'Wrong email or password','danger')

    return render_template('login.html',legend="login",form=form)

@users.route('/sign_up',methods=['GET','POST'])
def sign_up():
    db.create_all()
    if current_user.is_authenticated:
       return redirect(url_for('users.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data.lower())
        db.session.add(user)
        user.password=hashed_password
        customer = stripe.Customer.create(
            email=form.username.data+"@gmail.com",
            payment_method='pm_card_visa',
            invoice_settings={
                'default_payment_method': 'pm_card_visa',
            },
        )
        user.customer_id=customer['id']
        db.session.commit()
        if form.Price.data !='':
            user.paid=True
            product = stripe.Product.create(
                name=form.username.data.lower()+"subscription",
            )
            user.product_id=product['id']
            price = stripe.Price.create(
                product=product['id'],
                unit_amount=int(form.Price.data)*100,
                currency='usd',
                recurring={
                    'interval': 'month',
                },
            )
            user.price=float(price["unit_amount"])
            user.price_id=price["id"]
            account_ = stripe.Account.create(
            type='express',
            )
            acc=Account(user=user.id,account_id=account_['id'])
            db.session.add(acc)
            account_links = stripe.AccountLink.create(
            account=account_['id'],
            refresh_url='http://127.0.0.1:5000/account/refresh/'+str(user.id),
            return_url='http://127.0.0.1:5000/',
            type='account_onboarding',
            )
            db.session.commit()
            return redirect(account_links['url'])
        flash(f'Account created you can now login','success')
        return redirect(url_for('users.login'))
    return render_template('signup.html',legend="sign_up",form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users.route('/')
def dashboard():
    if current_user.is_authenticated:
        user=User.query.filter(User.id!=current_user.id).all()
        return render_template('dashboard.html',legend="Board",users=user)
    return redirect(url_for('users.login'))

@users.route('/followers/<int:id>/',methods=['GET','POST'])
def follower(id):
    if current_user.is_authenticated:
        Subscribers=current_user.is_followers()
        acc=Account.query.filter_by(user=current_user.id).first()
        link='#'
        if acc is not None:
            try:
                link=stripe.Account.create_login_link(
                    acc.account_id,
                    )
                link=link['url']
            except:
                link='#'
            
        return render_template('follower.html',legend="Board",link=link,acc=acc,users=Subscribers)
    return redirect(url_for('users.login'))

@users.route('/followed/<string:id>/',methods=['GET','POST'])
def followed(id):
    if current_user.is_authenticated:
        Subscribed=current_user.has_followed()
        session = stripe.billing_portal.Session.create(
            customer=current_user.customer_id,
            return_url='http://127.0.0.1:5000/followed/'+str(current_user.id),
        )
        link=session.url
        return render_template('followed.html',legend="Board",users=Subscribed,link=link)
    return redirect(url_for('users.login'))

@users.route('/all/posts/<int:id>/',methods=['GET','POST'])
def all_posts(id):
    if current_user.is_authenticated:
        posts=Posts.query.filter_by(user=id).all()
        payer=[]
        for i in posts:
            payed=Posts_access.query.filter(and_(Posts_access.user==current_user.id,Posts_access.post==i.id)).first()
            if payed:
                posts.remove(i)
                payer.append(payed)
        return render_template('posts.html',legend="Board",posts=posts,payer=payer)
    return redirect(url_for('users.login'))


@users.route('/posts/create/',methods=['GET','POST'])
def posted():
    if current_user.is_authenticated:
        account=Account.query.filter_by(user=current_user.id).first()
        if account:
            if account.valid == True:
                posts=Posts(user=current_user.id,content="This is a post nigga",price=25)
                db.session.add(posts)
                db.session.commit()
                product = stripe.Product.create(
                    name=current_user.username+"posts",
                )
                posts.product_id=product['id']
                price = stripe.Price.create(
                    product=product['id'],
                    unit_amount=int(posts.price)*100,
                    currency='usd',
                )
                posts.price_id=price["id"]
                posts.paid=True
                db.session.commit()
                flash(f'you have created a post ','success')
                return redirect(url_for('users.dashboard'))
        else:
            if account:
                return redirect('http://127.0.0.1:5000/account/refresh/'+str(current_user.id))
            else:
                account_ = stripe.Account.create(
                type='express',
                )
                acc=Account(user=current_user.id,account_id=account_['id'])
                db.session.add(acc)
                account_links = stripe.AccountLink.create(
                account=account_['id'],
                refresh_url='http://127.0.0.1:5000/account/refresh/'+str(current_user.id),
                return_url='http://127.0.0.1:5000/posts/create/',
                type='account_onboarding',
                )
                db.session.commit()
                return redirect(account_links['url'])
        
        return redirect(url_for('users.dashboard'))
    return redirect(url_for('users.login'))


@users.route('/sub/<string:Type>/<int:id>/start',methods=['GET','POST'])
def subprocess(Type,id):
    
    if current_user.is_authenticated:
        user=User.query.filter_by(id=id).first()
        acc=Account.query.filter_by(user=id).first()
        if Type=="Follow":
            if current_user.is_following(user):
                flash(f'you are already  subscribed to '+user.username,'warning')
                return redirect(url_for('users.dashboard'))
            else:
                if user.paid==True:
                    session = stripe.checkout.Session.create(
                        customer=current_user.customer_id,
                        mode="subscription",
                        payment_method_types=['card'],
                        line_items=[{
                            'price': user.price_id,
                            'quantity': 1,
                        }],
                        subscription_data={
                            'application_fee_percent': 10,
                            'transfer_data': {
                            'destination': acc.account_id,
                            },
                        },
                        success_url='http://127.0.0.1:5000/',
                        cancel_url='https://example.com/cancel',
                    )
                    
                    return redirect(session['url'])
                else:
                    current_user.follow(user)
                    db.session.commit()
                    flash(f'you have succesfully subscribed to '+user.username,'success')
                    return redirect(url_for('users.dashboard'))
        if Type=="Unfollow":
            if user.paid==True:
                if current_user.is_following(user):
                    product=Subs.query.filter(and_(Subs.user==current_user.id,Subs.product_user==user.id,Subs.valid==True)).first()
                    if product:
                        stripe.Subscription.modify(
                        product.sub_id,
                        cancel_at_period_end=True
                        )
                        flash(f'you have succesfully unsubscribed from '+user.username,'danger')
                        return redirect(url_for('users.dashboard'))
                    else:
                        flash(f'check subscription of '+user.username,'danger')
                        return redirect(url_for('users.dashboard'))
                else:
                    flash(f'you have not subscribed to '+user.username,'success')
                    return redirect(url_for('users.dashboard'))
                
            if current_user.is_following(user):
                current_user.unfollow(user)
                db.session.commit()
                flash(f'you have succesfully unsubscribed from '+user.username,'danger')
                return redirect(url_for('users.dashboard'))
            else:
                flash(f'you have not subscribed to '+user.username,'success')
                return redirect(url_for('users.dashboard'))
        return render_template('dashboard.html',legend="Board")
    return redirect(url_for('users.login'))

    