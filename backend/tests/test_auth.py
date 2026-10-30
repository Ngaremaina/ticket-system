def test_register_creates_client(client):
    res = client.post("/register", json={"email": "New@Example.com", "password": "secret123"})
    assert res.status_code == 201
    assert res.get_json()["email"] == "new@example.com"


def test_register_ignores_requested_role(client):
    client.post("/register", json={"email": "a@example.com", "password": "secret123", "role": "admin"})
    res = client.post("/login", json={"email": "a@example.com", "password": "secret123"})
    assert res.get_json()["role"] == "client"


def test_register_duplicate_email(client, make_user):
    make_user(email="dup@example.com")
    res = client.post("/register", json={"email": "dup@example.com", "password": "secret123"})
    assert res.status_code == 409


def test_register_validates_payload(client):
    res = client.post("/register", json={"email": "not-an-email", "password": "1"})
    assert res.status_code == 400
    assert set(res.get_json()["details"]) == {"email", "password"}


def test_login_success_sets_session(client, make_user):
    user = make_user(role="admin")
    res = client.post("/login", json={"email": "user@example.com", "password": "secret123"})
    assert res.status_code == 200
    assert res.get_json() == {"id": user.id, "email": "user@example.com", "role": "admin"}

    me = client.get("/current_user")
    assert me.status_code == 200
    assert me.get_json()["id"] == user.id


def test_login_unknown_user(client):
    res = client.post("/login", json={"email": "ghost@example.com", "password": "secret123"})
    assert res.status_code == 401


def test_login_wrong_password(client, make_user):
    make_user()
    res = client.post("/login", json={"email": "user@example.com", "password": "wrongpass"})
    assert res.status_code == 401


def test_current_user_requires_session(client):
    assert client.get("/current_user").status_code == 401


def test_logout_clears_session(client, make_user):
    make_user()
    client.post("/login", json={"email": "user@example.com", "password": "secret123"})
    assert client.post("/logout").status_code == 200
    assert client.get("/current_user").status_code == 401


def test_create_admin_cli(app):
    runner = app.test_cli_runner()
    result = runner.invoke(args=["create-admin", "boss@example.com"], input="secret123\nsecret123\n")
    assert result.exit_code == 0, result.output

    from server.models import Auth

    assert Auth.query.filter_by(email="boss@example.com").one().role == "admin"
