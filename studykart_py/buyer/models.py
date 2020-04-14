from django.db import models
from django.contrib.auth.models import User
from products.models import products
# Create your models here.
class wishlist(models.Model):
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(products,on_delete=models.CASCADE)
    class Meta:
        db_table='wishlist'
        unique_together=('buyer','products')