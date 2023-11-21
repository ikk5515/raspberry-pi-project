import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# mysql 유저정보
MYSQL_USER = "root"
MYSQL_PASSWORD = "#"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB = "sensor"

DATABASE_URL = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_HOST,
    MYSQL_DB
)

engine = create_engine(
    DATABASE_URL, echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = session.query_property()