# app/services/inventory_service.py
from app.db import SessionLocal
from app.models.medication import Medication
from datetime import datetime

def add_medication(data):
    session = SessionLocal()
    med = Medication(**data)
    session.add(med)
    session.commit()
    session.close()

def get_expired_medications():
    session = SessionLocal()
    today = datetime.now().date()
    meds = session.query(Medication).filter(Medication.expiration_date < today).all()
    session.close()
    return meds
