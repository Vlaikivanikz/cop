from django.db import models

class Portfolio(models.Model):
    userName = models.CharField(max_length=20,default='DEFAULT VALUE')
    name = models.CharField(max_length=20,default='DEFAULT VALUE')
    occupation = models.CharField(max_length=200,default='DEFAULT VALUE')
    salary = models.CharField(max_length=20,default='DEFAULT VALUE')
    exp = models.CharField(max_length=400,default='DEFAULT VALUE')
    education = models.CharField(max_length=200,default='DEFAULT VALUE')
    skills = models.CharField(max_length=400,default='DEFAULT VALUE')
    location = models.CharField(max_length=40,default='DEFAULT VALUE')
    age = models.CharField(max_length=20,default='DEFAULT VALUE')
    about = models.CharField(max_length=500, default='DEFAULT VALUE')
    mail = models.CharField(max_length=40,default='DEFAULT VALUE')
    phone = models.CharField(max_length=40,default='DEFAULT VALUE')
    hobby = models.CharField(max_length=100,default='DEFAULT VALUE')
    languages = models.CharField(max_length=100, default='DEFAULT VALUE')
    sch = models.CharField(max_length=40,default='DEFAULT VALUE')
    com = models.CharField(max_length=40,default='DEFAULT VALUE')
class Comment(models.Model):
    text = models.CharField(max_length=100, default='none')
    date = models.CharField(max_length=15, default='none')
    ref = models.CharField(max_length=10, default='none')
    author = models.CharField(max_length=50, default='anonym')
    verified = models.CharField(max_length=20,default='verificated')
    idToPort = models.CharField(max_length=20,default='none')
class User(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    

