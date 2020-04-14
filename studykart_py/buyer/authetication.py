from products.models import products


def seller_product_ownership_athentication(request,key):
    product = products.objects.get(pk=key)
    if product in request.user.products_set.all():
        return True
    else:
        return False