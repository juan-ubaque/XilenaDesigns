from django.db import models

# Create your models here.
class Product(models.Model):
    Product = models.CharField(max_length=120)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField()
    image = models.ImageField(upload_to='products', blank=True, null=True)
    def __str__(self):
        return self.Product


class Categories(models.Model):
    name_categories = models.TextField(blank=False, null=False)
    
    def __str__(self):
        return self.name_categories
    

class Cart(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    def __str__(self):
        return self.product.Product


