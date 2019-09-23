from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class BankInfo(models.Model):
    year = models.IntegerField()
    use_rate = models.FloatField()
    phone_rate = models.FloatField(null=True, blank=True)
    pc_rate = models.FloatField(null=True, blank=True)
    notebook_rate = models.FloatField(null=True, blank=True)
    etc_rate = models.FloatField(null=True, blank=True)
    pad_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.year)