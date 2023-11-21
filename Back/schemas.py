#DB 테이블 속성
	# 테이블
	# Api (추후 변경 가능)
	
	# 시퀀스 값, 센서 이름, 센서값, 측정시간
	# sequence, sensorName, sensorValue, dateTime
	
	# 참고 코드
	# https://cotak.tistory.com/25
	# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-model-attributescolumns

from sqlalchemy import Column, Integer, Float, String, TIMESTAMP

from .database import Base

class Api(Base):
    __tablename__ = "api"

    sequence = Column(Integer, primary_key = True)
    sensorName=Column(String)
    sensorValue = Column(Float)
    dateTime = Column(TIMESTAMP)
