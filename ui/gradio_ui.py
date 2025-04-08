import gradio as gr
import requests

# Use container service name instead of localhost
API_URL = "http://churn-fastapi:8080/predict"

def predict_churn(
    SeniorCitizen: int,
    tenure: int,
    MonthlyCharges: float,
    TotalCharges: float,
    gender: str,
    Partner: str,
    Dependents: str,
    PhoneService: str,
    MultipleLines: str,
    InternetService: str,
    OnlineSecurity: str,
    OnlineBackup: str,
    DeviceProtection: str,
    TechSupport: str,
    StreamingTV: str,
    StreamingMovies: str,
    Contract: str,
    PaperlessBilling: str,
    PaymentMethod: str
):
    payload = [{
        "SeniorCitizen": SeniorCitizen,
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "gender": gender,
        "Partner": Partner,
        "Dependents": Dependents,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod
    }]

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            return f"Prediction: {response.json()['predictions'][0]}"
        else:
            return f"Error: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

# Define inputs with validation
inputs = [
    gr.Dropdown([0, 1], label="Senior Citizen (0=No, 1=Yes)", type="index"),
    gr.Number(label="Tenure (months)", minimum=0, maximum=100, step=1),
    gr.Number(label="Monthly Charges ($)", minimum=0, maximum=200, step=1),
    gr.Number(label="Total Charges ($)", minimum=0, maximum=10000, step=1),
    gr.Dropdown(["Male", "Female"], label="Gender"),
    gr.Dropdown(["Yes", "No"], label="Partner"),
    gr.Dropdown(["Yes", "No"], label="Dependents"),
    gr.Dropdown(["Yes", "No"], label="Phone Service"),
    gr.Dropdown(["Yes", "No", "No phone service"], label="Multiple Lines"),
    gr.Dropdown(["DSL", "Fiber optic", "No"], label="Internet Service"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Online Security"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Online Backup"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Device Protection"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Tech Support"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Streaming TV"),
    gr.Dropdown(["Yes", "No", "No internet service"], label="Streaming Movies"),
    gr.Dropdown(["Month-to-month", "One year", "Two year"], label="Contract"),
    gr.Dropdown(["Yes", "No"], label="Paperless Billing"),
    gr.Dropdown(
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
        label="Payment Method"
    )
]

gr.Interface(
    fn=predict_churn,
    inputs=inputs,
    outputs="text",
    title="Customer Churn Predictor",
    description="Enter customer details to predict churn risk",
    allow_flagging="never"
).launch()