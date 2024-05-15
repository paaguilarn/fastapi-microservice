from fastapi.testclient import TestClient
from pytest import fixture

from api.main import app


@fixture(scope='session')
def client():
    return TestClient(app)
