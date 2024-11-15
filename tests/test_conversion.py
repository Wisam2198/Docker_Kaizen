from conversion import app
import pytest
from unittest.mock import patch


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Exemple de mock pour l'API
@patch("conversion.requests.get")
def test_convert(mock_get, client):
    # Simule la réponse de l'API
    mock_get.return_value.json.return_value = {
        "conversion_rates": {"EUR": 0.85, "USD": 1.0, "GBP": 0.75}
    }

    # Test de conversion valide
    response = client.get("/convert?amount=100&from_currency=USD&to_currency=EUR")
    assert response.status_code == 200
    data = response.get_json()
    assert data["converted_amount"] == 85.0  # 100 * 0.85


# Test pour une devise non valide
@patch("conversion.requests.get")
def test_convert_invalid_currency(mock_get, client):
    mock_get.return_value.json.return_value = {
        "conversion_rates": {"EUR": 0.85, "USD": 1.0, "GBP": 0.75}
    }

    response = client.get("/convert?amount=100&from_currency=USD&to_currency=XYZ")
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


# Test pour un montant non numérique
@patch("conversion.requests.get")
def test_convert_non_numeric_amount(mock_get, client):
    mock_get.return_value.json.return_value = {
        "conversion_rates": {"EUR": 0.85, "USD": 1.0, "GBP": 0.75}
    }

    response = client.get(
        "/convert?amount=not_a_number&from_currency=USD&to_currency=EUR"
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
