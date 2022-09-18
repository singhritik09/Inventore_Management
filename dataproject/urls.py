
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dbapp.urls')),
    path('maxsale',include('dbapp.urls')),
    path('managers/',include('dbapp.urls')),
    path('department/',include('dbapp.urls')),
    path('add/',include('dbapp.urls')), 
    path('add_inventory',include('dbapp.urls')),
    path('inventory/',include('dbapp.urls')),
    
    path('product/<int:pk>',include('dbapp.urls')),
    path('delete/<int:pk>',include('dbapp.urls')),

]
