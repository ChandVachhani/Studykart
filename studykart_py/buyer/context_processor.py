from user.models import roles


def is_seller_processor(request):
    seller_role = roles.objects.get(pk=2)
    is_seller=False
    if request.user.is_authenticated and seller_role in request.user.roles_set.all():
        is_seller=True
    context_dict = {'is_seller':is_seller}
    return context_dict