from django.shortcuts import render
from .models import EmpForm #imported for EmpRegister

# Create your views here.
# from django.views.generic import TemplateView

def homef(request):
    return render(request,'home.html')

class EmpRegister(EmpForm):
    form_class=EmpForm
    template_name='addemp.html'
