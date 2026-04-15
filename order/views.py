from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from order.models import Cart,Cartitem,Order,OrderItem
from order.serilizer import Cartserilizer,Cartitemserilizer,Addcartitemserilizer,Updatacartitem,Orderserilizer,Createorderserilizer,updateorserserilizer,Emptyseilizer,updateorserserilizer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import action
from order.services import orderservices
from rest_framework.response import Response
 
class CartViewset(GenericViewSet,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin):

    serializer_class=Cartserilizer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    
    def get_queryset(self):
        
        if getattr(self,'swagger_fake_view',False):
            return Cart.objects.none()
        return Cart.objects.prefetch_related('items__product').filter(user = self.request.user)

class Cartitemviewset(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    def get_serializer_class(self):
        if self.request.method=="POST":
            return Addcartitemserilizer
        if self.request.method=="PATCH":
            return Updatacartitem
        return Cartitemserilizer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        if getattr(self,'swagger_fake_view',False):
            return context

        return {'cart_id':self.kwargs.get('cart_pk')}
    
    def get_queryset(self):
        return Cartitem.objects.select_related('product').filter(cart_id = self.kwargs.get('cart_pk'))
    



class OrderViewset(ModelViewSet):
    http_method_names=['get','post','patch','delete','head','options']

    @action(detail=True,methods=['post'])
    def cancel(self,request,pk =None):
        order = self.get_object()
        orderservices.cancle_order(order=order , user = request.user)
        return Response({"status":'order canceled'})
    
    @action(detail=True,methods=['patch'])
    def Update_status(self,request,pk =None):
        order = self.get_object()
        serializer = updateorserserilizer(order,data= request.data,partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":f'order status updated to {request.data['status']}'})
    
  
    def get_permissions(self):
        if self.action in ['Update_status', 'destroy']:
            return [IsAdminUser()]
        return[IsAuthenticated()] 
    


    def get_serializer_class(self):
        if self.action=="cancel":
            return Emptyseilizer
        if self.action=="create":
           return Createorderserilizer
        elif self.action=="Update_status":
            return updateorserserilizer
        return Orderserilizer
    
    def get_serializer_context(self):
        if getattr(self,'swagger_fake_view',False):
            return super().get_serializer_context()

        return {'user_id': self.request.user.id ,'user': self.request.user }


    def get_queryset(self):
        if getattr(self,'swagger_fake_view',False):
                return Order.objects.none()
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user = self.request.user)
    
