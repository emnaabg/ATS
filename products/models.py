from django.db import models

# Create your models here.
class production(models.Model):
    color = models.CharField(max_length=36)
    category  = models.CharField(max_length=255)
    productName = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    productMaterial = models.CharField(max_length=255)
    imageUrl= models.CharField(max_length=255)
    createdAt = models.CharField(max_length=255)

class review(models.Model):
    idproducton = models.IntegerField(default=0)
    rating = models.CharField(max_length=36)
    content  = models.CharField(max_length=255)
        