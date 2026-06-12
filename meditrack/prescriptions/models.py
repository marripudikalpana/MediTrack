from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment


class Prescription(models.Model):

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    diagnosis = models.TextField()

    instructions = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.patient)
# Create your models here.
