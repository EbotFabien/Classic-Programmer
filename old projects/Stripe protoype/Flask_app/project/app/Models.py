from flask import current_app
from itsdangerous import  TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from app import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

followers = db.Table('followers',
    db.Column('follower_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('followed_id',db.Integer,db.ForeignKey('user.id')),
)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(60))
    product_id = db.Column(db.String(60))
    customer_id = db.Column(db.String(60))
    price = db.Column(db.Float())
    price_id = db.Column(db.String(60))
    paid = db.Column(db.Boolean,default=False)

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    

    def get_reset_token(self,expire_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'],expire_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')
        
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token) ['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return '<User %r>' %self.id

    def is_following(self,user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def follow(self,user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self,user):
        if self.is_following(user):
            self.followed.remove(user)

    def has_followed(self):
        return User.query.join(
            followers,(followers.c.followed_id == User.id)).filter(
                followers.c.follower_id == self.id).all() 
 
    def is_followers(self):
        return User.query.join(
            followers,(followers.c.follower_id == User.id)).filter(
                followers.c.followed_id == self.id).all()


 
class Subs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'))
    product_user = db.Column(db.Integer,db.ForeignKey('user.id'))
    sub_id = db.Column(db.String(60))
    valid = db.Column(db.Boolean,default=True)

    def __repr__(self):
        return '<Subs %r>' %self.id


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'))
    account_id = db.Column(db.String(60))
    valid = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<Account %r>' %self.id



class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'))
    content = db.Column(db.String(60))
    product_id = db.Column(db.String(60))
    price = db.Column(db.Float())
    price_id = db.Column(db.String(60))
    paid = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<Posts %r>' %self.id

class Posts_access(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer,db.ForeignKey('user.id'))
    post = db.Column(db.Integer,db.ForeignKey('posts.id'))

    def __repr__(self):
        return '<Posts_access %r>' %self.id