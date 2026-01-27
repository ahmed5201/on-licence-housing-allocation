from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt

class Mainpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("On licence Housing Allocation System")
        self.resize(900,600)

        label= QLabel("Main Page --- Log in ( Done )")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
