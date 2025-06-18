from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Load model (adjust path if needed)
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(os.path.dirname(__file__), "..", "model", "urgency_model.pkl")  # if in app/model
model_path = os.path.normpath(model_path)  # Normalize the path

print("MODEL PATH:", model_path)  # Optional for debugging

model = joblib.load(model_path)


app = FastAPI(title="MediTriage Urgency API", version="1.0")

class SymptomInput(BaseModel):
    symptoms: list[int]  # List of 1s and 0s indicating symptoms present

@app.get("/")
def read_root():
    return {"message": "Welcome to MediTriage Urgency Predictor API!"}

@app.post("/predict-urgency")
def predict_urgency(input: SymptomInput):
    try:
        prediction = model.predict([input.symptoms])[0]
        labels = {0: "Routine", 1: "Urgent", 2: "Emergency"}
        return {"predicted_urgency": labels.get(prediction, "Unknown")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))