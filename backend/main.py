from fastapi import FastAPI
from backend.coordinate_utils import radec_to_vector
from backend.gmn_parser import load_gmn_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "MeteorX backend running"}


@app.get("/vector")
def get_vector(ra: float, dec: float):

    vector = radec_to_vector(ra, dec)

    return {
        "vector": vector.tolist()
    }


@app.get("/events")
def get_events():

    df = load_gmn_data("Data/gmn_data.txt")

    events = []

    for _, row in df.head(100).iterrows():

        events.append({
            "id": str(row.iloc[0]) if len(row) > 0 else "unknown",

            "velocity": float(row.iloc[16]) if len(row) > 16 else 0,

            "start_lat": float(row.iloc[55]) if len(row) > 55 else 0,
            "start_lon": float(row.iloc[57]) if len(row) > 57 else 0,

            "end_lat": float(row.iloc[60]) if len(row) > 60 else 0,
            "end_lon": float(row.iloc[62]) if len(row) > 62 else 0
        })

    return events


@app.get("/trajectory")
def get_trajectory():

    df = load_gmn_data("Data/gmn_data.txt")

    trajectories = []

    for _, row in df.head(100).iterrows():

        trajectories.append({

            "id": str(row.iloc[0]) if len(row) > 0 else "unknown",

            "start": {
                "lat": float(row.iloc[55]) if len(row) > 55 else 0,
                "lon": float(row.iloc[57]) if len(row) > 57 else 0,
                "height_km": float(row.iloc[59]) if len(row) > 59 else 0
            },

            "end": {
                "lat": float(row.iloc[60]) if len(row) > 60 else 0,
                "lon": float(row.iloc[62]) if len(row) > 62 else 0,
                "height_km": float(row.iloc[64]) if len(row) > 64 else 0
            }

        })

    return trajectories