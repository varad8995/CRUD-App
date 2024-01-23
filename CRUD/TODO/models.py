from django.db import models

# Create your models here.
class Student(models.Model):
    id  = models.BigAutoField(primary_key=True)
    name = models.CharField((""), max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
