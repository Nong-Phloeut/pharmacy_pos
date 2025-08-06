from flask import Blueprint, request, jsonify
from app import db
from app.models import Medication

medication_bp = Blueprint('medication', __name__, url_prefix='/medications')

@medication_bp.route('/', methods=['GET'])
def get_medications():
    meds = Medication.query.all()
    return jsonify([
        {
            "id": m.id,
            "name": m.name,
            "description": m.description,
            "brand": m.brand,
            "category": m.category,
            "price": float(m.price),
            "quantity_in_stock": m.quantity_in_stock,
            "expiry_date": m.expiry_date.isoformat() if m.expiry_date else None
        }
        for m in meds
    ])

@medication_bp.route('/<int:med_id>', methods=['GET'])
def get_medication(med_id):
    med = Medication.query.get(med_id)
    if not med:
        return jsonify({"error": "Medication not found"}), 404
    return jsonify({
        "id": med.id,
        "name": med.name,
        "description": med.description,
        "brand": med.brand,
        "category": med.category,
        "price": float(med.price),
        "quantity_in_stock": med.quantity_in_stock,
        "expiry_date": med.expiry_date.isoformat() if med.expiry_date else None
    })

@medication_bp.route('/', methods=['POST'])
def create_medication():
    data = request.get_json()
    required_fields = ['name', 'price', 'quantity_in_stock']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    med = Medication(
        name=data['name'],
        description=data.get('description'),
        brand=data.get('brand'),
        category=data.get('category'),
        price=data['price'],
        quantity_in_stock=data['quantity_in_stock'],
        expiry_date=data.get('expiry_date')  # Should be ISO format string or None
    )
    db.session.add(med)
    db.session.commit()
    return jsonify({"message": "Medication created", "id": med.id}), 201

@medication_bp.route('/<int:med_id>', methods=['PUT'])
def update_medication(med_id):
    med = Medication.query.get(med_id)
    if not med:
        return jsonify({"error": "Medication not found"}), 404

    data = request.get_json()
    med.name = data.get('name', med.name)
    med.description = data.get('description', med.description)
    med.brand = data.get('brand', med.brand)
    med.category = data.get('category', med.category)
    med.price = data.get('price', med.price)
    med.quantity_in_stock = data.get('quantity_in_stock', med.quantity_in_stock)
    med.expiry_date = data.get('expiry_date', med.expiry_date)

    db.session.commit()
    return jsonify({"message": "Medication updated"})

@medication_bp.route('/<int:med_id>', methods=['DELETE'])
def delete_medication(med_id):
    med = Medication.query.get(med_id)
    if not med:
        return jsonify({"error": "Medication not found"}), 404

    db.session.delete(med)
    db.session.commit()
    return jsonify({"message": "Medication deleted"})
