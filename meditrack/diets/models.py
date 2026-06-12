from django.db import models

class DietPlan(models.Model):

    disease_name = models.CharField(
        max_length=100
    )

    diet_details = models.TextField()

    def __str__(self):
        return self.disease_name