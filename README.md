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

---

## 🔄 End-to-End Architecture
```mermaid
graph TD
    A[Raw Data: Telco-Customer-Churn.csv] --> B[train_model.py: Preprocess & Train Model]
    B --> C[model.pkl Saved to src/inference/]
    C --> D[app.py: FastAPI Web Server]
    D --> E[Azure Container Instance: Dockerized FastAPI API]
    E --> F[Public Prediction Endpoint]

    G[Gradio UI (gradio_ui.py)] -->|Sends input| F
    F -->|Receives prediction| G
```

---

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
