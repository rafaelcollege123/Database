from django.shortcuts import redirect, render
from .models import Product,Inventory, Location

def product_list(request):
    products = Product.objects.all()
    location = Location.objects.all()
    inventory = Inventory.objects.all()
    return render(request, 'IMS_APP/product_list.html', {'products': products, 'locations': location,'inventorys': inventory})


# ADD Location ID
#ProcuctID , size  
def add_product(request):
    if request.method == 'POST':
        productid = request.POST.get('productid')
        size = request.POST.get('size')
        type = request.POST.get('type')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        
        locationid = request.POST.get('locationid')
        address = request.POST.get('address')
        state = request.POST.get('state')
        
    # For Product
        product, created = Product.objects.get_or_create(productid=productid, defaults={'size': size, 'type': type, 'price': price})

    # For Location
        location, created = Location.objects.get_or_create(locationid=locationid, defaults={'address': address, 'state': state})

        Inventory.objects.create(locationid=location, productid=product, quantity=quantity)



        return redirect('product_list')
    return render(request, 'IMS_APP/add_product.html')

def location_info(request):
    locations = Location.objects.all()
    return render(request, 'IMS_APP/location_info.html', {'locations': locations})
