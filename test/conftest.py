import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    # Prepare before your test
    app.config["TESTING"] = True
    with app.test_client() as client:
        # Give control to your test
        yield client
    # Cleanup after the test run.
    # ... nothing here, for this simple example