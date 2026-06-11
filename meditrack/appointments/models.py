from django.db import models

from doctors.models import Doctor

from patients.models import Patient


class Appointment(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    status = models.CharField(
        max_length=50,
        default='Pending'
    )
