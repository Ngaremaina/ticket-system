def test_type_crud(admin, event):
    res = admin.post("/types", json={"name": "Regular", "price": 1000, "event_id": event["id"]})
    assert res.status_code == 201
    type_id = res.get_json()["id"]

    assert admin.get(f"/events/{event['id']}").get_json()["type"][0]["name"] == "Regular"

    res = admin.patch(f"/types/{type_id}", json={"price": 1500})
    assert res.get_json()["price"] == 1500

    assert admin.delete(f"/types/{type_id}").status_code == 200
    assert admin.get(f"/types/{type_id}").status_code == 404


def test_type_rejects_negative_price(admin, event):
    res = admin.post("/types", json={"name": "Bad", "price": -1, "event_id": event["id"]})
    assert res.status_code == 400


def test_types_are_publicly_readable(client, admin, event):
    admin.post("/types", json={"name": "VIP", "price": 5000, "event_id": event["id"]})
    assert len(client.get("/types").get_json()) == 1
