from datetime import datetime
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Text, Boolean, Float, DateTime
from sqlalchemy_utils import EmailType
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship

import sys
sys.path.append("..")
from userms.models import Users


db = SQLAlchemy()

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


class Bids(db.Model):
    __tablename__ = 'bids'
    bid_id = db.Column(Integer, primary_key=True, unique=True, autoincrement=True)
    prod_id = db.Column(Integer, ForeignKey(Product.prod_id))
    user_id = db.Column(Integer, ForeignKey(Users.id), primary_key=True)
    bid_amount = db.Column(Float)
    created_at = db.Column(DateTime, default=datetime.now())

    # Relationships
    product = relationship("Product", backref="bids")
    user = relationship("Users", backref="bids")

    __table_args__ = (
        db.UniqueConstraint('prod_id', 'user_id'),
    )
