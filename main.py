from typing import List
from fastapi import FastAPI
from route_sensor import sensor

app = FastAPI()
app.include_router(sensor)