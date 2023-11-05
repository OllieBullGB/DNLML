from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from pydantic import BaseModel
import pandas as pd
from DAML import DAML

app = FastAPI()
# allow the /models folder to be served as a static directory
app.mount("/models", StaticFiles(directory="models"), name="models")

# allow CORS
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def read_root():
    return {"Hello, welcome to the DNLML API!"}

@app.get("/link")
def processLink(
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

@app.get("/file")
def processFile(
    task,
    dataset_file: UploadFile = File(...)):

    try:
        print("TASK:", task)
        print("DATASET FILE:", dataset_file)
    except Exception as e:
        print(e)
        return {"error": "Invalid task or dataset file"}

    try:
        contents = dataset_file.file.read()
        buffer = BytesIO(contents)
        df = pd.read_csv(dataset_file)
        buffer.close()
        dataset_file.file.close()
        print("GOT DATASET")
        daml = DAML(df, task)
        return {"type": daml.selected_model, "accuracy": daml.models[0][1], "url": daml.selected_model_url}
    except Exception as e:
        print(e)
        return {"error": "Invalid dataset file"}