from django.shortcuts import render
# from .models import name,description,ratings,images


def homepage(request):
    return render(request, 'store/index.html')

# Create your views here.
