from flask import request
from flask_cors import CORS

from userms import main
from userms import models
from userms.app import app
from userms.main.api import api
from userms.main.database import db, migration

CORS(app, support_credentials=True)

db.init_app(app)
migration.init_app(app, db)
api.init_app(app)
