from rest_framework import serializers
from decimal import Decimal
from product.models import Product,Catagory,Review,ProductImage
from django.contrib.auth import get_user_model


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields =['id','name','description','product_count']

    product_count = serializers.IntegerField(read_only=True)

class ProductImageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id','image']


class Productserilizer(serializers.ModelSerializer):
    images = ProductImageSerilizer(many = True,read_only =True)
    class Meta:
        model = Product
        fields=['id','name','description','price','stock','catagory','price_with_tax','images']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')
        
    def calculate_tax(self,product):
        return round(product.price * Decimal(1.1),2)
    
    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Price could not be negative')
        return price





class Simpleuserserrilizer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name="get_current_user_name")
    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_current_user_name(self , obj):
        return obj.get_full_name()

class Reviewserilizer(serializers.ModelSerializer):
    # user = Simpleuserserrilizer()
    user = serializers.SerializerMethodField(method_name="get_user")

    class  Meta:
        model = Review
        fields=['id','user','comment','ratings','product']
        read_only_fields = ['user','product']
    def get_user(self,obg):
        return Simpleuserserrilizer(obg.user).data
    
    def create(self,validated_data):
        product_id=self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data)




    