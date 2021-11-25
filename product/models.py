from django.db import models
from login.models import signup

# Create your models here.

class categories(models.Model):
    cname=models.CharField(max_length=10)
    def __str__(self):
        return self.cname


class product(models.Model):
    cname = models.ForeignKey(categories, on_delete=models.CASCADE,default='')
    name=models.CharField(max_length=10)
    price=models.PositiveIntegerField()
    des=models.TextField()
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.name

