from flask import Blueprint, jsonify, request
from app.services.inventory_service import add_medication

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/api/medications", methods=["POST"])
def create_medication():
    data = request.get_json()
    add_medication(data)
    return jsonify({"message": "Medication added successfully"}), 201
