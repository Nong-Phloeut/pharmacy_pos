from flask import Blueprint, request, jsonify
from app import db
from app.models import Sale, SaleItem, Medication

sale_bp = Blueprint('sale', __name__, url_prefix='/sales')

@sale_bp.route('/', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    result = []
    for sale in sales:
        items = [{
            "id": item.id,
            "medication_id": item.medication_id,
            "medication_name": item.medication.name if item.medication else None,
            "quantity": item.quantity,
            "unit_price": float(item.unit_price)
        } for item in sale.sale_items]

        result.append({
            "id": sale.id,
            "sold_by": sale.sold_by,
            "total_amount": float(sale.total_amount),
            "created_at": sale.created_at.isoformat() if sale.created_at else None,
            "items": items
        })
    return jsonify(result)

@sale_bp.route('/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
    sale = Sale.query.get(sale_id)
    if not sale:
        return jsonify({"error": "Sale not found"}), 404

    items = [{
        "id": item.id,
        "medication_id": item.medication_id,
        "medication_name": item.medication.name if item.medication else None,
        "quantity": item.quantity,
        "unit_price": float(item.unit_price)
    } for item in sale.sale_items]

    return jsonify({
        "id": sale.id,
        "sold_by": sale.sold_by,
        "total_amount": float(sale.total_amount),
        "created_at": sale.created_at.isoformat() if sale.created_at else None,
        "items": items
    })

@sale_bp.route('/', methods=['POST'])
def create_sale():
    data = request.get_json()
    if not data.get('sold_by') or not data.get('items'):
        return jsonify({"error": "Missing sold_by or items"}), 400

    sale = Sale(
        sold_by=data['sold_by'],
        total_amount=0  # will calculate below
    )
    db.session.add(sale)
    db.session.flush()  # to get sale.id before commit

    total = 0
    for item_data in data['items']:
        medication = Medication.query.get(item_data['medication_id'])
        if not medication:
            db.session.rollback()
            return jsonify({"error": f"Medication ID {item_data['medication_id']} not found"}), 400

        quantity = item_data.get('quantity', 1)
        unit_price = medication.price
        total += quantity * unit_price

        sale_item = SaleItem(
            sale_id=sale.id,
            medication_id=medication.id,
            quantity=quantity,
            unit_price=unit_price
        )
        db.session.add(sale_item)

    sale.total_amount = total
    db.session.commit()

    return jsonify({"message": "Sale created", "id": sale.id}), 201

@sale_bp.route('/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    sale = Sale.query.get(sale_id)
    if not sale:
        return jsonify({"error": "Sale not found"}), 404

    data = request.get_json()

    # Optionally update sold_by
    if 'sold_by' in data:
        sale.sold_by = data['sold_by']

    # If items are included, update sale items
    if 'items' in data:
        # Remove existing sale items
        for item in sale.sale_items:
            db.session.delete(item)
        db.session.flush()

        total = 0
        for item_data in data['items']:
            medication = Medication.query.get(item_data['medication_id'])
            if not medication:
                db.session.rollback()
                return jsonify({"error": f"Medication ID {item_data['medication_id']} not found"}), 400

            quantity = item_data.get('quantity', 1)
            unit_price = medication.price
            total += quantity * unit_price

            sale_item = SaleItem(
                sale_id=sale.id,
                medication_id=medication.id,
                quantity=quantity,
                unit_price=unit_price
            )
            db.session.add(sale_item)

        sale.total_amount = total

    db.session.commit()
    return jsonify({"message": "Sale updated"})

@sale_bp.route('/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    sale = Sale.query.get(sale_id)
    if not sale:
        return jsonify({"error": "Sale not found"}), 404

    # Delete related sale items first
    for item in sale.sale_items:
        db.session.delete(item)
    db.session.delete(sale)
    db.session.commit()
    return jsonify({"message": "Sale deleted"})
