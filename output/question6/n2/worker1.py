```python
  def cancel_appointment(appointment):
      # Remove the appointment from the patient's appointment list
      appointment.patient.appointments.remove(appointment)
      
      # Remove the appointment from the doctor's appointment list
      appointment.doctor.appointments.remove(appointment)
```