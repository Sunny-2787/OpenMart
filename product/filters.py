from django_filters.rest_framework import FilterSet
from product.models import Product
class productfilter(FilterSet):
    class Meta:
        model = Product
        fields={
            'catagory_id':['exact'],
            'price':['gt','lt']
        }