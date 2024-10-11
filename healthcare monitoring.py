class Patient:
    def __init__(self,name,date_of_birth,p_id):
        self.name=name
        self.date_of_birth=date_of_birth
        self.p_id=p_id
        self.records=[]

    def record_details(self,record):
        self.records.append(record)

class Health_record:
    def __init__(self,date,temperature,pressure,symptoms,diagnosis=None):
        self.date=date
        self.temperature=temperature
        self.pressure=pressure
        self.symptoms=symptoms
        self.diagnosis=diagnosis

class Doctor:
    def __init__(self,d_name):
        self.d_name=d_name
        
    def diagnose(self,record):
        diagnosis="Potential General Physician issue based on symptoms"
        if "fever" in record.symptoms and record.temperature>=100:
            diagnosis="Fever is confirmed"
        if "Headache" in record.symptoms:
            diagnosis="Possible Headache,further treatment ahead"
        if "Stomach pain" in record.symptoms:   
            diagnosis="Possible diarrhea,further treatment ahead"
        return diagnosis

class Treatment:
    def __init__(self,medicine,dosage,duration):
        self.medicine=medicine
        self.dosage=dosage
        self.duration=duration


patient1 = Patient("Ramasamy", "1980-01-01", 1234)
record1 = Health_record("2024-06-30", 98.6, 110/70, "Headache")
patient1.record_details(record1)

doctor1 = Doctor("Dr. Smith")
diagnosis = doctor1.diagnose(record1)
print(f"Diagnosis: {diagnosis}")

treatment1 = Treatment("Aspirin", "200mg", "3 days")
print(f"Treatment: {treatment1.medicine} ({treatment1.dosage}) for {treatment1.duration}")

