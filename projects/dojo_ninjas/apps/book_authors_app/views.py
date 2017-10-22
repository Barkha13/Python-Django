from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print "in index"
    response = "This is the books app....!!!!"
    return HttpResponse(response)
