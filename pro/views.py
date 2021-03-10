from django.shortcuts import render
from .models import *

# index page
def index(request):
    context = {}
    return render(request,'pro/index.html', context)
