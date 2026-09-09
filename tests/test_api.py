import pytest
from fastapi.testclient import TestClient
from src.api.app import app  # adjust import path

client = TestClient(app)

def test_predict_valid_input():
    payload = {
        "amount_usd": 1250.50,
        "merchant_category": "Electronics",
        "card_type": "Visa",
        "auth_method": "OTP",
        "channel": "Online",
        "device_type": "Android Phone",
        "is_foreign_transaction": 0,
        "hours_since_last_txn": 2.5,
        "txn_count_last_24h": 4,
        "distance_from_home_km": 8.7,
        "is_new_merchant": 0,
        "used_vpn": 0,
        "card_age_months": 36,
        "customer_age": 29,
        "transaction_duration_sec": 18,
        "amount_to_balance_ratio": 0.08,
        "account_balance_usd": 15000,
        "ip_country_mismatch": 0,
        "billing_shipping_mismatch": 0,
        "cvv_retry_count": 0,
        "velocity_score": 0.15,
        "time_of_day_hour": 14,
        "day_of_week": "Tuesday",
        "is_ai_generated_scam_attempt": 0,
        "merchant_risk_score": 22.5,
        "prior_disputes": 1
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "fraud" in data
    assert "probability" in data
    assert isinstance(data["fraud"], int)
    assert isinstance(data["probability"], float)

def test_predict_invalid_input():
    # Wrong type for numeric field
    payload = {
        "amount_usd": "not_a_number",
        "merchant_category": "Electronics"
    }

    response = client.post("/predict", json=payload)
    assert response.status_code in (400, 422)
