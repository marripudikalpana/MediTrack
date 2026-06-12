from django.db import models
class Hospital(models.Model):

    name = models.CharField(max_length=100)

    address = models.TextField()

    city = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=6
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=6
    )

    def __str__(self):
        return self.name
# Create your models here.
