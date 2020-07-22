from django.urls import path, include
from .views import productList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', productList)

urlpatterns = [
    path('', include(router.urls))
]