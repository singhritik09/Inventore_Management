from urllib import request
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import is_valid_path
from .models import Employee ,Inventory
from .forms import EmployeeForm

from django.contrib import messages
# Create your views here.

def index(request):
    all_employee=Employee.objects.all()
    
    return render(request,'index.html',{'all':all_employee})

def add(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            
        messages.success(request,('New Employee Added to database'))
        return redirect('index')
        # return render(request,'add.html',{})
    else:
        return render(request,'add.html',{})
    
def inventory(request):
    inventories=Inventory.objects.all()
    context={
        "title": "Inventory List",
        "inventories": inventories
    }
    return render(request,'inventory.html',context=context)

def per_product_view(request,pk):
    
    inventory=get_object_or_404(Inventory,pk=pk)
    
    context={
        'inventory':inventory
    }
    return render(request,"per_product.html",context=context)