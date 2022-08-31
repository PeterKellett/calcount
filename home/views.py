from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """A view to render the homepage"""
    return render(request, 'home/index.html')


@login_required
def search(request):
    return render(request, 'home/search.html')
