from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('add',views.add,name="add"),
    path('add_inventory',views.add_inventory,name="add_inventory"),
    path('inventory',views.inventory,name="inventory"),
    path('product/<int:pk>',views.product,name='product'),
    path('delete/<int:pk>',views.delete_inventory,name="delete_inventory")
    
]
