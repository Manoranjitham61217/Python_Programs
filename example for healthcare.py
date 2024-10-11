class Patient:
  def __init__(self, name, dob, id):
    self.name = name
    self.dob = dob
    self.id = id
    self.records = []  # List to store HealthRecord objects

  def add_record(self, record):
    self.records.append(record)

class HealthRecord:
  def __init__(self, date, vitals, symptoms, diagnosis=None):
    self.date = date
    self.vitals = vitals  # Dictionary of vital signs (e.g., {"temperature": 37.5, "blood_pressure": 120/80})
    self.symptoms = symptoms  # List of symptoms reported
    self.diagnosis = diagnosis  # Set by doctor

class Doctor:
  def __init__(self, name, tasa):  # تخصص tasawwus means specialization in Arabic
    self.name = name
    self.tasawwus = tasawwus

  def diagnose(self, record):
    # This is a basic implementation, replace with logic for actual diagnosis
    diagnosis = "Potential " + self.tasawwus + " issue based on symptoms."
    if "fever" in record.symptoms and record.vitals["temperature"] > 100.4:
      diagnosis = "Possible fever. Further tests recommended."
    return diagnosis

class Treatment:
  def __init__(self, medication, dosage, duration):
    self.medication = medication
    self.dosage = dosage
    self.duration = duration


# Example Usage
patient1 = Patient("John Doe", "1980-01-01", 1234)
record1 = HealthRecord("2024-06-30", {"temperature": 98.6, "blood_pressure": 110/70}, ["headache", "fatigue"])
patient1.add_record(record1)

doctor1 = Doctor("Dr. Smith")
diagnosis = doctor1.diagnose(record1)
print(f"Diagnosis: {diagnosis}")

treatment1 = Treatment("Ibuprofen", "200mg", "3 days")
print(f"Treatment: {treatment1.medication} ({treatment1.dosage}) for {treatment1.duration}")
