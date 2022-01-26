from django.db import models

# Create your models here.

# Module has many models or classes
# Model is used to represent


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True) #  every data will be stored as strings 123 = '123' Entertainment and news
    slug = models.SlugField(max_length=200) # every data will be stored as slug 'my name' = 'my-name'
    content = models.TextField()
    date = models.DateField()
    phone_number = models.IntegerField() # every data will be stored as Integer 123 = 123 2.5 = 2


class Blog(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    # price = models.DecimalField() # 2.5 = 2.5 every data will be stored as Float 123 = 123.00000000000
    # name = models.DateTimeField() # every data will be stored as Date m12/d3/y2021 12:55:03 00000000
    # name = models.DateField() # every data will be stored as Date m12/d3/y2021
    # name = models.DurationField() # every data will be stored as duration m12/d3/y2021
    # name = models.URLField() # every data will be stored as duration m12/d3/y2021
    # name = models.OneToOneField()
    # name = models.ManyToManyField()
    # name = models.ForeignKey()
