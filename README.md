# 🧠 Customer Churn Prediction (End-to-End ML Deployment)

This project demonstrates a full MLOps workflow for predicting customer churn using logistic regression, with a production-ready API deployed to Azure and a live Gradio UI.

---

## 🗂 Project Structure
```
churn-prediction-mlops-azure/
├── data/                   # Telco churn dataset
├── docker/                 # Dockerfile for FastAPI app
├── notebooks/              # EDA, preprocessing notebooks
├── src/
│   ├── train_model.py      # Train + save model
│   ├── inference/
│   │   ├── app.py          # FastAPI server
│   │   └── model.pkl       # Saved model
│   └── ui/
│       └── gradio_ui.py    # Gradio app for user input
├── requirements.txt
├── README.md
```

## What This Project Demonstrates

- ✅ Data preprocessing and encoding (LabelEncoder, NaNs, type casting)
- ✅ Logistic Regression model training and evaluation
- ✅ MLflow tracking (metrics, parameters, artifacts)
- ✅ Saving model to disk (`joblib`)
- ✅ Serving predictions via FastAPI
- ✅ Containerization with Docker
- ✅ Deployment to Azure Container Instances
- ✅ Live UI via Gradio connected to the Azure API

---

## 🧱 Architecture Overview (C4 Model)

### 1. System Context
![System Context](out/plantuml_diagrams/C4_system_context_diagram/System_Context.png)

### 2. Container Diagram
![Container Diagram](out/plantuml_diagrams/C4_container_diagram/Container_Diagram.png)

### 3. Deployment Diagram
![Deployment Diagram](out/plantuml_diagrams/C4_deployment_diagram/Deployment_Diagram.png)

### 4. Sequence Flow
![Sequence Diagram](out/plantuml_diagrams/C4_sequence_diagram/Sequence_Diagram.png)

---
## Live Demo
👉 API Docs: `http://churnapi21017.westeurope.azurecontainer.io/docs`  
👉 Gradio UI: `http://localhost:7860` *(or hosted Gradio link if deployed)*

---

## 🛠 Tech Stack
- Python 3.12
- scikit-learn, pandas, joblib
- FastAPI, Uvicorn
- Docker
- Azure CLI + Azure Container Instances
- Gradio (UI layer)

---

## How to Run
1. `python -m venv venv && source venv/bin/activate`  
2. `pip install -r requirements.txt`
3. `python src/train_model.py`
4. `uvicorn src.inference.app:app --reload`
5. `python src/ui/gradio_ui.py`

---

## Next Steps
- Add Streamlit dashboard (or deploy Gradio UI)
- Implement CI/CD via GitHub Actions
- Expand to multi-model registry with MLflow
- Add frontend for business reporting

---

## Author
**Kene Agbodike**  
_Data & AI | ML Engineering | MLOps | Cloud Deployment_
