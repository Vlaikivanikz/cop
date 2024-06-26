from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    occupation = models.CharField(max_length=40)
    salary = models.IntegerField(default=1)
    exp = models.CharField(max_length=40,default='DEFAULT VALUE')
    education = models.CharField(max_length=40,default='DEFAULT VALUE')
    skills = models.CharField(max_length=40,default='DEFAULT VALUE')
    citizenship = models.CharField(max_length=40,default='DEFAULT VALUE')
    location = models.CharField(max_length=40,default='DEFAULT VALUE')
    photo = models.ImageField(default='DEFAULT VALUE')
    contacts = models.CharField(max_length=40,default='DEFAULT VALUE')
    age = models.IntegerField(default=1)
    ifOnlineWork = models.CharField(max_length=40,default='DEFAULT VALUE')
    about = models.CharField(max_length=40, default='DEFAULT VALUE')