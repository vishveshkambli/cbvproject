from django.shortcuts import render

# Create your views here.

def homef(request):
    return render(request,'home.html')
