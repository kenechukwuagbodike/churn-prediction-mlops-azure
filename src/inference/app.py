from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from enum import Enum

app = FastAPI()
pipeline = joblib.load("src/inference/pipeline.pkl")

# Enums for categorical validation
class YesNo(str, Enum):
    yes = "Yes"
    no = "No"

class YesNoService(str, Enum):
    Yes = "Yes"
    No = "No"
    NoService = "No internet service"

class Gender(str, Enum):
    male = "Male"
    female = "Female"

class InternetService(str, Enum):
    dsl = "DSL"
    fiber = "Fiber optic"
    no = "No"

class Contract(str, Enum):
    monthly = "Month-to-month"
    one_year = "One year"
    two_year = "Two year"

class PaymentMethod(str, Enum):
    electronic = "Electronic check"
    mailed = "Mailed check"
    transfer = "Bank transfer (automatic)"
    credit = "Credit card (automatic)"

class ChurnInput(BaseModel):
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender: Gender
    Partner: YesNo
    Dependents: YesNo
    PhoneService: YesNo
    MultipleLines: YesNoService
    InternetService: InternetService
    OnlineSecurity: YesNoService
    OnlineBackup: YesNoService
    DeviceProtection: YesNoService
    TechSupport: YesNoService
    StreamingTV: YesNoService
    StreamingMovies: YesNoService
    Contract: Contract
    PaperlessBilling: YesNo
    PaymentMethod: PaymentMethod

@app.post("/predict")
async def predict(input_data: list[ChurnInput]):
    try:
        # Convert input to DataFrame
        df = pd.DataFrame([item.dict() for item in input_data])
        
        # Get predictions
        predictions = pipeline.predict(df).tolist()
        
        # Convert to human-readable labels
        churn_labels = [
            "No Churn" if pred == 0 else "Churn"
            for pred in predictions
        ]
        
        return {"predictions": churn_labels}
        
    except Exception as e:
        return {"error": str(e)}