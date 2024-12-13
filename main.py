from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello"}


@app.get("/sergio")
def sergio():
    return{"hello":"Sergio"}