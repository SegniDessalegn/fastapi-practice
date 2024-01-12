
from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post("/")
def root(request: schemas.Blog):
    return {"message": request}
