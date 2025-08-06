from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import all blueprints
    from app.routes.user_routes import user_bp
    from app.routes.medication_routes import medication_bp
    from app.routes.sale_routes import sale_bp
    from app.routes.reports_routes import report_bp

    # Register all blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(medication_bp)
    app.register_blueprint(sale_bp)
    app.register_blueprint(report_bp)

    return app
