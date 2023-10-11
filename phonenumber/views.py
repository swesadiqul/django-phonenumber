from django.shortcuts import render
from .forms import *


# Create your views here.
def home(request):
    forms = RegistrationForm()
    return render(request, 'index.html', {'forms': forms})