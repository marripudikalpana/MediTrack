from django.db import models

from patients.models import Patient

class EmergencyContact(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    contact_name = models.CharField(
        max_length=100
    )

    relationship = models.CharField(
        max_length=50
    )

    phone = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.contact_name