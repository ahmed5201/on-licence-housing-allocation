from PySide6.QtWidgets import(
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton,QMessageBox,QComboBox,QTextEdit
)


class RegisterLicencee(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register Licencee")
        self.resize(360,380)

        self.filled_id = QLineEdit()
        self.filled_id.setPlaceholderText("1212")

        self.filled_name =  QLineEdit()
        self.filled_name.setPlaceholderText("Name Fully Written")

        self.filled_risk = QComboBox()
        self.filled_risk.addItems(["High","Medium","Low"])

        self.filled_end_date = QLineEdit()
        self.filled.end_date.setPlaceholderText("09/10/2026")

        structure = QVBoxLayout()
        structure.addWidget