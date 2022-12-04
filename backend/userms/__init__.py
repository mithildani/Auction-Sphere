import os

from flask import Flask

from userms import main
from userms.main.api import api
from userms.main.database import db, migration
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])

from userms import models

db.init_app(app)
migration.init_app(app, db)
api.init_app(app)
