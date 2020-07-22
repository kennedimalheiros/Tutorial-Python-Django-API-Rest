from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


def home(request):
    return render(request, 'index.html')


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
