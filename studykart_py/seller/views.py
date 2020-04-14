from django.shortcuts import render,redirect
from seller.forms import add_product1,add_product2,edit_product
from products.models import products,sold_products
from seller.authentication import seller_authentication,seller_product_authentication
from django.contrib.auth.decorators import login_required
from seller.flipkart_scrapper import flipkart_data,flipkart_link
from products.models import categories
# Create your views here.


@login_required
def add_product_view(request):
    if seller_authentication(request):
        add_product_form = add_product1()
        context_dict = {'form':add_product_form}
        return render(request,'seller/add_product.html',context_dict)
    else:
        return redirect('main-page')


def add_product_success(request):
    if request.POST:
        add_product_form = add_product2(request.POST,request.FILES)
        if add_product_form.is_valid():
            image = add_product_form.cleaned_data['product_image']
            price = add_product_form.cleaned_data['product_price']
            name = request.POST.get('secure-name','')
            category = request.POST.get('secure-category', '')
            description = request.POST.get('secure-description', '')
            insert_product = products.objects.create(product_name=name, product_description=description,
                                                     product_price=price, products_image=image,
                                                     product_seller=request.user, product_category_id=category)
            return redirect('main-page')


def add_product_view2(request):
    if request.POST:
        add_product_form = add_product1(request.POST)
        if add_product_form.is_valid():
            name = add_product_form.cleaned_data['product_name']
            description = add_product_form.cleaned_data['product_desciption']
            add_product_form = add_product2()
            flip = flipkart_data(name)
            flip_link = flipkart_link(name)
            category = categories.objects.all()
            if flip==-1:
                content_dict = {'form': add_product_form, 'name': name, 'description': description,
                                'flipkart_product': flip, 'categories': category}
            else:
                content_dict = {'form': add_product_form,'name':name,'description':description,'flipkart_product':flip[0],'flipkart_price':flip[1],'categories':category,'flip_link':flip_link}
            return render(request, 'seller/add-product2.html', content_dict)
    else:
        return redirect('add-product')


@login_required
def seller_product_view(request):
    if request.POST:
        key = request.POST.get('secure-key','')
        sold_product = products.objects.get(pk=key)
        sold_product_add = sold_products.objects.create(product_name=sold_product.product_name,
                                                        product_seller=sold_product.product_seller,
                                                        products_image=sold_product.products_image,
                                                        product_price=sold_product.product_price,
                                                        product_description=sold_product.product_description,
                                                        product_buyer=sold_product.user_booked,
                                                        product_category=sold_product.product_category)
        sold_product.delete()


    sold_product = sold_products.objects.filter(product_seller=request.user)
    all_products = products.objects.filter(product_seller=request.user).order_by('-is_booked')
    context_dict = {'products':all_products,'sold_products':sold_product}
    return render(request,'seller/products.html',context_dict)


@login_required
def edit_product_view(request,key):
    if seller_product_authentication(request,key):
        if request.POST:
            edit_form = edit_product(request.POST,request.FILES)
            if edit_form.is_valid() and edit_form.has_changed():
                product = products.objects.get(pk=key)
                product.product_name = edit_form.cleaned_data['product_name']
                product.product_description = edit_form.cleaned_data['product_description']
                product.product_price = edit_form.cleaned_data['product_price']
                product.products_image = edit_form.cleaned_data['product_image']
                product.save()
                return redirect('products')
            else:
                context_dict = {'form': edit_form}
                return render(request,'seller/products.html',context_dict)
        else:
            product = products.objects.get(pk=key)
            bound_dict = {'product_name':product.product_name,
                          'product_description':product.product_description,
                          'product_price':product.product_price,
                          'product_image':product.products_image}
            edit_form = edit_product(bound_dict)
            context_dict = {'form':edit_form}
            return render(request,'seller/edit-product.html',context_dict)
    return redirect('main-page')