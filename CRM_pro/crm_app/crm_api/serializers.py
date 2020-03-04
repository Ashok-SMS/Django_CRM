from crm_app.models import Customers, Orders, Products
from rest_framework.serializers import ModelSerializer


class CustomreSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
