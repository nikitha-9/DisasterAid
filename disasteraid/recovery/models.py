from django.db import models

# Create your models here.

class AidResource(models.Model):
    resource_type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.resource_type} - {'Available' if self.availability else 'Not Available'}"

