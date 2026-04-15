from rest_framework import serializers
from order.models import Cart ,Cartitem,Order,OrderItem
from product.models import  Product
from product.seralizer import Productserilizer
from order.services import orderservices

class Emptyseilizer(serializers.Serializer):
    pass


class NessaryINFOofProduct(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','price']

class Addcartitemserilizer(serializers.ModelSerializer):
    product_id  = serializers.IntegerField()
    class Meta:
        model = Cartitem
        fields=['id','product_id','quantity']
    
    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = Cartitem.objects.get(cart_id = cart_id , product_id = product_id)
            cart_item.quantity +=quantity
            self.instance = cart_item.save()

        except Cartitem.DoesNotExist:
           self.instance =  Cartitem.objects.create(cart_id=cart_id , **self.validated_data)

        return self.instance
    
    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError(f"product is {value} does not exixts")
        return value

class Updatacartitem(serializers.ModelSerializer):
    class Meta:
        model = Cartitem
        fields=['quantity']
        

class Cartitemserilizer(serializers.ModelSerializer):
    product = NessaryINFOofProduct()
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model=Cartitem
        fields=['id','product','quantity','product','total_price']
    
    def get_total_price(self,cart_item:Cartitem):
        return cart_item.quantity * cart_item.product.price


class Cartserilizer(serializers.ModelSerializer):
    items=Cartitemserilizer(many=True,read_only=True)

    total_price=serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = Cart
        fields=['id','user','items','total_price']
        read_only_fields = ['user']

    def get_total_price(self,cart:Cart):
        return sum([item.product.price*item.quantity for item in cart.items.all()])

class Createorderserilizer(serializers.Serializer):
    cart_id= serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk = cart_id).exists():
            raise serializers.ValidationError('No cart found with thid id ')
        if not Cartitem.objects.filter(cart_id = cart_id).exists():
            raise serializers.ValidationError('cart is empty')
        
        return cart_id
    
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        cart_id = validated_data["cart_id"]

        try:
            order = orderservices.create_order(user_id=user_id,cart_id=cart_id)
            return order
        except ValueError as e:
            raise serializers.ValidationError(str(e))




    def to_representation(self, instance):
        return Orderserilizer(instance).data






class OrderItemSerler(serializers.ModelSerializer):
    product = NessaryINFOofProduct()
    class Meta:
        model = OrderItem
        fields = ['id','product','quantity','price']

class updateorserserilizer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields=['status']
    

        
        

class Orderserilizer(serializers.ModelSerializer):
    items = OrderItemSerler(many  = True)
    class  Meta:
        model  = Order
        fields = ['id','user','status','total_price','created_at' ,'items']


