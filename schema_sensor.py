from pydantic import BaseModel


class SensorSchema(BaseModel):
    time: str
    sensor_name: str
    sensor_value: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True