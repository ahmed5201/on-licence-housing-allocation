from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt
import sys
from ui.login_page import LoginPage

def main():
    app= QApplication(sys.argv)
    login = LoginPage()
    login.exec()
    sys.exit(0)
    welcome_text=QLabel("Welcome to the On licence Housing Allocations System")
    welcome_text.setWindowTitle("On licence Housing Allocations System")
    welcome_text.resize(400,200)
    welcome_text.setAlignment(Qt.AlignCenter)
    welcome_text.show()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()