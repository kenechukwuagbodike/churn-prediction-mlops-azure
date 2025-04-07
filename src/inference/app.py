from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI()

# Automatically resolve the directory the script is in
base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, "model.pkl")

model = joblib.load(model_path)

# Define expected input
class ChurnInput(BaseModel):
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender: int
    Partner: int
    Dependents: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int

@app.post("/predict")
def predict_churn(data: ChurnInput):
    try:
        input_df = pd.DataFrame([data.dict()])

        # Enforce correct feature order
        model_features = [
            'SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'gender',
            'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService',
            'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
            'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
            'PaymentMethod'
        ]

        input_df = input_df[model_features]
        

        pred = model.predict(input_df)[0]
        return {"churn_prediction": int(pred)}
    except Exception as e:
        return {"error": str(e)}

