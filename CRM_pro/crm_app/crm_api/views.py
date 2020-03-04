from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CustomreSerializer, ProductSerializer, OrderSerializer
from crm_app.models import Products, Customers, Orders
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet


#
# @login_required(login_url='login')
# class CustomerApiViewList(ListCreateAPIView):
#     queryset = Customers.objects.all()
#     serializer_class = CustomreSerializer
#
#
# @login_required(login_url='login')
# class CustomerApiViewDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Customers.objects.all()
#     serializer_class = CustomreSerializer
#
#
# @login_required(login_url='login')
# class ProductsApiViewList(ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#
#
# @login_required(login_url='login')
# class ProductsApiViewDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#
#
# @login_required(login_url='login')
# class OrdersApiViewList(ListCreateAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrderSerializer
#
#
# @login_required(login_url='login')
# class OrdersApiViewDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrderSerializer

# @login_required(login_url='login')
class CustomerModelViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomreSerializer


# @login_required(login_url='login')
class ProductModelViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


# @login_required(login_url='login')
class OrdersModelViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
