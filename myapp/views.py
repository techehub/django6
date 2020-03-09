
from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template("home.html")
    data = {}
    res = template.render(data, request)
    return HttpResponse(res)
