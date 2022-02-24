from django.db import models

# Create your models here.
class data(models.Model):
    book_name=models.CharField(max_length=50)
    author_name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)

class Record(models.Model):
    ename=models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)