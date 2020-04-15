from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page,name='main-page'),
    path('<int:key>/', views.main_page_key,name='main-page'),
    path('product/<int:key>/',views.product_page,name='products'),
    path('user/wishlist',views.wishlist_list,name='wishlist'),
   # path('user/cart',views.cart,name='cart'),
    path('user/signin_card',views.signin_card_validator,name='signin_card'),
    path('user/orders',views.orders,name='orders'),
    path('user/profile',views.user_profile,name='profile'),
    path('user/search',views.search_page,name='search-page'),
    path('user/logout',views.logout_user,name='logout'),
    path('user/checkout/<int:key>',views.checkout,name='checkout'),
    path('user/buy',views.buy,name='buy'),
    path('user/cancel_booking/<int:key>',views.cancel,name='cancel'),
    path('user/remove/<int:key>',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('user/add_wishlist/<int:key>',views.add_to_wishlist,name='add_to_wishlist'),
]
