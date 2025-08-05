# app/services/report_service.py
from reportlab.pdfgen import canvas
from app.services.inventory_service import get_expired_medications

def generate_expired_items_report():
    c = canvas.Canvas("reports/expired_items.pdf")
    meds = get_expired_medications()
    y = 800
    c.drawString(100, y, "Expired Medications Report")
    y -= 30
    for med in meds:
        c.drawString(100, y, f"{med.name} | Qty: {med.quantity} | Exp: {med.expiration_date}")
        y -= 20
    c.save()
