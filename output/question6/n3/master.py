Here's a combined version of the function:

def cancel_appointment(appointment):
    appointment.patient.appointments.remove(appointment)
    appointment.doctor.appointments.remove(appointment)