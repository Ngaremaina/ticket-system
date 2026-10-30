import pytest

ADMIN_ONLY = [
    ("post", "/events"),
    ("patch", "/events/1"),
    ("delete", "/events/1"),
    ("post", "/types"),
    ("patch", "/types/1"),
    ("delete", "/types/1"),
    ("patch", "/tickets/1"),
    ("get", "/users"),
    ("delete", "/users/1"),
]

LOGIN_REQUIRED = [
    ("get", "/tickets"),
    ("get", "/tickets/1"),
    ("post", "/tickets"),
    ("delete", "/tickets/1"),
    ("get", "/users/1"),
    ("patch", "/users/1"),
]

PUBLIC = [
    ("get", "/events"),
    ("get", "/types"),
    ("get", "/health"),
]


@pytest.mark.parametrize("method,url", ADMIN_ONLY + LOGIN_REQUIRED)
def test_anonymous_is_rejected(client, method, url):
    assert getattr(client, method)(url, json={}).status_code == 401


@pytest.mark.parametrize("method,url", ADMIN_ONLY)
def test_clients_are_forbidden_from_admin_routes(customer, method, url):
    assert getattr(customer, method)(url, json={}).status_code == 403


@pytest.mark.parametrize("method,url", PUBLIC)
def test_public_routes(client, method, url):
    assert getattr(client, method)(url).status_code == 200
