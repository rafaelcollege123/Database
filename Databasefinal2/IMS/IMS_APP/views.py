from django.shortcuts import redirect, render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'IMS_APP/product_list.html', {'products': products})


# ADD Location ID
#ProcuctID , size  
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        locationId = request.POST['locationId']
        
        Product.objects.create(name=name, description=description, price=price, quantity=quantity, location = locationId)
        return redirect('product_list')
    return render(request, 'IMS_APP/add_product.html')

def location_info(request):
    products = Product.objects.all()
    return render(request, 'IMS_APP/location_info.html', {'products': products})
