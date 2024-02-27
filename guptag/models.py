from django.db import models

# Create your models here.
class apple(models.Model):
    name = models.CharField(max_length=90)
    amount = models.CharField(max_length=90)
    payment_id = models.CharField(max_length=90)
    paid = models.BooleanField(default=False)
