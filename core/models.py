from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user= models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    description= models.TextField(max_length=425, blank=True, null=True)
    start_date= models.DateTimeField(auto_now_add=True, blank=True)
    end_date=   models.DateTimeField(auto_now_add=True, blank=True)
    status= models.BooleanField(default= False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['status']