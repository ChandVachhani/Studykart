from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.add_product_view,name='add-product'),
    path('add-product-next/', views.add_product_view2,name='add-product-next'),
    path('add-product-success/',views.add_product_success,name='add-product-success'),
    path('edit-product/<int:key>/',views.edit_product_view,name='edit-product'),
    path('products/', views.seller_product_view,name='seller-products'),
]