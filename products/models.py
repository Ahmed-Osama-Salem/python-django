from django.db import models

# Create your table for products by create class.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    discription = models.TextField()
    image= models.ImageField(upload_to= "images/%y/%m/%d")
    active= models.BooleanField(default=False)

    