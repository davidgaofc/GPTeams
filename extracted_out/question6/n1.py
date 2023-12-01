import datetime

class Patient:
    def __init__(self, name, age, medical_record):
        self.name = name
        self.age = age
        self.medical_record = medical_record
        self.appointments = []

    def schedule_appointment(self, date, doctor):
        appointment = Appointment(self, doctor, date)
        self.appointments.append(appointment)
        doctor.appointments.append(appointment)

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.appointments = []

    def get_upcoming_appointments(self):
        return [appt for appt in self.appointments if appt.date >= datetime.datetime.now()]

class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def reschedule(self, new_date):
        self.date = new_date

def create_patient(name, age, medical_record):
    return Patient(name, age, medical_record)

def create_doctor(name, specialty):
    return Doctor(name, specialty)

def schedule_appointment(patient, doctor, date):
    patient.schedule_appointment(date, doctor)

def reschedule_appointment(appointment, new_date):
    appointment.reschedule(new_date)

def get_doctor_appointments(doctor):
    return doctor.get_upcoming_appointments()

def update_medical_record(patient, new_record):
    patient.medical_record = new_record

def list_patient_appointments(patient):
    return [(appt.date, appt.doctor.name) for appt in patient.appointments]

# TODO: Implement the 'cancel_appointment' function
def cancel_appointment(appointment):
    # This function should take an Appointment object as input and remove it from both the patient's and doctor's appointment lists.
    # Expected Input: appointment (Appointment object)
    # Expected Output: None, but the appointment should be removed from the respective lists.
    patient = appointment.patient
    doctor = appointment.doctor

    patient.appointments.remove(appointment)
    doctor.appointments.remove(appointment)
