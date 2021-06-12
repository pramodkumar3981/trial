from django.shortcuts import render,redirect
from .models import*
from django.core.files.storage import FileSystemStorage

# Create your views here.

# HOME PAGE
def home(request):
    return render(request,'home.html')
