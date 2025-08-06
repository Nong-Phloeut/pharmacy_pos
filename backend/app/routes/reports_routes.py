# backend/app/routes/report_routes.py

from flask import Blueprint, jsonify, request
from app.models import Sale, Medication
from datetime import date, datetime

report_bp = Blueprint('report', __name__, url_prefix='/reports')


# 🔹 Daily Sales Report
@report_bp.route('/daily-sales', methods=['GET'])
def daily_sales():
    try:
        # Accept optional ?date=YYYY-MM-DD param
        query_date_str = request.args.get('date')
        if query_date_str:
            query_date = datetime.strptime(query_date_str, '%Y-%m-%d').date()
        else:
            query_date = date.today()

        # Filter sales by date only (ignore time)
        sales = Sale.query.filter(Sale.created_at >= query_date).all()

        # Summarize
        total_amount = sum(float(s.total_amount) for s in sales)

        # Return all sales as well if needed
        sale_details = [
            {
                "id": s.id,
                "sold_by": s.user.name if s.user else "Unknown",
                #   {
                #     "id": s.sold_by,
                #     "name": s.user.name if s.user else "Unknown"
                # },
                "total_amount": float(s.total_amount),
                "created_at": s.created_at.isoformat() if s.created_at else None
            } for s in sales
        ]

        return jsonify({
            "date": query_date.isoformat(),
            "total_sales": total_amount,
            "number_of_sales": len(sales),
            "sales": sale_details
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🔹 Expired Medications
@report_bp.route('/expired-items', methods=['GET'])
def expired_items():
    try:
        today = date.today()
        expired = Medication.query.filter(Medication.expiry_date < today).all()

        return jsonify([
            {
                "id": m.id,
                "name": m.name,
                "expiry_date": m.expiry_date.isoformat() if m.expiry_date else None,
                "quantity_in_stock": m.quantity_in_stock
            } for m in expired
        ])

    except Exception as e:
        return jsonify({"error": str(e)}), 500
