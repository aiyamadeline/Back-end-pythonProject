import pytest
from ..backend.app import create_app
from ..backend.storage import DBstorage

@pytest.fixture()
def app():
    app = create_app("sqlite://")

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
