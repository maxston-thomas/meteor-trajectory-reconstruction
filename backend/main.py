from fastapi import FastAPI
from backend.coordinate_utils import radec_to_vector
from backend.data_loader import fetch_meteor_events

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MeteorX backend running"}

@app.get("/vector")
def get_vector(ra: float, dec: float):
    vector = radec_to_vector(ra, dec)
    return {"vector": vector.tolist()}

