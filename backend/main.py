from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
from DAML import DAML

app = FastAPI()
# allow the /models folder to be served as a static directory
app.mount("/models", StaticFiles(directory="models"), name="models")

@app.get("/")
def read_root():
    return {"Hello, welcome to the DNLML API!"}

@app.get("/link")
def process(
    task,
    dataset_url):

    try:
        print("TASK:", task)
        print("DATASET URL:", dataset_url)
    except Exception as e:
        print(e)
        return {"error": "Invalid task or dataset URL"}

    try:
        df = pd.read_csv(dataset_url)
        print("GOT DATASET")
        daml = DAML(df, task)
        return {"type": daml.selected_model, "accuracy": daml.models[0][1], "url": daml.selected_model_url}
    except Exception as e:
        print(e)
        return {"error": "Invalid dataset URL"}
