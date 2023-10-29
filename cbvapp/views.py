from django.shortcuts import render
from django.views.generic import FormView, CreateView, ListView
from .models import Emp,EmpForm 

# Create your views here.

def homef(request):
    return render(request,'home.html')

class EmpRegister(FormView):
    form_class=EmpForm
    template_name='addemp.html'
    
    
class addEmp(CreateView):
    model=Emp
    fields='__all__'
    success_url='/'
    
class elist(ListView):
    model=Emp
    template_name='emplist.html'

