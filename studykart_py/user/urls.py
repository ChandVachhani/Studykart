from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('buyer_signup/', views.SignUpBuyer,name='signup_buyer'),
    path('seller_signup/', views.SignUpSeller,name='signup_seller'),
    path('pandas/', views.filter, name='filters')
]