from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    occupation = models.CharField(max_length=40)
