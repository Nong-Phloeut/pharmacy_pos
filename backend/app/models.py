from app import db
from datetime import datetime

# 🔹 User model (Admin / Pharmacist)
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin' or 'pharmacist'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.name} - {self.role}>"


# 💊 Medication model
class Medication(db.Model):
    __tablename__ = 'medications'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    brand = db.Column(db.String(100))
    category = db.Column(db.String(50))
    price = db.Column(db.Numeric(10, 2), nullable=False)
    quantity_in_stock = db.Column(db.Integer, default=0)
    expiry_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Medication {self.name}>"


# 📦 Stock entry when adding inventory
class StockEntry(db.Model):
    __tablename__ = 'stock_entries'

    id = db.Column(db.Integer, primary_key=True)
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    purchase_price = db.Column(db.Numeric(10, 2))
    added_by = db.Column(db.Integer, db.ForeignKey('users.id'))  # optional
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    medication = db.relationship('Medication', backref='stock_entries')
    user = db.relationship('User', backref='stock_added')

    def __repr__(self):
        return f"<StockEntry for med_id {self.medication_id}>"


# 🧾 Sale transaction
class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    sold_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='sales')

    def __repr__(self):
        return f"<Sale {self.id} - Amount {self.total_amount}>"


# 🧾 Sale items in a transaction
class SaleItem(db.Model):
    __tablename__ = 'sale_items'

    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)

    sale = db.relationship('Sale', backref='items')
    medication = db.relationship('Medication')

    def __repr__(self):
        return f"<SaleItem {self.medication_id} x {self.quantity}>"
