from app import create_app, db
from app.models import User, Medication, StockEntry, Sale, SaleItem
from faker import Faker
import random
from datetime import datetime, timedelta

app = create_app()
fake = Faker()

def seed_users(n=20):
    db.session.query(User).delete()
    roles = ['admin', 'pharmacist']

    for _ in range(n):
        user = User(
            name=fake.name(),
            email=fake.unique.email(),
            password="hashed_password",  # Replace with hashed password logic if needed
            role=random.choice(roles)
        )
        db.session.add(user)
    db.session.commit()
    print(f"✅ Seeded {n} users")

def seed_medications(n=20):
    db.session.query(Medication).delete()

    for _ in range(n):
        med = Medication(
            name=fake.unique.company(),
            description=fake.text(max_nb_chars=100),
            brand=fake.company(),
            category=random.choice(['Antibiotic', 'Analgesic', 'Vitamin', 'Vaccine']),
            price=round(random.uniform(5, 100), 2),
            quantity_in_stock=random.randint(10, 200),
            expiry_date=datetime.utcnow() + timedelta(days=random.randint(30, 365))
        )
        db.session.add(med)
    db.session.commit()
    print(f"✅ Seeded {n} medications")

def seed_stock_entries(n=20):
    db.session.query(StockEntry).delete()

    users = User.query.all()
    meds = Medication.query.all()

    for _ in range(n):
        entry = StockEntry(
            medication_id=random.choice(meds).id,
            quantity=random.randint(10, 50),
            purchase_price=round(random.uniform(1, 50), 2),
            added_by=random.choice(users).id,
            created_at=fake.date_time_this_year()
        )
        db.session.add(entry)
    db.session.commit()
    print(f"✅ Seeded {n} stock entries")

def seed_sales(n=20):
    db.session.query(SaleItem).delete()
    db.session.query(Sale).delete()

    users = User.query.all()
    meds = Medication.query.all()

    for _ in range(n):
        sale = Sale(
            sold_by=random.choice(users).id,
            total_amount=0,  # we’ll update this after adding items
            created_at=fake.date_time_this_year()
        )
        db.session.add(sale)
        db.session.flush()  # get sale.id before commit

        total = 0
        for _ in range(random.randint(1, 5)):  # 1 to 5 items per sale
            med = random.choice(meds)
            qty = random.randint(1, 5)
            unit_price = float(med.price)
            total += qty * unit_price

            item = SaleItem(
                sale_id=sale.id,
                medication_id=med.id,
                quantity=qty,
                unit_price=unit_price
            )
            db.session.add(item)

        sale.total_amount = round(total, 2)
    db.session.commit()
    print(f"✅ Seeded {n} sales with items")

def seed_all():
    with app.app_context():
        seed_users(20)
        seed_medications(20)
        seed_stock_entries(20)
        seed_sales(20)

if __name__ == "__main__":
    seed_all()
