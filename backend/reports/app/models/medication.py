# app/models/medication.py
from sqlalchemy import Column, Integer, String, Float, Date
from app.db import Base

class Medication(Base):
    __tablename__ = 'medications'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    quantity = Column(Integer)
    price = Column(Float)
    expiration_date = Column(Date)
