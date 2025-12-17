from . import db # import the db instance from the package __init__.py file
from flask_login import UserMixin # import UserMixin to add default implementations for user methods
from sqlalchemy.sql import func # import func to use SQL functions like current timestamp


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True) # unique identifier for each password entry
    website = db.Column(db.String(150)) # website field
    username = db.Column(db.String(150)) # username field
    password = db.Column(db.String(250)) # password field
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # foreign key to link to User
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # timestamp of creation


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # unique identifier for each user
    email = db.Column(db.String(150), unique=True) # email field, must be unique
    password = db.Column(db.String(200)) # password field
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # timestamp of creation
    passwords = db.relationship('Password') # relationship to Password model
