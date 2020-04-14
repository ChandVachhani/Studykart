from django.db import models
from django.contrib.auth.models import User


class categories(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table='categories'
    def __str__(self):
        return self.name


class products(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=300)
    product_price = models.IntegerField()
    product_seller = models.ForeignKey(User,on_delete=models.CASCADE)
    products_image = models.ImageField(default='default.png',upload_to='__892374product_8129083_imgs!@__')
    product_category = models.ForeignKey(categories,on_delete=models.CASCADE,default='1')
    is_booked = models.BooleanField(default=0,blank=False)
    user_booked = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_booked',null=True,blank=True)
    class Meta:
        db_table = 'products'

class sold_products(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=300)
    product_price = models.IntegerField()
    product_buyer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='buyer')
    product_seller = models.ForeignKey(User,on_delete=models.CASCADE,related_name='seller')
    products_image = models.ImageField(default='default.png',upload_to='__892374product_8129083_imgs!@__')
    product_category = models.ForeignKey(categories, on_delete=models.CASCADE)
    class Meta:
        db_table = 'sold_products'
