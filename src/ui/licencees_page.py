from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget,QTableWidgetItem,QMessageBox
)
from services.data_save import DataSave
from ui.licencee_form import RegisterLicencee
from models.licencee import Licencee

class LicenceesPage(QWidget):
    def __init__(self, store:DataSave):
        super().__init__()
        self.store=store
        self.table=QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "Prison ID","Full Name","Risk","End date"])
        add_button=QPushButton("Licencee Adding")
        remove_button=QPushButton("Delete")
        button_setup=QHBoxLayout()
        button_setup.addWidget(add_button)
        button_setup.addWidget(remove_button)
        main_design= QVBoxLayout()
        main_design.addLayout(button_setup)
        main_design.addWidget(self.table)
        self.setLayout(main_design)
        add_button.clicked.connect(self.add_licencee)
        remove_button.clicked.connect(self.delete_licencee)
        self.update_table()
        self.table.resizeColumnsToContents()
    def update_table(self):
        self.table.setRowCount(len(self.store.licencees))

        for row,licencee in enumerate(self.store.licencees):
            self.table.setItem(row,0,QTableWidgetItem(str(licencee.id_prison)))
            self.table.setItem(row,1,QTableWidgetItem(str(licencee.full_name)))
            self.table.setItem(row,2,QTableWidgetItem(str(licencee.risk_type)))
            self.table.setItem(row,3,QTableWidgetItem(str(licencee.end_date)))

    def add_licencee(self):
        add_form = RegisterLicencee()
        result = add_form.exec()

        if result == RegisterLicencee.Accepted:
            prison_id,full_name,risk_type,end_date = add_form.get_values()

            new_licencee = Licencee(prison_id,full_name,risk_type,end_date)
            self.store.licencees.append(new_licencee)
            self.update_table()
            self.table.resizeColumnsToContents()

    def delete_licencee(self):
        row =self.table.currentRow()
        if row == -1:
            QMessageBox.warning(self,"Warning", "Select a row please")
            return
        del self.store.licencees[row]
        self.update_table()
        self.table.resizeColumnsToContents()










