# app/db.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("mysql+mysqlconnector://user:password@localhost/pharmacy_pos")
SessionLocal = sessionmaker(bind=engine)
