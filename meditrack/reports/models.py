

from django.db import models
from patients.models import Patient

class MedicalReport(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    report_file = models.FileField(
        upload_to='reports/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Report {self.id}"
