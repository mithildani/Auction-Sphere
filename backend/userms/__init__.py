from userms import main
from userms.app import app
from userms.main.api import api
from userms.main.database import db, migration
from flask_cors import CORS

from userms import models

CORS(app, support_credentials=True)

db.init_app(app)
migration.init_app(app, db)
api.init_app(app)
