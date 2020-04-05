from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()



@app.get("/")
def root():
    return {"method": "GET"}

@app.post("/")
def root():
    return {"method": "POST"}

@app.put("/")
def root():
    return {"method": "PUT"}

@app.delete("/")
def root():
    return {"method": "DELETE"}
