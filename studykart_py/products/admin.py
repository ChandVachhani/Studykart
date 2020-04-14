from django.contrib import admin
from .models import products,sold_products,categories
# Register your models here.
admin.site.register(products)
admin.site.register(sold_products)
admin.site.register(categories)
