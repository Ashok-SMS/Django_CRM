from django.shortcuts import render, redirect
from .models import Customers, Products, Orders
from .forms import Orderform, Customerform, ProductForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging
from django.contrib.auth.models import User

logger = logging.getLogger()


def registerpage(request):
    logger.info(request.headers)
    if request.user.is_authenticated:
        logger.info('inside registerpage and authenticated ')
        logger.info(request.headers)
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = request.POST.get('username')

                messages.success(request, 'account created sucessfully for ' + user)
                logger.info('inside registerpage and new user ')
                logger.info(request.headers)
                return redirect(loginpage)
        context = {'form': form}
        return render(request, 'crmaccounts/registration.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        logger.info('inside loginpage and authenticated ')
        logger.info(request.path)
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info('inside login page  and new login ')
                logger.info(request.META)
                return redirect('home')
            else:
                messages.warning(request, 'username or password is wrong')
        return render(request, 'crmaccounts/loginpage.html')


def logoutpage(request):
    logout(request)
    logger.info('user loged out ')
    logger.info(request.headers)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    # if request.user.is_authenticated:
    #     print(request.body)
    #     return redirect('/')
    # else:
    admin_user = request.user
    logger.info(admin_user.is_staff)
    logger.info('user logged in successfull ')
    logger.info(request.user)
    if admin_user.is_staff:

        customers = Customers.objects.all()
        products = Products.objects.all()
        orders = Orders.objects.all()

        total_orders = len(orders)
        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()
        outfordelivery = orders.filter(status='OutforDelivery').count()

        context = {'customers': customers, 'products': products, 'orders': orders,
                   'total_orders': total_orders, 'pending': pending, 'delivered': delivered,
                   'outfordelivery': outfordelivery, 'request': request}
        return render(request, 'crmaccounts/dashbord.html', context)
    else:
        customers = Customers.objects.all()
        products = Products.objects.all()
        orders = Orders.objects.filter(id=admin_user.id)

        total_orders = len(orders)
        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()
        outfordelivery = orders.filter(status='OutforDelivery').count()

        context = {'customers': customers, 'products': products, 'orders': orders,
                   'total_orders': total_orders, 'pending': pending, 'delivered': delivered,
                   'outfordelivery': outfordelivery, 'request': request}
        return render(request, 'crmaccounts/dashbord.html', context)


@login_required(login_url='login')
def products(request):
    # if request.user.is_authenticated:
    #     logger.info('inside products page and authenticated ')
    #     logger.info(request.headers)
    #     return redirect('product')
    # else:
    products = Products.objects.all()
    context = {'products': products,'request':request}
    logger.info('inside products page and new login ')
    logger.info(request.headers)
    return render(request, 'crmaccounts/products.html', context)


@login_required(login_url='login')
def customers(request, pk):
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    customers = Customers.objects.get(cid=pk)
    orders = customers.orders_set.all()
    total_orders = orders.count()
    context = {'customers': customers, 'orders': orders, 'total_orders': total_orders, 'request': request}
    return render(request, 'crmaccounts/customers.html', context)


@login_required(login_url='login')
def create_order(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    form = Orderform()

    if request.method == 'POST':
        form = Orderform(request.POST)
        logger.info(Orderform.Meta)
        if form.is_valid():
            form.save()
            # logger.info(form.customer)
            return redirect('/')
        else:
            logger.info(form.customer)
            return HttpResponse("form not valid")
    context = {'form': form, 'request': request}
    return render(request, 'crmaccounts/create_order.html', context)


@login_required(login_url='login')
def update_order(request, pk):
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    order = Orders.objects.get(id=pk)
    form = Orderform(instance=order)
    if request.method == 'POST':
        form = Orderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'crmaccounts/order_form.html', context)


@login_required(login_url='login')
def delete_order(request, pk):
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    order = Orders.objects.get(id=pk)
    order.delete()
    return redirect('/')


@login_required(login_url='login')
def update_customer(request, pk):
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    customer = Customers.objects.get(cid=pk)
    form = Customerform(instance=customer)
    if request.method == 'POST':
        form = Customerform(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'crmaccounts/update_customer.html', context)


@login_required(login_url='login')
def delete_customer(request, pk):
    # if request.user.is_authenticated:
    #     print(request)
    #     return redirect('/')
    # else:
    form = Customers.objects.get(cid=pk)
    form.delete()
    return redirect('/')


@login_required(login_url='login')
def update_product(request, pk):
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    res=HttpResponse("aaaa")
    res.set_cookie('ashok','palaki')
    print(request.COOKIES)
    product = Products.objects.get(pid=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'crmaccounts/product_edit.html', context)


@login_required(login_url='login')
def delete_product(request, pk):
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    form = Products.objects.get(pid=pk)
    form.delete()
    return redirect('/')


@login_required(login_url='login')
def addcustomer(request):
    customers = Customers.objects.all()
    form = Customerform()
    if request.method == 'POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            print(request.headers)
            return redirect(addcustomer)
        else:
            return HttpResponse("Check the values you entered")
        # context = {'form': form}
        # return render(request, 'addcustomer.html', context)
    else:

        context = {'form': form, 'customers': customers}
        return render(request, 'crmaccounts/addcustomer.html', context)
