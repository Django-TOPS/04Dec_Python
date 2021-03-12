from django.db import models

# Create your models here.
class signup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()
    
    def __str__(self):
        return self.fname

class mynotes(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    #myfile=models.FileField(upload_to='Upload')
    myfile=models.ImageField(upload_to="gallery")
    comments=models.TextField()

    def __str__(self):
        return self.title