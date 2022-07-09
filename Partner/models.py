from django.db import models
from Users.models import User
# Create your models here.

class Partner(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Donate(models.Model):
    Name=models.CharField(max_length=200)
    email=models.EmailField(null=False,blank=False)
    amount=models.FloatField(null=False,blank=False)
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ('-date_created',)




class Event(models.Model):
    Title=models.CharField(max_length=250)
    description=models.TextField()
    image=models.ImageField(null=True,blank=False,upload_to='Partner_Event/')
    date_created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=('-date_created',)

    def __str__(self):
        return self.Title


class New(models.Model):
    Title=models.CharField(max_length=250)
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-date_created',)

    def __str__(self):
        return self.Title

class Category(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Contribute(models.Model):
    partner=models.ForeignKey(Partner,on_delete = models.CASCADE)
    amount=models.FloatField(null=False,blank=False)
    categories=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=False)
    date_created=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=('-date_created',)
