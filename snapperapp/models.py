from django.db import models
from tinymce.models import HTMLField 


# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):

        return self.name 
    

class Subcategory(models.Model):

     cate = models.ForeignKey(Category, on_delete=models.CASCADE) 
     name = models.CharField(max_length=200)

     def __str__(self):
         
         return self.name   
     
class Product(models.Model):
    
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='ecomm/pimg', null=True)
    disc = HTMLField(null =True)
    date = models.DateField(auto_now_add=True)
    code = models.IntegerField()

    def __str__(self):

        return self.name
    
class Inquriy(models.Model):

    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    mobile = models.CharField(max_length=15)
    ps = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def __str__(self):

        return self.name    

class Address(models.Model):

    adds = models.CharField(max_length=1000)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

    def __str__(self):

        return self.adds
    

