# 🧠 Customer Churn Prediction (End-to-End ML Deployment)

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.WebSite)

This project demonstrates a full MLOps workflow for predicting customer churn using logistic regression, with a production-ready API deployed to Azure and a live Gradio UI.

---

## 🤔 Why This Matters (For the Common Reader)

In business, keeping your current customers is often far more valuable than gaining new ones. But how do you know which customers are about to leave?

This project tackles that challenge by using machine learning to predict customer churn — i.e., which customers are likely to cancel their service. With this insight, businesses can act in advance: offering better deals, addressing complaints, or making personalized contact.

What makes this system special:
- 🤖 It's not just a model — it's fully deployed.
- ✨ You can interact with it through a clean API (for developers) or a simple interface (for business teams).
- ✈️ It's portable, production-grade, and can be deployed to the cloud in minutes.

Think of it as your own AI assistant for customer retention.

---

## 🗂 Project Structure
```
├── data/                       # Dataset
├── notebooks/                 # Data cleaning, EDA notebooks
├── src/
│   ├── inference/
│   │   ├── app.py             # FastAPI application
│   │   ├── model.pkl          # Trained model
│   │   └── pipeline.pkl       # Sklearn pipeline
│   ├── train_model.py         # Training script
│   └── __init__.py
├── ui/
│   └── gradio_ui.py           # Gradio application
├── docker/
│   └── Dockerfile             # Base Dockerfile
├── Docker-compose.yml         # Compose file for local multi-container setup
├── requirements.txt           # Project dependencies
```

## What This Project Demonstrates

- ✅ Data preprocessing and encoding (ColumnTransformer, NaNs, one-hot encoding)
- ✅ Logistic Regression model with pipeline encapsulation
- ✅ MLflow tracking (metrics, parameters, artifacts)
- ✅ Model saved and reused via `joblib`
- ✅ Serving predictions via FastAPI
- ✅ Live Gradio UI for manual testing
- ✅ Dockerized with one Dockerfile, multi-service Compose
- ✅ Deployed to Azure Web App for Containers / Azure Container Instances

---

## 🛠 Architecture Overview (C4 Model)

### 1. System Context
![System Context](out/plantuml_diagrams/C4_system_context_diagram/System_Context.png)

### 2. Container Diagram
![Container Diagram](out/plantuml_diagrams/C4_container_diagram/Container_Diagram.png)

### 3. Deployment Diagram
![Deployment Diagram](out/plantuml_diagrams/C4_deployment_diagram/Deployment_Diagram.png)

### 4. Sequence Flow
![Sequence Diagram](out/plantuml_diagrams/C4_sequence_diagram/Sequence_Diagram.png)

---
## 🚀 Live Demo
👉 API Docs: `http://churnapi21017.westeurope.azurecontainer.io/docs`  
👉 Gradio UI: `http://localhost:7860` *(or hosted Gradio link if deployed)*

---

## 🛠 Tech Stack
- Python 3.12
- scikit-learn, pandas, joblib
- FastAPI, Uvicorn
- Docker, Docker Compose
- Azure CLI + Azure Web App for Containers
- Gradio (UI layer)

---

## ✨ How to Run Locally (via Docker Compose)
```bash
git clone https://github.com/<your-username>/churn-prediction-mlops-azure.git
cd churn-prediction-mlops-azure

# Build and run both FastAPI + Gradio
docker compose up --build
```

- Visit `http://localhost:8000/docs` for API
- Visit `http://localhost:7860` for Gradio UI

---

## 🚤 Deploy to Azure

1. Step 1: Tag & Push Images to Azure Container Registry (ACR)
```bash
az acr login --name churnmlacr

# Tag your images correctly
# Replace with your actual local image names from `docker images`
docker tag churn-prediction-mlops-azure-churn-fastapi churnmlacr.azurecr.io/churn-fastapi:latest
docker tag churn-prediction-mlops-azure-churn-gradio churnmlacr.azurecr.io/churn-gradio:latest

# Push to ACR
docker push churnmlacr.azurecr.io/churn-fastapi:latest
docker push churnmlacr.azurecr.io/churn-gradio:latest
```

2. Step 2: Deploy to Azure Container Instances (ACI)
```bash
# Deploy FastAPI
az container create \
  --resource-group churnmlrg \
  --name churn-fastapi \
  --image churnmlacr.azurecr.io/churn-fastapi:latest \
  --registry-login-server churnmlacr.azurecr.io \
  --registry-username churnmlacr \
  --registry-password <your-password> \
  --cpu 1 --memory 1.5 \
  --dns-name-label churn-fastapi-kene \
  --ports 8000 --os-type Linux

# Deploy Gradio
az container create \
  --resource-group churnmlrg \
  --name churn-gradio \
  --image churnmlacr.azurecr.io/churn-gradio:latest \
  --registry-login-server churnmlacr.azurecr.io \
  --registry-username churnmlacr \
  --registry-password <your-password> \
  --cpu 1 --memory 1.5 \
  --dns-name-label churn-gradio-kene \
  --ports 7860 \
  --os-type Linux \
  --environment-variables ENV_MODE=cloud
```
🔁 When deploying Gradio, make sure the gradio_ui.py file uses the FastAPI container's full Azure FQDN in url = "FQDN:8000/predict"

### Final State
![Frontend Diagram](/frontend.png)

---

## Next Steps
- Implement CI/CD via GitHub Actions
- Auto-deploy to Azure on push
- Add model monitoring and metadata
- expand to Streamlit or frontend dashboard for BI teams

---

## Author
**Kene Agbodike**  
_Data & AI | ML Engineering | MLOps | Cloud Deployment_