from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def contactInfo(request):
    template= loader.get_template("contact.html")
    data= {}
    res= template.render(data, request)
    return HttpResponse(res)