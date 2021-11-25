from django.db import models

# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    email=models.EmailField()
    phn=models.PositiveIntegerField()
    Male = 'M'
    Female = 'F'
    Gender = [
        (Male, 'MAle choice'),
        (Female, 'Female choice'),]
    Gender = models.CharField(max_length=2,choices=Gender)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.username
