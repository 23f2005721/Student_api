from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

CSV_FILE = Path(__file__).parent.parent / "q-fastapi.csv"
df = pd.read_csv(CSV_FILE)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/api")
def get_students(class_filter: list[str] | None = Query(None, alias="class")):
    data = df

    if class_filter:
        data = data[data["class"].isin(class_filter)]

    return {
        "students": data.to_dict(orient="records")
    }
