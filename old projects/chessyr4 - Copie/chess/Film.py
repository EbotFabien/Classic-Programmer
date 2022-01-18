from flask import Flask,render_template,url_for,flash,redirect,request
from flask_bootstrap import Bootstrap
import  Form  as f  
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,current_user,logout_user,login_required,LoginManager
from flask_bcrypt import Bcrypt
from sqlalchemy import ForeignKeyConstraint,ForeignKey,UniqueConstraint
from datetime import datetime
from pythonProject1.main import main
from flask_login import UserMixin
import sys
import threading

app = Flask(__name__)
#bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bot.db'
app.config['SECRET_KEY'] ='fabs' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = 'User'

    id = db.Column(db.Integer,primary_key=True)
    User_name = db.Column(db.String(80))
    Password = db.Column(db.String(300))
    email = db.Column(db.String(300))
    
    

    def __repr__(self):
        return '<User %r>' %self.id
class Bot(db.Model):
    __tablename__ = 'Bot'
    id = db.Column(db.Integer,primary_key=True)
    token = db.Column(db.String(300))
    bot= db.Column(db.String(80))
    phone = db.Column(db.String(300))
    Name = db.Column(db.String(300))
    user= db.Column(db.Integer, ForeignKey('User.id', onupdate="CASCADE", ondelete="CASCADE"))

    def __repr__(self):
        return '<Bot %r>' %self.id

class Bot_data(db.Model):
    __tablename__ = 'Bot_data'

    id = db.Column(db.Integer,primary_key=True)
    bot = db.Column(db.Integer, ForeignKey('Bot.id', onupdate="CASCADE", ondelete="CASCADE"))
    question = db.Column(db.String(80) )
    response = db.Column(db.String(300))
    
    def __repr__(self):
        return '<Bot_data %r>' %self.id

class Bot_responses(db.Model):
    __tablename__ = 'Bot_responses'

    id = db.Column(db.Integer,primary_key=True)
    bot = db.Column(db.Integer, ForeignKey('Bot.id', onupdate="CASCADE", ondelete="CASCADE"))
    user_name = db.Column(db.String(300))
    user_message = db.Column(db.String(300))
    botresponse = db.Column(db.String(300))
    date=db.Column(db.DateTime(),default=datetime.utcnow)
    
    def __repr__(self):
        return '<Bot_responses %r>' %self.id


db.create_all()





    
@app.route('/login',methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
       return redirect(url_for('dashboard'))
    form = f.LoginForm()
    if form.validate_on_submit():
        name=User.query.filter_by(User_name=form.username.data).first()
        if  name and bcrypt.check_password_hash(name.Password,form.password.data):
            login_user(name)
            next_page=request.args.get('next')
            return redirect (next_page) if next_page else  redirect(url_for('dashboard'))
        else:
            flash(f'Wrong email or password','danger')

    return render_template('login.html',legend="login",form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if current_user.is_authenticated:
       return redirect(url_for('dashboard'))
    form = f.RegistrationForm()
    print('ok')
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(User_name=form.username.data, email=form.email.data )
        db.session.add(user)
        db.session.commit()
        user.Password=hashed_password
        db.session.commit()
        flash(f'Account created you can now login','success')
        return redirect(url_for('login'))
    return render_template('signup.html',legend="sign_up",form=form)

@app.route('/customize/<int:id>/bots',methods=['GET','POST'])
def customize(id):
    form = f.questionform()
    if form.validate_on_submit():
        bot=Bot_data(bot=id,question=form.question.data,response=form.response.data)
        db.session.add(bot)
        db.session.commit()
        return redirect(url_for('viewresponse',id=id))
    return render_template('addresponse.html',legend="custom",form=form)

@app.route('/create/<int:id>/bots',methods=['GET','POST'])
def createBot(id):
    form = f.BotForm()
    if form.validate_on_submit():
        user=User.query.filter_by(id=int(id)).first()
        bot_new=Bot(user=id,Name=form.Bot_name.data,token=form.token.data)
        db.session.add(bot_new)
        db.session.commit()
        return redirect(url_for('viewbot',id=id))
    return render_template('createbot.html',legend="create",form=form)

@app.route('/view/<int:id>/bots',methods=['GET','POST'])
def viewbot(id):
    if current_user.is_authenticated:
        Bots=list(Bot.query.filter_by(user=int(id)).all())
        return render_template('botpage.html',legend="viewbot",bot=Bots)
    return redirect(url_for('login'))

@app.route('/response/<int:id>/bots',methods=['GET','POST'])
def viewresponse(id):
    if current_user.is_authenticated:
        Bots=list(Bot_data.query.filter_by(bot=int(id)).all())
        return render_template('viewresponse.html',legend="response",bot=Bots)
    return redirect(url_for('login'))

@app.route('/convo/<int:id>/bots',methods=['GET','POST'])
def viewconvo(id):
    if current_user.is_authenticated:
        Bots=list(Bot_responses.query.filter_by(bot=int(id)).all())
        return render_template('convo.html',legend="convo",bot=Bots)
    return redirect(url_for('login'))

@app.route('/bot/<string:token>/<int:id>/start',methods=['GET','POST'])
def botprocess(token,id):
    if current_user.is_authenticated:
        bot=Bot.query.filter_by(token=token).first()
        if id==1:
            main(token)
            return redirect(url_for('viewconvo',id=bot.id))
        if id==0:
            return redirect(url_for('dashboard'))#botactivity
        return render_template('dashboard.html',legend="Board")
    return redirect(url_for('login'))

@app.route('/delete/customize/<int:id>/bots',methods=['GET','POST'])
def deletecustom(id):
    if current_user.is_authenticated:
        bot=Bot.query.filter_by(Bot_data=id).delete()
        db.session.commit()
        return redirect(url_for('viewresponse',id=id))
    return redirect(url_for('login'))
@app.route('/')
def dashboard():
    if current_user.is_authenticated:
        return render_template('dashboard.html',legend="Board")
    return redirect(url_for('login'))

'''@app.route('/')
def dashboard():
    if current_user.is_authenticated:
        return render_template('dashboard.html',legend="Board")
    return redirect(url_for('login'))'''



if __name__ == '__main__':
    
    app.run()


#botactivity