import os

from flask import Flask

from userms import main


def create_app():
	app_ = Flask("userms")
	app_.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])

	return app_


app = create_app()
