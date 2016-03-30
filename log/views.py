from django.shortcuts import render
from .models import Calculator

# Create your views here.
def calculator_list(request):
    posts = Calculator.objects.all()
    return render(request, 'log/calculator_list.html', {'posts': posts})