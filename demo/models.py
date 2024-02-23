from django.db import models

# Create your models here.
class sam(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    mobile_no=models.IntegerField()

