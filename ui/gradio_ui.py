import gradio as gr
import requests
from collections import OrderedDict

API_URL = "http://churnapi21017.westeurope.azurecontainer.io:8000/predict"

def predict_churn(
    SeniorCitizen, tenure, MonthlyCharges, TotalCharges, gender, Partner, Dependents,
    PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup,
    DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract,
    PaperlessBilling, PaymentMethod
):
    payload = OrderedDict([
        ("SeniorCitizen", SeniorCitizen),
        ("tenure", tenure),
        ("MonthlyCharges", MonthlyCharges),
        ("TotalCharges", TotalCharges),
        ("gender", gender),
        ("Partner", Partner),
        ("Dependents", Dependents),
        ("PhoneService", PhoneService),
        ("MultipleLines", MultipleLines),
        ("InternetService", InternetService),
        ("OnlineSecurity", OnlineSecurity),
        ("OnlineBackup", OnlineBackup),
        ("DeviceProtection", DeviceProtection),
        ("TechSupport", TechSupport),
        ("StreamingTV", StreamingTV),
        ("StreamingMovies", StreamingMovies),
        ("Contract", Contract),
        ("PaperlessBilling", PaperlessBilling),
        ("PaymentMethod", PaymentMethod)
    ])

    response = requests.post(API_URL, json=payload)
    return response.json()

# Build UI
demo = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Radio([0, 1], label="SeniorCitizen"),
        gr.Slider(0, 72, step=1, label="tenure"),
        gr.Number(label="MonthlyCharges"),
        gr.Number(label="TotalCharges"),
        gr.Radio([0, 1], label="gender"),
        gr.Radio([0, 1], label="Partner"),
        gr.Radio([0, 1], label="Dependents"),
        gr.Radio([0, 1], label="PhoneService"),
        gr.Radio([0, 1], label="MultipleLines"),
        gr.Dropdown([0, 1, 2], label="InternetService"),
        gr.Radio([0, 1], label="OnlineSecurity"),
        gr.Radio([0, 1], label="OnlineBackup"),
        gr.Radio([0, 1], label="DeviceProtection"),
        gr.Radio([0, 1], label="TechSupport"),
        gr.Radio([0, 1], label="StreamingTV"),
        gr.Radio([0, 1], label="StreamingMovies"),
        gr.Dropdown([0, 1, 2], label="Contract"),
        gr.Radio([0, 1], label="PaperlessBilling"),
        gr.Dropdown([0, 1, 2, 3], label="PaymentMethod")
    ],
    outputs="json",
    title="Churn Prediction App",
    description="Enter customer features to get churn prediction from your live Azure-hosted model!"
)

demo.launch()
