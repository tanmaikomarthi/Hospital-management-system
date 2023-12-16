from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    Specialization = models.CharField(max_length=50)
    Qualification = models.CharField(max_length=50)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    def __str__(self):
        return self.Name

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    symptoms = models.TextField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    doctor=models.ForeignKey('Doctor',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

