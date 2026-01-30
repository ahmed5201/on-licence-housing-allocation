from models.licencee import Licencee
class DataSave:
    def __init__(self):
        self.licencees=[]
        self.data_sample()

    def data_sample(self):
        self.licencees.append(Licencee("1212", "Wujood Khalid","Low","09/10/2026"))
        self.licencees.append(Licencee("1313", "Mike Owens","High","12/12/2026"))
        self.licencees.append(Licencee("1111","David Stan","Medium","03/03/2026"))

#Ahmed Ahmadi w23054487
