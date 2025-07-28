from django.db import models

# Create your models here.


class DoctorProfile(models.Model):
    name = models.CharField(max_length=200) 
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    specialization = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=20) 
    password = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=10,default='inactive')

    def __str__(self):
        return self.name

class PatientProfile(models.Model):
    name = models.CharField(max_length=200) 
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200,null=True)