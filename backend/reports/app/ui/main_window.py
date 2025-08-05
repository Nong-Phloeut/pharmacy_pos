# app/ui/main_window.py
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from app.services.report_service import generate_expired_items_report

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pharmacy POS System")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.report_btn = QPushButton("Generate Expired Report")
        self.report_btn.clicked.connect(self.handle_generate_report)
        layout.addWidget(self.report_btn)
        self.setLayout(layout)

    def handle_generate_report(self):
        generate_expired_items_report()
