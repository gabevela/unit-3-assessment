# Create your views here.
from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def delete(request):
  return HttpResponse('<h1>Are you sure you want to delete this Widget?</h1>')

