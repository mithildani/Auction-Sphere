import os

import pytest

from userms.app import app as userms_app
from userms.main.database import db, migration


os.environ["FLASK_ENV"] = "testing"


@pytest.fixture(scope='session')
def app():
    with userms_app.app_context():
        db.init_app(userms_app)
        db.create_all()
        migration.init_app(userms_app, db)
        # api.init_app(userms_app)

        yield userms_app

        db.drop_all()


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture(scope="session")
def runner(app):
    return app.test_cli_runner()


def test_request_example(app, client):
    response = client.post("/users/api/signup", json={
        "firstName": "Sam",
        "lastName": "Mason",
        "email": "sam.mason@gmail.com",
        "contact": "1234567890",
        "password": "1234"
    }, headers={
        "Content-Type": "application/json"
    })

    print("Hi,", response.text)

    assert response.json["message"] == "Added successfully"
