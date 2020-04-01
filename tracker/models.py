from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Wallet(models.Model):
    name=models.CharField(max_length=100)
    balance=models.IntegerField()
    last_transaction=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)



class Expense(models.Model):
    title= models.CharField(max_length = 100 )
    Amount =models.IntegerField() 
    timestamp =models.DateTimeField(auto_now=True) 
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True,blank=True) 
    

    def __str__(self):
        return self.title


class Income(models.Model):
    title= models.CharField(max_length = 100 )
    description=models.TextField()
    Amount =models.IntegerField() 
    timestamp =models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True,blank=True) 

    def __str__(self):
        return self.title