from django.db import models

# Create your models here.
from django.db import models

class SafetyTip(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
