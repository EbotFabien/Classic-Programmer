import os

basedir= os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY='FABIENCLASSIC'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'prototype.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME = 'touchone0001@gmail.com'
    MAIL_PASSWORD = 'onetouch000100'
    stripe_secret_key= 'sk_test_IRUKv5saDJtl2B605DVTYm6I00Si1ogtf5'
    stripe_publishable_key= 'pk_test_NFegWC0KCmYbYcdODYzmf7pJ00TGEsHHbh'











class Development(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8000

class Production(Config):
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 80


config = {
    'dev': Development,
    'prod': Production,
    'default': Development
}
