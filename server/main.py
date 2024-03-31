from typing import Union
from fastapi import FastAPI

from router import notes

app = FastAPI()

app.include_router(notes.router, prefix="/notes", tags=["notes"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
