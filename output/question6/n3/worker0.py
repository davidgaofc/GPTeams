```python
def cancel_appointment(appointment):
    appointment.patient.appointments.remove(appointment)
    appointment.doctor.appointments.remove(appointment)
```