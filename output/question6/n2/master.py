def cancel_appointment(appointment):
    patient = appointment.patient
    doctor = appointment.doctor
    
    patient.appointments.remove(appointment)
    doctor.appointments.remove(appointment)
    
    # Remove the appointment from the patient's appointment list
    appointment.patient.appointments.remove(appointment)
      
    # Remove the appointment from the doctor's appointment list
    appointment.doctor.appointments.remove(appointment)