from fastapi import status


def test_health(client):
    response = client.get("/health")

    assert response.status_code == status.HTTP_200_OK
