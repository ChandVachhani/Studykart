from django.contrib.auth.models import User
from products.models import products
from user.models import roles


def seller_authentication(request):
    User = request.user
    seller = roles.objects.get(pk=2)
    all_roles = User.roles_set.all()
    if seller in all_roles:
        return True
    else:
        return False

def seller_product_authentication(request,key):
    if seller_authentication(request):
        user = request.user
        product = products.objects.get(pk=key)
        if product in user.products_set.all():
            return True
        else:
            return False
    else:
        return False