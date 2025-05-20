from fastapi import FastAPI
from db import files_col

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DQ API is up!"} 

@app.get("/files")
def get_files():
    return list(files_col.find({}, {"_id": 0}))
