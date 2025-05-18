from django.db import models

# Create your models here.

class DisasterReport(models.Model):
    disaster_type = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='disaster_images/')

    def __str__(self):
        return f"{self.disaster_type} - {self.location}"
