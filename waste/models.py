from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class logins(models.Model):
#     username=models.CharField(max_length=100)
#     # email=models.EmailField(max_length=100)
#     password=models.CharField(max_length=100)

# class user(models.Model):
#     LOGIN=models.ForeignKey(logins, on_delete=models.CASCADE)
#     fullname=models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
  
class BioModel(models.Model):
    fullname=models.CharField(max_length=100)
    wasteweight=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
  
class NonBioModel(models.Model):
    fullname=models.CharField(max_length=100)
    wasteweight=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
   
   
   
class HazModel(models.Model):
    fullname=models.CharField(max_length=100)
    wasteweight=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
 


class HomeModel(models.Model):
    Name=models.CharField(max_length=100)
    
    Weight=models.IntegerField()
    location=models.CharField(max_length=100)
    options=(
        ("Bio-Degradable","Bio-Degradable"),
        ("Non_Degradable","Non_Degradable"),
        ("Hazardious-Waste","Hazardious-Waste")
    )
    waste_type=models.CharField(max_length=100,choices=options,default="Bio-Degradable") 
    ContactNumber=models.IntegerField()
    State=models.CharField(max_length=100)
    PinCode=models.IntegerField()


class Complaints(models.Model):
    # name=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    # message=models.ForeignKey(User,on_delete=models.CASCADE)
    
# class Meta:
#     unique_together('name','message')
# class logins(models.Model):
    # username=models.CharField(max_length=100)
    # password=models.CharField(max_length=100)
          
       

# class UserProfile(models.Model):
#     phone=models.IntegerField()
#     dob=models.CharField(max_length=100)

# class logins(models.Model):
#     username=models.CharField(max_length=100)
#     password=models.CharField(max_length=100)

# class user(models.Model):
#     LOGIN=models.ForeignKey(logins, on_delete=models.CASCADE)
#     fullname=models.CharField(max_length=100)
#     email=models.CharField(max_length=50)

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name