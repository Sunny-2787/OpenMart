from django.contrib import admin
from order.models import Cart,Cartitem,Order,OrderItem
# Register your models here.

@admin.register(Cart)
class Cartadmin(admin.ModelAdmin):
    list_display=['id','user']


@admin.register(Order)
class orderadmn(admin.ModelAdmin):
    list_display=['id','user','status']


admin.site.register(Cartitem)
admin.site.register(OrderItem)




