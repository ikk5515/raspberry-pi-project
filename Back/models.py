from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, DateTime
from pydantic import BaseModel
from database import Base
from database import engine


class SensorTable(Base):
    __tablename__ = "sensor"

    seq = Column(Integer, primary_key=True, autoincrement=True)
    sensor_name = Column(String(50), nullable=False)
    measure_value = Column(Float, nullable=False)
    measure_time = Column(DateTime)

class Sensor(BaseModel):
    seq: int
    sensor_name : str
    measure_value : float
    measure_time : datetime
