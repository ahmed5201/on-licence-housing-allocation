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
        self.filled_end_date.setPlaceholderText("09/10/2026")

        structure = QVBoxLayout()

        structure.addWidget(QLabel("Prison ID"))
        structure.addWidget(self.filled_id)
        structure.addWidget(QLabel("Full Name"))
        structure.addWidget(self.filled_name)

        structure.addWidget(QLabel("Risk"))
        structure.addWidget(self.filled_risk)
        structure.addWidget(QLabel("End Date"))
        structure.addWidget(self.filled_end_date)

        save_btn= QPushButton("SAVE")
        close_btn= QPushButton("CANCEL")

        save_btn.clicked.connect(self.save_clicked)
        close_btn.clicked.connect(self.reject)
        action_button_layout=QHBoxLayout()
        action_button_layout.addWidget(save_btn)
        action_button_layout.addWidget(close_btn)

        structure.addLayout(action_button_layout)
        self.setLayout(structure)

    def save_clicked(self):
        prison_id= self.filled_id.text().strip()
        full_name= self.filled_name.text().strip()
        end_date= self.filled_end_date.text().strip()
        self.accept()

        if prison_id == "" or full_name == "" or end_date =="":
            QMessageBox.warning(self,"Missing information","Please fill the slots")
            return
    def get_values(self):
        return (
            self.filled_id.text().strip(),
            self.filled_name.text().strip(),
            self.filled_risk.currentText(),
            self.filled_end_date.text().strip()

        )
        self.accept()

