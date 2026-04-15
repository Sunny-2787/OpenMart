from django.urls import path,include
from product.views import PoductViewset,Catagoryviewset,Reviewviewset,ProductImageViewSet
from rest_framework_nested import routers
from order.views import CartViewset,Cartitemviewset,OrderViewset

router = routers.DefaultRouter()
router.register('products',PoductViewset)
router.register('catagory',Catagoryviewset)
router.register('carts',CartViewset,basename='carts')
router.register('oders',OrderViewset,basename='oders')


productrouter=routers.NestedDefaultRouter(router,'products',lookup='product')
productrouter.register('reviews',Reviewviewset,basename='product-review')
cartrouter = routers.NestedDefaultRouter(router,'carts',lookup='cart')
cartrouter.register('items',Cartitemviewset,basename="cart-items")
productrouter.register('image',ProductImageViewSet,basename='product-images')

urlpatterns = [
    
    path('',include(router.urls)),
    path('',include(productrouter.urls)),
    path('',include(cartrouter.urls)),
    path("auth/",include('djoser.urls')),
    path("auth/",include('djoser.urls.jwt')),
]
