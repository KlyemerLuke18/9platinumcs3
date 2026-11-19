#Klyemer Luke S. Colico
#9-Platinum

class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount
    def calculate_bill(self):
        return self.bill_amount
    def display_patient_type(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.80
    def display_patient_type(self):
        print("Patient Type: Senior Citizen")
    
class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.85 
    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")

print("Hospital Billing System")
print("-----------------------")
patients = [
    Patient("Juan Dela Cruz", 15000.00),
    SeniorPatient("Maria Santos", 15000.00),
    PhilhealthPatient("Pedro Reyes", 15000.00)
]

for patient in patients:
    print(f"Patient Name:  {patient.name}")
    patient.display_patient_type()
    print(f"Original Bill: ₱{patient.bill_amount:,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")