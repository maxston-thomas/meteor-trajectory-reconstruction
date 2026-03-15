from fastapi import FastAPI
from backend.coordinate_utils import radec_to_vector
from backend.data_loader import fetch_meteor_events
from backend.gmn_parser import load_gmn_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MeteorX backend running"}

@app.get("/vector")
def get_vector(ra: float, dec: float):
    vector = radec_to_vector(ra, dec)
    return {"vector": vector.tolist()}

@app.get("/events")
def get_events():

    df = load_gmn_data("Data/gmn_data.txt")

    events = []

    for _, row in df.head(20).iterrows():

        events.append({
            "id": row.iloc[0],
            "velocity_km_s": row.iloc[16],
            "start_lat": row.iloc[55],
            "start_lon": row.iloc[57],
            "end_lat": row.iloc[60],
            "end_lon": row.iloc[62]
        })

    return events

@app.get("/trajectory")
def get_trajectory():

    df = load_gmn_data("Data/gmn_data.txt")

    trajectories = []

    for _, row in df.head(10).iterrows():

        trajectories.append({
            "id": row.iloc[0],
            "start": {
                "lat": float(row.iloc[55]),
                "lon": float(row.iloc[57]),
                "height_km": float(row.iloc[59])
            },
            "end": {
                "lat": float(row.iloc[60]),
                "lon": float(row.iloc[62]),
                "height_km": float(row.iloc[64])
            }
        })

    return trajectories