from django.db import models

# Create your models here.

class Client(models.Model) :
       userName = models.CharField(max_length=50)
       userEmail = models.EmailField(max_length=254)
       userPassword = models.CharField( max_length=12)

      

       


