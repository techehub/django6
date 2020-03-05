from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.


myproducts= {

    "111" : {"id":"111",
            "name": "samsung galexy s1",
            "desc": "Andriod phone",
            "price": 25000,
            "features": ["Andriod Phone",
                         "5 MP front camera",
                         "30 MP rear cam",
                         "5.5 Inch display"]
           }
    ,

    "222": {"id": "222",
            "name": "samsung galexy s2",
            "desc": "Andriod phone",
            "price": 25000,
            "features": ["Andriod Phone",
                         "5 MP front camera",
                         "30 MP rear cam",
                         "5.5 Inch display"]
            }

    ,

    "333": {"id": "333",
            "name": "samsung galexy s3",
            "desc": "Andriod phone",
            "price": 25000,
            "features": ["Andriod Phone",
                         "5 MP front camera",
                         "30 MP rear cam",
                         "5.5 Inch display"]
            }

}

def displayProduct (req, pid):
    print ("########",pid)
    template = loader.get_template("product.html")
    data =  myproducts[pid]

    res = template.render(data, req)
    return  HttpResponse(res)

def displayProductList(req):
    template = loader.get_template("productlist1.html")

    data = { "products" :myproducts}

    res = template.render(data, req)
    return HttpResponse(res)


