from django.db import models

# Create your models here.

class DataEntry(models.Model):
    data = models.CharField(max_length=255)

    def __str__(self):
        return self.data