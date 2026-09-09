# Risk-Aware-Credit-Decisioning-System

conda activate credit_fraud_detection
uvicorn src.api.app:app --reload
Test Predict API:
{
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

Start MLFlow : mlflow ui