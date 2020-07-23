from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django_filters import rest_framework as filters


def home(request):
    return render(request, 'index.html')


class ProductFilter(filters.FilterSet):
    #description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = {
            'description': ['icontains'],
            'stock': ['gte'],
        }

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #filterset_fields = ('description',)
    filterset_class = ProductFilter
