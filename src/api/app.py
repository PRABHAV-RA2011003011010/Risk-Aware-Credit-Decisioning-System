from fastapi import FastAPI
import joblib
import pandas as pd
from pathlib import Path
import mlflow.pyfunc

app = FastAPI(
    title="Credit Card Fraud Detection API",
    version="1.0"
)

# Load trained pipeline
# model_path = Path(__file__).resolve().parents[2] / "models" / "fraud_pipeline.pkl"
model = mlflow.pyfunc.load_model(
    model_uri="models:/credit_fraud_detector/Production"
)

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "fraud": int(prediction),
        "probability": float(probability)
    }