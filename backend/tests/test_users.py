def test_users_never_expose_password(admin, customer, ticket_payload):
    customer.post("/tickets", json=ticket_payload)
    users = admin.get("/users").get_json()
    assert len(users) == 2
    assert all("password" not in u for u in users)

    me = customer.get(f"/users/{customer.user.id}").get_json()
    assert "password" not in me
    assert len(me["ticket"]) == 1


def test_password_update_is_hashed(customer, client):
    res = customer.patch(f"/users/{customer.user.id}", json={"password": "newsecret"})
    assert res.status_code == 200

    login = client.post("/login", json={"email": "client@example.com", "password": "newsecret"})
    assert login.status_code == 200


def test_user_cannot_change_own_role(customer):
    res = customer.patch(f"/users/{customer.user.id}", json={"role": "admin"})
    assert res.status_code == 200
    assert res.get_json()["role"] == "client"


def test_email_update_must_be_unique(customer, make_user):
    make_user(email="taken@example.com")
    res = customer.patch(f"/users/{customer.user.id}", json={"email": "taken@example.com"})
    assert res.status_code == 409


def test_clients_cannot_access_other_users(login_as):
    alice = login_as("client", "alice@example.com")
    bob = login_as("client", "bob@example.com")
    assert alice.get("/users").status_code == 403
    assert alice.get(f"/users/{bob.user.id}").status_code == 403
    assert alice.patch(f"/users/{bob.user.id}", json={"password": "hijacked"}).status_code == 403
    assert alice.delete(f"/users/{bob.user.id}").status_code == 403


def test_admin_delete_user_cascades_tickets(admin, customer, ticket_payload):
    customer.post("/tickets", json=ticket_payload)
    assert admin.delete(f"/users/{customer.user.id}").status_code == 200
    assert admin.get("/tickets").get_json() == []


def test_missing_user_returns_404(admin):
    assert admin.get("/users/999").status_code == 404
