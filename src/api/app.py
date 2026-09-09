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
models_dir = Path(__file__).resolve().parents[2] / "models"
latest_model = sorted(models_dir.glob("fraud_pipeline_v*.pkl"))[-1]
model = joblib.load(latest_model)
# model_path = Path(__file__).resolve().parents[2] / "models" / "fraud_pipeline_v1.pkl"
# model = joblib.load(model_path)
# model = mlflow.pyfunc.load_model(
#     model_uri="models:/credit_fraud_detector/Production"
# )

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "fraud": int(prediction),
        "probability": float(probability)
    }