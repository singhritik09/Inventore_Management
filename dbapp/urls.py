from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('maxsale/',views.max_sale,name="maxsale"),
    path('department/',views.department,name="department"),
    path('managers/',views.managers,name="managers"),
    path('add',views.add,name="add"),
    path('add_inventory',views.add_inventory,name="add_inventory"),
    path('inventory',views.inventory,name="inventory"),
    path('product/<int:pk>',views.product,name='product'),
    path('delete/<int:pk>',views.delete_inventory,name="delete_inventory"),
    path('update_inventory/<up_id>',views.update_inventory,name="update_inventory"),

    
    
    

]
