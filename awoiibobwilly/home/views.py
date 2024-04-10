from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    homeresponse = "Welcome to Awoii Bob Willy Website"
    resp = HttpResponse(homeresponse)
    return resp
