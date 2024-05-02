from django.shortcuts import redirect, render
from .models import Product,Inventory, Location

def product_list(request):
    products = Product.objects.all()
    location = Location.objects.all()
    inventory = Inventory.objects.all()
    return render(request, 'IMS_APP/product_list.html', {'products': products, 'location': location,'inventory': inventory})


# ADD Location ID
#ProcuctID , size  
def add_product(request):
    if request.method == 'POST':
        productId = request.POST.get('productId')
        size = request.POST.get('size')
        type = request.POST.get('type')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        
        locationid = request.POST.get('locationid')
        address = request.POST.get('address')
        state = request.POST.get('state')
        
        # Assuming Location model has fields locationid, address, state
        location = Location.objects.create(locationid=locationid, address=address, state=state)
        
        # Ensure the location object is saved before creating the Inventory object
        location.save()
        
        # Assuming Inventory model has fields locationid, productId, quantity
        Inventory.objects.create(locationid=location, productId=productId, quantity=quantity)
        
        # Assuming Product model has fields productId, size, type, price
        Product.objects.create(productId=productId, size=size, type=type, price=price)

        return redirect('product_list')
    return render(request, 'IMS_APP/add_product.html')

def location_info(request):
    location = Location.objects.all()
    return render(request, 'IMS_APP/location_info.html', {'location': location})
