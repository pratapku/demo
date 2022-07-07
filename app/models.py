from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class UserModel(models.Model):
    Please_Upload_Image = models.ImageField(upload_to='static/images/', blank=True)
    
    Name = models.CharField(max_length=100)
    Contect = models.IntegerField()
    Date_of_Birth = models.DateField(max_length=8)
    Email = models.EmailField(max_length = 254,unique=True)
    Positions = models.CharField(max_length=100)
    Ornizations = models.CharField(max_length=20000)

    def __str__(self):
        return self.Name