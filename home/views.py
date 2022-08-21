from django.shortcuts import render


# Create your views here.
def index(request):
    """A view to render the homepage"""
    return render(request, 'home/index.html')
