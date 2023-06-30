from sqlalchemy import Column, String
from database import Base

class SensorModel(Base):
    __tablename__ = "sensors"

    time = Column(String, primary_key=True, autoincrement=False)
    sensor_name = Column(String)
    sensor_value = Column(String)

    created_at = Column(String)
    updated_at = Column(String)