from django.db import models

class Treatment(models.Model):

    disease_name = models.CharField(
        max_length=100
    )

    treatment_details = models.TextField()

    def __str__(self):
        return self.disease_name
