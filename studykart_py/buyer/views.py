from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from products.models import products,sold_products,categories
from buyer.models import wishlist
from django.db.models import F,Q
from django.contrib.auth.models import User
from .algorithms import lcs,sort
from user.models import roles
from django.contrib.auth import login as login_user
from django.contrib.auth import authenticate,password_validation
from buyer.forms import edit_profile,signin_card
from .authetication import seller_product_ownership_athentication
# Create your views here.


def main_page(request):
    all_products  = products.objects.all()
    all_categories = categories.objects.all()
    is_seller = False
    signin_form = signin_card()
    seller_role = roles.objects.get(pk=2)
    if request.user.is_authenticated and seller_role in request.user.roles_set.all():
        is_seller=True
    context_dict = {'products':all_products,'categories':all_categories,'is_seller':is_seller,'form':signin_form}
    return render(request,'buyer/index.html',context_dict)


def main_page_key(request,key):
    all_products  = products.objects.filter(Q(product_category_id=key))
    all_categories = categories.objects.all()
    context_dict = {'products':all_products,'categories':all_categories}
    return render(request,'buyer/index.html',context_dict)


def search_page(request):
    if request.GET:
        para_dict = request.GET
        value = para_dict['search-result']
        related_products = products.objects.all().order_by('product_price')
        products_count=0
        product_list = []
        max_match = 0
        for product in related_products:
            lcs_val = lcs(str(product.product_name),value)
            max_match = max(max_match,lcs_val)
        for product in related_products:
            product_tuple = (product,lcs(str(product.product_name),value))
            if(product_tuple[1]>int(max_match/2) and product_tuple[1]>=int(len(value))/2):
                product_list.append(product_tuple)
                products_count+=1
        sort(product_list)
        final_product_list=[]
        for i in product_list:
            final_product_list.append(i[0])
        context_dict = {'products':final_product_list,'total_products':products_count,'search_result':value}
        return render(request, 'buyer/search.html',context_dict)
    return render(request,'buyer/search.html')


def product_page(request,key):
        try:
            product = products.objects.get(pk=key)
        except products.DoesNotExist:
            return redirect('main-page')
        in_wishist = False
        is_user_seller=False
        if request.user.is_authenticated:
            is_user_seller = seller_product_ownership_athentication(request, key)
            wishlist_products = wishlist.objects.filter(buyer=request.user)
            for w_product in wishlist_products:
                if product == w_product.products:
                    in_wishist=True
                    break

        context_dict = {'product':product,'in_wishlist':in_wishist,'is_user_seller':is_user_seller}
        return render(request,'buyer/product-desc-page.html',context_dict)


@login_required
def logout_user(request):
    logout(request)
    return redirect('main-page')


def signin_card_validator(request):
    if request.method == 'POST':
        login_form = signin_card(request.POST)
        if login_form.is_valid():
            identifier = login_form.cleaned_data['identifier']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=identifier, password=password)
            if user != None:
                login_user(request, user)
                return redirect('main-page')
            else:
                context_dict = {'form': login_form, 'invalid_credentials': True}
                return render(request, 'buyer/index.html', context_dict)
        else:
            context_dict = {'form': login_form, 'invalid_credentials': True}
            return render(request, 'buyer/index.html', context_dict)

    else:
        login_form = signin_card()
        context_dict = {'form': login_form, 'invalid_credentials': False}
        return render(request, 'buyer/index.html', context_dict)


@login_required
def user_profile(request):
    if request.POST:
        edit_form = edit_profile(request.POST)
        context_dict = {'form':edit_form}
        if edit_form.is_valid():
            fname = edit_form.cleaned_data['first_name']
            lname = edit_form.cleaned_data['last_name']
            username = edit_form.cleaned_data['username']
            email = edit_form.cleaned_data['email']
            mobile = edit_form.cleaned_data['mobile']
            if edit_form.has_changed():
                user = request.user
                user.first_name = fname
                user.last_name = lname
                user.username = username
                user.email = email
                user.user_profile.user_mobile = mobile
                user.save()
                user.user_profile.save()
            return redirect('profile')
        else:
            return render(request, 'buyer/profile.html',context_dict)
    else:
        user = request.user
        edit_dict={'first_name':user.first_name,'last_name':user.last_name,'username':user.username,'email':user.email,'mobile':user.user_profile.user_mobile}
        edit_form = edit_profile(edit_dict)
        context_dict={'form':edit_form}
    return render(request,'buyer/profile.html',context_dict)


@login_required
def wishlist_list(request):
    current_user = request.user.pk
    user = User.objects.get(pk=current_user)
    wish_list = wishlist.objects.filter(buyer=user)
    total_products = wishlist.objects.filter(buyer=user).count()
    final_list=[]
    total_amt=0
    for i in wish_list:
        product = products.objects.get(pk = i.products_id)
        final_list.append(product)
        total_amt += product.product_price
    context_dict = {'wishlist':final_list,'total_products':total_products,'total_amt':total_amt}
    return render(request,'buyer/wishlist.html',context_dict)


@login_required
def add_to_wishlist(request,key):
    list = wishlist.objects.create(buyer=request.user,products_id=key)
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request,key):
    list = wishlist.objects.filter(Q(buyer=request.user),Q(products_id=key))
    list.delete()
    return redirect('wishlist')

@login_required
def cart(request):
    return render(request,'buyer/cart.html')


@login_required
def checkout(request,key):
    product = products.objects.get(pk=key)
    if product.is_booked == 0:
        context_dict = {'product': product}
        return render(request,'buyer/checkout.html',context_dict)
    else:
        return redirect('main-page')


@login_required
def buy(request):
    if request.method == 'POST':
        pk = request.POST.get('secure-credential','')
        product = products.objects.get(pk=pk)
        if product.is_booked == 0:
            product.is_booked=1
            product.user_booked=request.user
            product.save()
        else:
            return redirect('main-page')
    return redirect('main-page')


@login_required
def cancel(request,key):
    if request.POST:
        secure_key = request.POST.get('secure-key','')
        cancel_product = products.objects.get(pk=secure_key)
        cancel_product.is_booked=0
        cancel_product.save()
        return redirect('main-page')
    else:
        product = products.objects.get(pk=key)
        if product.is_booked and product.user_booked == request.user:
            context_dict = {'product': product}
            return render(request,'buyer/cancel.html',context_dict)
        else:
            return redirect('main-page')


@login_required
def orders(request):
    all_orders = products.objects.filter(Q(user_booked=request.user),Q(is_booked=1))
    bought_orders = sold_products.objects.filter(product_buyer=request.user)
    context_dict = {'products':all_orders,'sold_products':bought_orders}
    return render(request,'buyer/order.html',context_dict)