# Create your views here.
from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request): #,widgets

    return render(request, 'home.html' )

#, { 'widgets' : widgets }

def add(request):
    print("thank you for submitting a widget")
    return render(request, 'home.html')

def delete(request):
    return render(request, 'delete.html')
