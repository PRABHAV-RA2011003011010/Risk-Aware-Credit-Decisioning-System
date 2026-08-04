from pathlib import Path
import joblib
import mlflow
import mlflow.sklearn

# Project root
project_root = Path(__file__).resolve().parents[2]

# Point to the same MLflow tracking store used during training
mlflow.set_tracking_uri(
    f"file:///{(project_root / 'mlruns').as_posix()}"
)

# Load the Production model
model = mlflow.sklearn.load_model(
    "models:/credit_fraud_detector/Production"
)

# Export directory
models_dir = project_root / "models"
models_dir.mkdir(exist_ok=True)

# Save the model
output_path = models_dir / "fraud_pipeline.pkl"

joblib.dump(model, output_path)

print(f"Production model exported to:\n{output_path}")