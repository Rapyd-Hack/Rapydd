from django.db import models

# Create your models here.
class Product(models.Model):
    name =models.CharField(max_length = 100)
    amount = models.IntegerField(default = 0)
    price = models.IntegerField(default = 0)
    currency = models.CharField(max_length=6)
    file = models.FileField(upload_to = "product_files/", blank = True, null = True)
    url = models.URLField()
    description = models.CharField(max_length = 1056)

    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price)
