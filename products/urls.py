from django.urls import path
from . import views

urlpatterns=[
    path('',views.allproducts,name='allproducts'),
    path('oneproduct/<str:id>',views.oneproduct, name='oneproduct'),


]