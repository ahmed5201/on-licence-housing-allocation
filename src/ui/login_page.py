from PySide6.QtWidgets import QDialog, QVBoxLayout,QLabel, QLineEdit, QPushButton, QMessageBox

class LoginPage(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(320,160)

        self.password_input=QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)

        login_button= QPushButton("Login")
        login_button.clicked.connect(self.login_attempt)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("On Licence Housing Allocation System"))
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)
        self.setLayout(layout)

    def login_attempt(self):
        correct_pass = "2468"

        if self.password_input.text() == correct_pass:
            self.accept()
        else:
            QMessageBox.warning(self, "Incorrect Password", "Try Again")
            self.password_input.clear()

