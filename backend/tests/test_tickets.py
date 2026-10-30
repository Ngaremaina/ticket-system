from server.routes.tickets import MAX_TICKETS_PER_USER


def test_booking_belongs_to_logged_in_user(customer, make_user, ticket_payload):
    other = make_user(email="other@example.com")
    # A client cannot book on behalf of someone else: auth_id comes from the session
    res = customer.post("/tickets", json={**ticket_payload, "auth_id": other.id})
    assert res.status_code == 201
    assert res.get_json()["auth_id"] == customer.user.id


def test_booking_requires_login(client, ticket_payload):
    assert client.post("/tickets", json=ticket_payload).status_code == 401


def test_booking_limit(customer, ticket_payload):
    for _ in range(MAX_TICKETS_PER_USER):
        assert customer.post("/tickets", json=ticket_payload).status_code == 201
    res = customer.post("/tickets", json=ticket_payload)
    assert res.status_code == 400
    assert "at most" in res.get_json()["error"]


def test_ticket_requires_fields(customer):
    assert customer.post("/tickets", json={"name": "Concert"}).status_code == 400


def test_clients_only_see_their_own_tickets(login_as, admin, ticket_payload):
    alice = login_as("client", "alice@example.com")
    bob = login_as("client", "bob@example.com")
    alice_ticket = alice.post("/tickets", json=ticket_payload).get_json()
    bob.post("/tickets", json=ticket_payload)

    assert [t["auth_id"] for t in alice.get("/tickets").get_json()] == [alice.user.id]
    assert len(admin.get("/tickets").get_json()) == 2

    assert bob.get(f"/tickets/{alice_ticket['id']}").status_code == 403
    assert bob.delete(f"/tickets/{alice_ticket['id']}").status_code == 403
    assert alice.get(f"/tickets/{alice_ticket['id']}").status_code == 200


def test_client_can_cancel_own_ticket(customer, ticket_payload):
    ticket = customer.post("/tickets", json=ticket_payload).get_json()
    assert customer.delete(f"/tickets/{ticket['id']}").status_code == 200
    assert customer.get(f"/tickets/{ticket['id']}").status_code == 404


def test_only_admin_can_edit_tickets(admin, customer, ticket_payload):
    ticket = customer.post("/tickets", json=ticket_payload).get_json()
    assert customer.patch(f"/tickets/{ticket['id']}", json={"price": 1}).status_code == 403

    res = admin.patch(f"/tickets/{ticket['id']}", json={"persons": 2})
    assert res.status_code == 200
    assert res.get_json()["persons"] == 2
