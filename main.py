
# main.py
from PyQt5.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.db import Base, engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
