from . import db # import the db instance from the package __init__.py file
from flask_login import UserMixin # import UserMixin to add default implementations for user methods
from sqlalchemy.sql import func # import func to use SQL functions like current timestamp


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True) # unique identifier for each password entry
    website = db.Column(db.String(150)) # website field
    username = db.Column(db.String(150)) # username field

# encrypted password field
    encryypted_password = db.Column(db.String(250)) # encrypted password field
    salt = db.Column(db.LargeBinary) # salt used for encryption

# extra fields
    category = db.Column(db.String(100)) # category field
    notes = db.Column(db.Text) # notes field

#foreign key 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # foreign key to link to User

# timestamps
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # timestamp of creation
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now()) # timestamp of last update


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # unique identifier for each user
    email = db.Column(db.String(150), unique=True) # email field, must be unique
    password = db.Column(db.String(200)) # password field
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # timestamp of creation

# relationship to Password model
    passwords = db.relationship('Password') # relationship to Password model
    