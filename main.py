from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()



@app.get("/method")
def root():
    return {"method": "GET"}

@app.post("/method")
def root():
    return {"method": "POST"}

@app.put("/method")
def root():
    return {"method": "PUT"}

@app.delete("/method")
def root():
    return {"method": "DELETE"}
