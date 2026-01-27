from PySide6.QtWidgets import QApplication, QLabel
from PySide.QtCore import Qt
import sys

def main():
    app= QApplication(sys.argv)
    welcome_text=QLabel("Welcome to the On licence Housing Allocations System")
    welcome_text.setWindowTitle("On licence Housing Allocations System")
    welcome_text.resize(400,200)
    welcome_text.setAlignment(Qt.AlignCenter)
    welcome_text.show()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()