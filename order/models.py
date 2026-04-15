from django.db import models
from users.models import USER
from product.models import Product
from uuid import uuid4
from django.core.validators import MinValueValidator

# Create your models here.

class Cart(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    user = models.OneToOneField(USER,on_delete=models.CASCADE,
                                related_name=  "cart"  
                                ) 
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"cart of {self.user.username}"

class Cartitem(models.Model):
    cart = models.ForeignKey(
        Cart,on_delete=models.CASCADE,related_name='items'
    )   
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = [['cart','product']]


    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
class Order(models.Model):
    Not_Paid = 'Not Paid'
    Ready_to_ship = 'Ready_to_ship'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    CANCELED = 'Canceled'
    STATUS_CHOICES = [
        (Not_Paid, 'Not Paid'),
        (Ready_to_ship ,  'Ready_to_ship'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (CANCELED, 'Canceled'),
    ]
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    user = models.ForeignKey(
        USER, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=Not_Paid)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.first_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price =  models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"