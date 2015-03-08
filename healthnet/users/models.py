from django.db import models
from django.contrib.auth.models import User

# Create your models here.


##class User(models.Model):
##    #user = models.OneToOneField(User)
##    first_name = models.CharField(max_length=100)
##    last_name = models.CharField(max_length=100)
##    password = models.CharField(max_length=100)

class Patient(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.username
   
    
