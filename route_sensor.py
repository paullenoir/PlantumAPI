from fastapi import APIRouter, Depends
from database import get_db
from model_sensor import SensorModel
from schema_sensor import SensorSchema
from sqlalchemy.orm import Session
from datetime import datetime


# Base.metadata.create_all(bind=engine)
sensor = APIRouter()

@sensor.get("/")
def get_Massage():
    return {"message":"message test"}

@sensor.get("/sensors",response_model=list[SensorSchema])
def get_all_sensors(db: Session=Depends(get_db)):
    return db.query(SensorModel).all()