from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from pydantic import BaseModel
import pandas as pd
from binascii import a2b_base64
import uuid
from DAML import DAML

class FileQuery(BaseModel):
    task: str
    dataset_file: str

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
    query: FileQuery):

    try:
        print("TASK:", query.task)
        print("DATASET FILE:", query.dataset_file)
    except Exception as e:
        print(e)
        return {"error": "Invalid task or dataset file"}

    try:
        padding_len = len(query.dataset_file) % 4
        query.dataset_file += "=" * (4 - padding_len) if padding_len != 0 else ""
        binary_data = a2b_base64(query.dataset_file)

        temp_file_name = "./temp/" + str(uuid.uuid4()) + '.csv'
        fd = open(temp_file_name, 'wb')
        fd.write(binary_data)
        fd.close()
        df = pd.read_csv(temp_file_name)
        print("GOT DATASET")
        daml = DAML(df, query.task)
        return {"type": daml.selected_model, "accuracy": daml.models[0][1], "url": daml.selected_model_url}
    except Exception as e:
        print(e)
        return {"error": "Invalid dataset file"}