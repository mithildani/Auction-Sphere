from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from userms.app import app

db = SQLAlchemy(app)

migration = Migrate(directory='./userms/migrations')
