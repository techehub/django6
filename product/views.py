from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product

# Create your views here.


def displayProduct (req, pid):
    print ("########",pid)

    template = loader.get_template("product.html")
    pdata=Product.objects.get(id=pid)
    data =  { "id": pdata.id,
              "name": pdata.name,
              "desc": pdata.description,
              "price": pdata.price}

    res = template.render(data, req)
    httpResponse=  HttpResponse(res)

    pids=""
    ids= req.COOKIES.get("PIDS")
    if ids!= None:
        pids=ids
    pids=pids + "|"+ pid

    httpResponse.set_cookie("PIDS", pids)
    return httpResponse;

def displayProductList(req):
    template = loader.get_template("productlist.html")
    data = { "products" :Product.objects.all()}
    res = template.render(data, req)
    return HttpResponse(res)


def addToCart (request):
    pid = request.GET['pid']
    qty = request.GET['qty']
    cartItems = {}
    if request.session.__contains__("cart"):
        cartItems = request.session.__getitem__('cart')

    cartItems[pid] = qty
    #request.session['cart'] = cartItems
    request.session.__setitem__("cart", cartItems)
    print (cartItems)
    return HttpResponse("Added Item to Cart")




