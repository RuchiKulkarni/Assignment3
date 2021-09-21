from django.db import models
class student(models.Model):
    name=models.CharField(max_length=60)
    college=models.CharField(max_length=60)
    city=models.CharField(max_length=100)
