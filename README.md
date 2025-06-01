# MLOps Model Deployment Template

This project is a quick-start template for deploying machine learning models using FastAPI, Docker, MLflow, and GitHub Actions. Ideal for software architects and ML engineers looking to get hands-on with model deployment.

---

## Project Structure

```
.
├── app.py                      # FastAPI app to serve model
├── Dockerfile                 # Docker container setup
├── requirements.txt           # Python dependencies
├── train_and_log_model.py     # Script to train model and log with MLflow
└── .github/workflows/train.yml  # GitHub Actions workflow
```

---

## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd mlops_model_deployment_template
```

### 2. Create a virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Train and log your model with MLflow
```bash
python train_and_log_model.py
```
- This trains a simple regression model.
- Logs model, score, and parameters in MLflow.
- Generates `model.pkl` used by FastAPI.

### 4. Serve your model using FastAPI
```bash
uvicorn app:app --reload
```
Try making a POST request:
```bash
curl -X POST http://127.0.0.1:8000/predict \
     -H "Content-Type: application/json" \
     -d "{\"features\": [3.5]}"
```

---

## 🐳 Dockerize the App

```bash
docker build -t ml-model-api .
docker run -p 8000:8000 ml-model-api
```

---

## 🔁 CI/CD with GitHub Actions

A GitHub Actions workflow is provided to:
- Set up Python
- Install dependencies
- Train and log model on code push

File: `.github/workflows/train.yml`

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

---

## ✅ Next Steps

- Add unit tests for the API.
- Deploy to cloud (AWS, GCP, etc.)
- Use a model registry for version control (e.g., MLflow Registry)
- Add authentication and logging to your API
---

## How it works?

Let's break down what prediction we're getting from:

```json
{ "features": [5] }
```

### 📌 Based on the Template:

In `train_and_log_model.py`, we're training a **simple linear regression model** using `scikit-learn` on **synthetic data**:

```python
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)
```
The `random_state` param will ensure reproducible predictions.

This generates:

* 100 synthetic data points
* 1 input feature
* A linear relationship with some noise

Then the model is trained and saved to `model.pkl`, which our FastAPI app loads to make predictions.

---

### So when we call:

```bash
 curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"features\": [5]}"
```

The model predicts the output `y` for an input `X = 5` based on the linear equation it learned (something like $y = w \cdot x + b$).

---

### 🧪 Example Output:

If the model learned something like:
$$
y = 41.7702 \cdot x + 0.0201
$$

Then the prediction for $x = 5$ would be:

$$
y = 41.7702 \cdot 5 + 0.0201 = 208.87131485597536
$$

But again — the **actual number** depends on the data generated and the model trained.

---