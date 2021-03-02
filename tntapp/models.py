from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product')
    category = models.CharField(max_length=50)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
