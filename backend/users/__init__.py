import os

from flask import Flask

from users import main
from users.main.api import api
from users.main.database import db, migration

app = Flask(__name__)
app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])

from users import models

db.init_app(app)
migration.init_app(app, db)
api.init_app(app)
