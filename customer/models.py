from django.db import models

# Create your models here.
class Vendor(models.model):
    businessName = models.charField(max_length 100)
    email = models.emailField()
    phoneNumber = models.integerField()
    dateTimeCreated = models.dateField()

class Customer (models.model):
    firstName = models.charField(max_length 20 )
    lastName = models.charField(max_length = 20 )
    email =  models.emailField()
    phoneNumber = models.integerField()
    dateTimeCreated = models.dateTimeCreated()
    amountOutstanding = models.floatField()

class Auhtentication(models.model):
    email = models.emailField()
    password = models.
    dateTimeCreated = 

class MenuTable(models.model):
    name = 
    description =
    price = 
    quantity =
    dateTimeCreated = 
    vendorID =

class OrderTable(models.model):
    