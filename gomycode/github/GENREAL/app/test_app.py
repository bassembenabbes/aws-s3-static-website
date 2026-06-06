from app import create_app


def test_health_endpoint():
    client = create_app().test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_index_endpoint():
    client = create_app().test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["service"] == "devops-starter-app"


def test_metrics_endpoint():
    client = create_app().test_client()
    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"app_requests_total" in response.data
