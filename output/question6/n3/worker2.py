```python
def cancel_appointment(appointment):
    patient = appointment.patient
    doctor = appointment.doctor
    patient.appointments.remove(appointment)
    doctor.appointments.remove(appointment)
```