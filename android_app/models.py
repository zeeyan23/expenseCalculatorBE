from django.db import models

# Create your models here.

class all_records(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    credited_date = models.DateField()
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
