from flask import render_template, url_for,flash,redirect,request,abort,Blueprint
from app.Models import User,Subs,Account,Posts,Posts_access
from flask_login import login_user,current_user,logout_user,login_required,LoginManager
from app import bcrypt,db
import stripe
from flask import app
from app.config import Config
import json
import os
import stripe
from sqlalchemy import or_, and_, desc,asc
import webbrowser



pay =Blueprint('pay',__name__)
stripe.api_key = Config.stripe_secret_key


from flask import Flask, jsonify, request

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_oN3IGfm2oUjOzAJ9bgAySwpfNx4yR8gZ'


@pay.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    a=json.loads(payload)
    requet=json.dumps(a)
    sig_header = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e

    # Handle the event
    if event['type'] == "invoice.paid":#follow
      subscription_schedule = event['data']['object']
      customer=subscription_schedule.customer
      subscription=subscription_schedule.lines['data'][0].subscription
      product_=subscription_schedule.lines['data'][0]['plan'].product
      client=User.query.filter_by(customer_id=customer).first()
      product=User.query.filter_by(product_id=product_).first()
      if client and product:
        client.follow(product)
        db.session.commit()
        sub=Subs(user=client.id,product_user=product.id,sub_id=subscription)
        db.session.add(sub)
        db.session.commit()

    if event['type'] == "checkout.session.completed":#pay post
        subscription_schedule = event['data']['object']
        if subscription_schedule.mode=="payment":
            client=User.query.filter_by(customer_id=subscription_schedule.customer).first()
            user=Posts.query.filter_by(product_id=subscription_schedule.client_reference_id).first()
            post_done=Posts_access(user=client.id,post=user.id)
            db.session.add(post_done)
            db.session.commit()




    # ... handle other event types
    if event['type'] == "customer.subscription.updated":#unfollow
        subscription_schedule = event['data']['object']
        product=Subs.query.filter(and_(Subs.sub_id==subscription_schedule.id,Subs.valid==True)).first()
        if product is not None:
            client=User.query.filter_by(id=product.user).first()
            product=User.query.filter_by(id=product.product_user).first()
            client.unfollow(product)
            product.valid=False
            db.session.commit()
    
    if event['type'] == "account.updated":#account verified
        subscription_schedule = event['data']['object']
        account=Account.query.filter_by(account_id=subscription_schedule['id']).first()
        account.valid=True#cheeck
        db.session.commit()
    else:
      print('Unhandled event type {}'.format(event['type']))

    return jsonify(success=True)


@pay.route('/index')
def index():
    return render_template('payment/index.html', key=Config.stripe_publishable_key)

@pay.route('/account/refresh/<string:id>', methods=['GET'])
def refresh(id):
    account = Account.query.filter_by(user=int(id)).first()
    account_links = stripe.AccountLink.create(
            account=account.account_id,
            refresh_url='http://127.0.0.1:5000/account/refresh/'+str(id),
            return_url='http://127.0.0.1:5000/',
            type='account_onboarding',
            )
    return redirect(account_links['url'])
    


@pay.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('payment/charge.html', amount=amount)



@pay.route('/charge/<int:id>/', methods=['GET','POST'])
def chargep(id):
    if current_user.is_authenticated:
        user=Posts.query.filter_by(user=id).first()
        acc=Account.query.filter_by(user=id).first()
        session = stripe.checkout.Session.create(
            customer=current_user.customer_id,
            client_reference_id=user.product_id,
            mode="payment",
            payment_method_types=['card','alipay'],
            line_items=[{
                'price':user.price_id,
                'quantity': 1,
            }],
            payment_intent_data={
                'application_fee_amount': 123,
                'transfer_data': {
                'destination': acc.account_id,
                },
            },
            success_url='http://127.0.0.1:5000/',
            cancel_url='https://example.com/cancel',
        )
        
        return redirect(session['url'])

    return redirect(url_for('users.login'))

