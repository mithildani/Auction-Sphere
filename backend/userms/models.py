from sqlalchemy import Integer, Text
from sqlalchemy_utils import EmailType

from userms.main.database import db


"""This model is duplicated in backend/productms/models.py"""
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
