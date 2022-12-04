from userms import main
from userms.app import app
from userms.main.api import api
from userms.main.database import db, migration

from userms import models

db.init_app(app)
migration.init_app(app, db)
api.init_app(app)
