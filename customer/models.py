from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import moneyed
#from djmoney.models.fields import models.DecimalField
from datetime import datetime
from django.db import models

# Create your models here.
class Vendor(models.Model):
    businessName = models.CharField(max_length = 100)
    email = models.EmailField()
    phoneNumber = PhoneNumberField()
    dateTimeCreated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (self.businessName,self.email,self.phoneNumber)

class Customer(models.Model):
    firstName = models.CharField(max_length = 20 )
    lastName = models.CharField(max_length = 20 )
    email =  models.EmailField()
    phoneNumber = PhoneNumberField()
    dateTimeCreated = models.DateTimeField(auto_now=True)
    amountOutstanding = models.DecimalField(max_digits=10, decimal_places=2)
    #amountOutstanding = models.DecimalField(max_digits=10, decimal_places=2, default_currency='NGN')

    def __str__(self):
        return (self.firstName, self.lastName, self.email,self.phoneNumber)


# class Auhtentication(models.Model):
#     #Id = models.IntegerField()
#     email = models.EmailField()
#     password = forms.CharField(max_length=32, widget=forms.PasswordInput) 
#     dateTimeCreated = models.DateTimeField(auto_now=True)


class MenuItem(models.Model):
    name = models.CharField(max_length = 60)
    description =models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    dateTimeCreated = models.DateTimeField(auto_now=True )
    vendorID = models.ForeignKey(Vendor, on_delete= models.CASCADE)
    isRecurring = models.BooleanField()
    freqOfRecurrence = models.IntegerField()

    def __str__(self):
        return '%s - %s - %s' %(self.name, self.description, self.price)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    description = models.TextField()
    itemsOrdered = models.TextField()
    amountDue = models.DecimalField(max_digits=9, decimal_places=2)
    amountOutstanding = models.DecimalField(max_digits=9, decimal_places=2)
    orderStatus = models.TextField()
    menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    dateTimeCreated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    

class OrderStatus(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.title


class MessageStatus(models.Model):
    #messagesID = models.ForeignKey(Notification, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.title


class Notification(models.Model):
    subjecteUser = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    message = models.TextField()
    dateTimeCreated = models.DateTimeField(auto_now=True)
    messageStatus = models.ForeignKey(MessageStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



