from django.conf.urls import url, include
# from .views import CustomerApiViewDetail, CustomerApiViewList, ProductsApiViewDetail, ProductsApiViewList, \
#     OrdersApiViewDetail, OrdersApiViewList
from rest_framework.routers import DefaultRouter

from .views import CustomerModelViewSet, ProductModelViewSet, OrdersModelViewSet
from crm_app.models import Customers
#
# urlpatterns = [
#     url(r'^customer/$', CustomerApiViewList.as_view()),
#     url(r'^customer/(?P<pk>[1-9]+)/$', CustomerApiViewDetail.as_view()),
#     url(r'^product/$', ProductsApiViewList.as_view()),
#     url(r'^product/(?P<pk>[1-9]+)/$', ProductsApiViewDetail.as_view()),
#     url(r'^order/$', OrdersApiViewList.as_view()),
#     url(r'^order/(?P<pk>[1-9]+)/$', OrdersApiViewDetail.as_view()),
#
#
#
# ]


router = DefaultRouter()
router.register('customer', CustomerModelViewSet,basename='Customers')
router.register('product', ProductModelViewSet)
router.register('order', OrdersModelViewSet)
urlpatterns = [
    url('', include(router.urls))
]
