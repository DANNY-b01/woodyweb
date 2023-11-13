from django.db import models




class Category(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="category_images")



# Create your models here.
