from django.urls import path
from product import views



urlpatterns = [

    path("",views.CatagoryList.as_view(),name="catagory-list"),
    path("<int:pk>/",views.DetailsCatagory.as_view(),name="catagory")

]
