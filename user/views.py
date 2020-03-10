from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Contact
# Create your views here.


def contactInfo(request):
    template= loader.get_template("contact.html")
    data= {}
    res= template.render(data, request)
    return HttpResponse(res)

def savecontact (request):
    vals= request.GET
    c= Contact(firstName=vals["fname"], lastName=vals["lname"],
               mobile= vals["mobile"], email=vals["emailId"])
    c.save()

    return HttpResponse("success")