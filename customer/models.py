from django.db import models
from django import forms

# Create your models here.
class Vendor(models.Model):
    #vendorID= models.IntegerField()
    businessName = models.CharField(max_length = 100)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    dateTimeCreated = models.DateTimeField(auto_now=True)
    

class Customer (models.Model):
    #CustomerID = models.IntegerField()
    firstName = models.CharField(max_length = 20 )
    lastName = models.CharField(max_length = 20 )
    email =  models.EmailField()
    phoneNumber = models.IntegerField()
    dateTimeCreated = models.DateTimeField(auto_now=True)
    amountOutstanding = models.FloatField()


class Auhtentication(models.Model):
    #Id = models.IntegerField()
    email = models.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput) 
    dateTimeCreated = models.DateTimeField(auto_now=True)


class MenuTable(models.Model):
    #menuID = models.IntegerField()
    name = models.CharField(max_length = 20)
    description =models.TextField(max_length = 20 )
    price = models.FloatField()
    quantity = models.IntegerField()
    dateTimeCreated = models.DateTimeField(auto_now=True )
    vendorID = models.IntegerField()
    isRecurring = models.BooleanField()
    freq_ofRecurrence = models.IntegerField()


class OrderTable(models.Model):
    CustomerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vendorID = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    description = models.TextField()
    itemsOrdered = models.TextField()
    amountDue = models.FloatField()
    amountOutstanding = models.FloatField()
    orderStatus = models.TextField()
    menuID = models.ForeignKey(MenuTable, on_delete=models.CASCADE)
    dateTimeCreated = models.DateTimeField(auto_now = True)
    

class OrderStatus(models.Model):
    orderStatus_ID = models.ForeignKey(OrderTable, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
class MessageStatus(models.Model):
    #messagesID = models.ForeignKey(Notification, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)

class Notification(models.Model):
    #Notification_ID = models.IntegerField()
    subjecteUser = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    orderID = models.ForeignKey(OrderTable, on_delete=models.CASCADE)
    message = models.TextField()
    dateTimeCreated = models.DateTimeField(auto_now=True)
    messageStatus = models.ForeignKey(MessageStatus, on_delete=models.CASCADE)



