from msLogger import logger
from fastapi import FastAPI

app = FastAPI()

@app.get("/byLocation/getCount/{location}")
def get_count_by_location(location: str):
    return {"itemCount": 3}