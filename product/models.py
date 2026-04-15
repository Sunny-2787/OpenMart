from django.db import models
from django.conf import settings
from product.validators import valited_file_size
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,related_name='product')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product  = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(
        upload_to="product/images/", validators=[valited_file_size]
    )

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    comment = models.TextField()
    ratings = models.PositiveBigIntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)]  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Review By {self.user.first_name} on {self.product.name}"


    
