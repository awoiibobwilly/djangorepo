from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def aboutus(request):
    template = loader.get_template ('aboutus.html')
    return HttpResponse(template.render())


