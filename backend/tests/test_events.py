def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok", "database": "ok"}


def test_list_events_empty(client):
    res = client.get("/events")
    assert res.status_code == 200
    assert res.get_json() == []


def test_create_and_fetch_event(client, event_payload):
    res = client.post("/events", json=event_payload)
    assert res.status_code == 201
    created = res.get_json()
    assert created["name"] == "Concert"
    assert created["type"] == []

    assert client.get(f"/events/{created['id']}").get_json()["name"] == "Concert"
    assert client.get("/events/Concert").get_json()["id"] == created["id"]
    assert len(client.get("/events").get_json()) == 1


def test_create_event_missing_fields(client):
    res = client.post("/events", json={"name": "Incomplete"})
    assert res.status_code == 400
    assert "venue" in res.get_json()["details"]


def test_create_event_ignores_client_id(client, event_payload):
    res = client.post("/events", json={**event_payload, "id": 999})
    assert res.status_code == 201
    assert res.get_json()["id"] != 999


def test_update_event_partial(client, event):
    res = client.patch(f"/events/{event['id']}", json={"venue": "Mombasa"})
    assert res.status_code == 200
    body = res.get_json()
    assert body["venue"] == "Mombasa"
    assert body["name"] == "Concert"


def test_delete_event_cascades_types(client, event):
    client.post("/types", json={"name": "VIP", "price": 5000, "event_id": event["id"]})
    res = client.delete(f"/events/{event['id']}")
    assert res.status_code == 200
    assert client.get(f"/events/{event['id']}").status_code == 404
    assert client.get("/types").get_json() == []


def test_missing_event_returns_404(client):
    assert client.get("/events/12345").status_code == 404
    assert client.get("/events/does-not-exist").status_code == 404
    assert client.patch("/events/12345", json={"venue": "x"}).status_code == 404
    assert client.delete("/events/12345").status_code == 404
