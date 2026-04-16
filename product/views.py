from product.models import Product,Catagory,Review,ProductImage
from product.seralizer import Productserilizer,CatagorySerializer,Reviewserilizer,ProductImageSerilizer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import productfilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.pagination import mypagination
from rest_framework.permissions import AllowAny,IsAdminUser
from api.permission import IsadminOrReadonly 
from product.permission import IsreviewAuthororreadonly
# Create your views here.


    
class PoductViewset(ModelViewSet):

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    serializer_class=Productserilizer
    filterset_class = productfilter
    pagination_class = mypagination
    search_fields = ['name','description']
    ordering_fields=['price']
    permission_classes = [IsadminOrReadonly]

    def get_queryset(self):
        return Product.objects.prefetch_related('images').all()



class ProductImageViewSet(ModelViewSet):
    serializer_class  = ProductImageSerilizer
    permission_classes = [IsadminOrReadonly]

    def get_queryset(self):
        return ProductImage.objects.filter(product_id = self.kwargs.get('product_pk'))
    def perform_create(self, serializer):
        serializer.save(product_id = self.kwargs.get('product_pk'))

class Catagoryviewset(ModelViewSet):
    queryset = Catagory.objects.annotate(product_count=Count('product')).all()
    serializer_class=CatagorySerializer
    permission_classes = [IsadminOrReadonly]

    
class Reviewviewset(ModelViewSet):
    serializer_class=Reviewserilizer
    permission_classes = [IsreviewAuthororreadonly]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def perform_update(self, serializer):
        serializer.save(user = self.request.user )

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs.get('product_pk'))
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs.get('product_pk')}
    


    


    

    

    