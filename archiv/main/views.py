from django.shortcuts import render,HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    return render(request,'home.html')
def select(request):
    items=Todo.objects.all
    # items=Todo.objects.

    return render(request,'select.html',{"items":items})
