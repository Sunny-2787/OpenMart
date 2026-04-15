from django.urls import path
from product import views



urlpatterns = [
    path("",views.Productlist.as_view(),name="product-list"),
    path("<int:pk>/",views.DetailsProduct.as_view(),name="product-list"),
  


]
