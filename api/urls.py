from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.Prodict_list, name='product-list'),
]
