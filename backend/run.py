from app import create_app, db
from app.models import User

app = create_app()

# For first run: create tables
with app.app_context():
    # db.drop_all()
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
