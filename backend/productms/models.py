from datetime import datetime
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Text, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType


import sys
sys.path.append("..")


db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer(), primary_key=True)

    first_name = db.Column(Text(), nullable=False)
    last_name = db.Column(Text(), nullable=False)

    contact_number = db.Column(Text(), nullable=False, unique=True)
    email = db.Column(EmailType(), nullable=False, unique=True)

    password = db.Column(Text(), nullable=False)

    def __init__(self, first_name, last_name, contact_number, email, password):
        self.first_name = first_name
        self.last_name = last_name

        self.contact_number = contact_number
        self.email = email

        self.password = password

    def __repr__(self):
        return f"User(name='{self.first_name} {self.last_name}', " \
               f"email='{self.email}'," \
               f" contact_number='{self.contact_number}')"
               
    def to_dict(self):
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        del result["password"]
        return result

class Product(db.Model):
    __tablename__ = 'product'
    prod_id = db.Column(Integer(), primary_key=True,
                        unique=True, autoincrement=True)
    name = db.Column(Text())
    photo = db.Column(Text())
    seller_id = db.Column(Integer(), ForeignKey(Users.id))
    initial_price = db.Column(Float())
    date = db.Column(DateTime(), default=datetime.now())
    increment = db.Column(Float())
    deadline_date = db.Column(DateTime())
    description = db.Column(Text())
    email_sent = db.Column(Boolean(), default = False)

    # Relationships
    seller = relationship("Users", backref="products")

    __table_args__ = (
        db.UniqueConstraint('prod_id'),
    )

    def to_dict(self):
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        del result["email_sent"]
        return result



class Bids(db.Model):
    __tablename__ = 'bids'
    bid_id = db.Column(Integer, primary_key=True, unique=True, autoincrement=True)
    prod_id = db.Column(Integer, ForeignKey(Product.prod_id))
    user_id = db.Column(Integer, ForeignKey(Users.id))
    bid_amount = db.Column(Float)
    created_at = db.Column(DateTime, default=datetime.now())

    # Relationships
    product = relationship("Product", backref="bids")
    user = relationship("Users", backref="bids")

    __table_args__ = (
        db.UniqueConstraint('prod_id', 'user_id'),
    )

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}