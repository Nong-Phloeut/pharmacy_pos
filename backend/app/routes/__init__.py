from app.routes.user_routes import user_bp
from app.routes.medication_routes import medication_bp
from app.routes.sale_routes import sale_bp
from app.routes.reports_routes import report_bp

def register_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(medication_bp)
    app.register_blueprint(sale_bp)
    app.register_blueprint(report_bp)
