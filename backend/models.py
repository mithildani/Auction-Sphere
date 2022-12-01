from datetime import datetime
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True,
                        unique=True, autoincrement=True)
    first_name = db.Column(db.Text())
    last_name = db.Column(db.Text())
    contact_number = db.Column(db.Text(), unique=True)
    email = db.Column(db.Text(), unique=True)
    password = db.Column(db.Text())

    __table_args__ = (
        db.UniqueConstraint('user_id'),
    )


class Product(db.Model):
    __tablename__ = 'product'
    prod_id = db.Column(db.Integer, primary_key=True,
                        unique=True, autoincrement=True)
    name = db.Column(db.Text())
    photo = db.Column(db.Text())
    seller_email = db.Column(db.Text(), ForeignKey("users.email"))
    initial_price = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.now())
    increment = db.Column(db.Float)
    deadline_date = db.Column(db.DateTime)
    description = db.Column(db.Text())
    email_sent = db.Column(db.Boolean(), default = False)

    __table_args__ = (
        db.UniqueConstraint('prod_id'),
    )


class Bids(db.Model):
    __tablename__ = 'bids'
    prod_id = db.Column(db.Integer, ForeignKey(
        "product.prod_id"), primary_key=True)
    email = db.Column(db.Text(), ForeignKey("users.email"), primary_key=True)
    bid_amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now())

    # __table_args__ = (
    #     db.UniqueConstraint('prod_id'),
    # )


class Claims(db.Model):
    __tablename__ = 'claims'
    prod_id = db.Column(db.Integer, ForeignKey(
        "product.prod_id"), primary_key=True)
    email = db.Column(db.Text(), ForeignKey("users.email"), primary_key=True)
    expiry_date = db.Column(db.DateTime, default=datetime.now())
    claim_status = db.Column(db.Integer)
