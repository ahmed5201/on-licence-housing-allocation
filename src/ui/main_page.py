from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt
from services.data_save import DataSave
from ui.licencees_page import LicenceesPage

class Mainpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("On licence Housing Allocation System")
        self.resize(900,600)

        self.store=DataSave()
        self.licencees_page= LicenceesPage(self.store)
        self.setCentralWidget(self.licencees_page)

#Ahmed Ahmadi w23054487

