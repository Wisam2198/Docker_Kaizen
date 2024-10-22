from conversion import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_convert(client):
    response = client.get('/convert?amount=100&from_currency=USD&to_currency=EUR')
    assert response.status_code == 200
    data = response.get_json()
    assert data['converted_amount'] is not None
