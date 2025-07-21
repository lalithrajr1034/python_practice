"""Hospital and Doctor

Create a Doctor class (name, specialization).
Create a Hospital class that stores multiple Doctor objects using aggregation.
Print the hospital name and list of doctors."""

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        
class Hospital:
    def __init__(self, hos_name, doctor_info):
        self.hos_name = hos_name
        self.doctor_info = doctor_info

doct1 = Doctor("lalithraj", "mbbs-heart")
doct2 = Doctor("teja", "mbbs-brain")
doct3 = Doctor("nithin", "mbbs-kidny")
doct4 = Doctor("seena", "mbbs-apendix")

doct = [doct1, doct2, doct3, doct4]

hosp = Hospital("mit-mental_hospital", doct)                

for i in doct:
    print(f"Hospital name:  { hosp.hos_name} Doct name: {i.name}, specialization: {i.specialization}")