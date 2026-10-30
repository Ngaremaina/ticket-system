import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import create_app  # noqa: E402
from server.extensions import bcrypt, db  # noqa: E402
from server.models import Auth  # noqa: E402

PASSWORD = "secret123"


@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Anonymous (logged out) test client."""
    return app.test_client()


@pytest.fixture
def make_user(app):
    def _make_user(email="user@example.com", password=PASSWORD, role="client"):
        user = Auth(
            email=email,
            password=bcrypt.generate_password_hash(password).decode("utf-8"),
            role=role,
        )
        db.session.add(user)
        db.session.commit()
        return user

    return _make_user


@pytest.fixture
def login_as(app, make_user):
    """Create a user with the given role and return a test client logged in as them."""
    def _login_as(role="client", email=None):
        email = email or f"{role}@example.com"
        user = make_user(email=email, role=role)
        test_client = app.test_client()
        res = test_client.post("/login", json={"email": email, "password": PASSWORD})
        assert res.status_code == 200
        test_client.user = user
        return test_client

    return _login_as


@pytest.fixture
def admin(login_as):
    return login_as("admin")


@pytest.fixture
def customer(login_as):
    return login_as("client")


@pytest.fixture
def event_payload():
    return {
        "name": "Concert",
        "description": "Live music",
        "venue": "Nairobi",
        "date": "2026-12-01",
        "time": "18:00",
        "image": "https://example.com/concert.png",
        "max_attendees": 100,
    }


@pytest.fixture
def event(admin, event_payload):
    return admin.post("/events", json=event_payload).get_json()


@pytest.fixture
def ticket_payload():
    return {
        "name": "Concert",
        "description": "Live music",
        "venue": "Nairobi",
        "date": "2026-12-01",
        "time": "18:00",
        "image": "https://example.com/concert.png",
        "persons": 1,
        "type_name": "VIP",
        "price": 5000,
    }
