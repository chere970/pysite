from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.Prodict_list, name='product-list'),

    path('products/<int:pk>/', views.Product_detail, name='product-detail'),
]
