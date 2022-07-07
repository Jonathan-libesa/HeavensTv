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
    email=models.EmailField()
    amount=models.FloatField(null=False,blank=False)
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ('-date_created',)




        