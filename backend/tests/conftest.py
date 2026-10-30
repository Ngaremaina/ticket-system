import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import create_app  # noqa: E402
from server.extensions import bcrypt, db  # noqa: E402
from server.models import Auth  # noqa: E402


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
    return app.test_client()


@pytest.fixture
def make_user(app):
    def _make_user(email="user@example.com", password="secret123", role="client"):
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
def event(client, event_payload):
    return client.post("/events", json=event_payload).get_json()
