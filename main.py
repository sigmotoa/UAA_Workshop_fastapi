from fastapi import FastAPI,Path


app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello"}


@app.get("/sergio")
def sergio():
    return{"hello":"Sergio"}


@app.get("/hello/{name}")
def name(name:str =Path(...)):
    return {"Hello":name}