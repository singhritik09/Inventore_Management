from multiprocessing import context
from urllib import request
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import is_valid_path
from requests import delete

from .models import Employee ,Inventory, Managers,Department
from .forms import EmployeeForm, InventoryForm,UpdateInventoryForm

from django.contrib import messages


# Create your views here.

def index(request):
    all_employee=Employee.objects.raw("SELECT e.id,e.name,d.pname FROM Employee as e LEFT JOIN Department as d ON e.did=d.pid")
    return render(request,'index.html',{'all':all_employee})

def managers(request):
    all_managers=Managers.objects.raw("SELECT * FROM Managers")
    
    return render(request,"managers.html",{'all':all_managers})

def department(request):
    all_dept=Department.objects.raw("SELECT * from Department")
    return render(request,"department.html",{'all':all_dept})
    
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

def add_inventory(request):
    
    if request.method=='POST':
        form=InventoryForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('Item successfully added to Inventory'))
        return redirect('inventory')
    else:
        return render(request,'add_inventory.html',{})


def inventory(request):
    inventories=Inventory.objects.all()
    context={
        "title": "Inventory List",
        "inventories": inventories
    }
    return render(request,'inventory.html',context=context)

def product(request,pk):
    
    inventory=get_object_or_404(Inventory, pk=pk)
    
    context={
        'inventory':inventory
    }
    return render(request,"product.html",context=context)

def delete_inventory(request,pk):
    inventory=get_object_or_404(Inventory,pk=pk)
    inventory.delete()
    
    return redirect('inventory')


def update_inventory(request,up_id):
    inventory=Inventory.objects.get(pk=up_id)
    form=InventoryForm(data=request.POST or None,instance=inventory)
    if form.is_valid():
        print(inventory.cost)
        print("Check")
        form.save()
        return redirect('inventory')
        

        
    context = {'form': form, 'inventory': inventory}
    print("Last part")
    return render(request, 'update_inventory.html', context=context)

