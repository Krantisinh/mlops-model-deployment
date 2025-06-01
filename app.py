from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model (assumes it's already trained and saved)
model = joblib.load("model.pkl")

class Features(BaseModel):
    features: list

@app.post("/predict")
def predict(data: Features):
    prediction = model.predict(np.array(data.features).reshape(1, -1))
    equation = "y = {:.4f} * x + {:.4f}".format(model.coef_[0], model.intercept_)
    return {"Equation": equation, "prediction": prediction[0]}
