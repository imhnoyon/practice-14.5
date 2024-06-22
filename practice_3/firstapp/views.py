from django.shortcuts import render
from . import forms
# Create your views here.
def home(request):
    data=forms.ExampleFrom()
    
    return render(request,'index.html',{'form':data})