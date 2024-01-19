from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

class ProductPhoto(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_photos')
    file = models.FileField(upload_to='Products/')
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file.path