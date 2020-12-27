from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, Orderupdate
from math import ceil
import json


# Create your views here.
def index(request):
    products = Product.objects.all()  # Fetching products from database
    # print(products)

    allprods = []
    catprods = Product.objects.values('category', 'id')  # fetching categories
    # print(catprods)
    cats = {item['category'] for item in catprods}
    # print(cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        # print(prod)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1, nslides), nslides])

    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        # print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        #print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'shop/contact.html')


def tracker(request):
    return HttpResponse("tracker")

'''    if request.method == "POST":
        orderid = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderid, email=email)
            # print(update)
            if len(order) > 0:
                order = Orders.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'item': item.timestamp})
                    response = json.dumps(updates)
                    return HttpResponse(response)
            else:
                pass

        return render(request, 'shop/tracker.html') '''


def search(request):
    return render(request, 'shop/search.html')


def prodview(request, myid):
    # fetch the product using id
    product = Product.objects.filter(id=myid)
    # print(product) here product is list so we have to specify its index

    return render(request, 'shop/prodview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Orders(items_json=items_json, name=name, email=email,
                       address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = Orderupdate(order_id=order.order_id,
                             update_desc="The order has been placed")
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')
