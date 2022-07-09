from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
	username=models.CharField(unique=True,max_length=100)
	email=models.EmailField(unique=True,null=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone=models.CharField(max_length=30,null=True,blank=True)
	profile_pic=models.ImageField(default="no_avatar.jpg",null=True,blank=False,upload_to='Partner_profile_picture/')
	country=models.CharField(max_length=50)
	Occupation=models.CharField(max_length=100)
	is_partner=models.BooleanField(default=False)



	USERNAME_FIELD='email'

	REQUIRED_FIELDS=['username']
 
