from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# NAME OF CATEGORIES
class Category(models.Model):
    category_name = models.CharField(max_length=250)
    category_pic = models.FileField(upload_to="images/", default=True)


    def __str__(self):
        return self.category_name


# PRODUCT DETAILS
# choice field for product according gender
according_gender = (
    ("Select Gender", "Select Gender"),
    ("Male", "Male"),
    ("Female", "Female"),
    ("Kid", "Kid"),
    ("All", "All")
)


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    product_desc = models.TextField(max_length=300)
    product_pic = models.FileField(upload_to="images/")
    product_price = models.FloatField()
    product_view = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_for = models.CharField(choices=according_gender, max_length=20)

    def __str__(self):
        return self.product_name

#NEWS LETTER

class Gender(models.Model):
    gender_name = models.CharField(max_length=50)

    def __str__(self):
        return self.gender_name

class Newsletter(models.Model):
    mailid = models.EmailField(max_length=100)

    def __str__(self):
        return self.mailid

class Profileusers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    gender=models.CharField(max_length=100,default="Male")
    profile_pic=models.FileField(upload_to="images/",null=True)
    city=models.CharField(max_length=200,default="India")
    doc=models.DateField(auto_now=True)
    def __str__(self):
        return self.phone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name