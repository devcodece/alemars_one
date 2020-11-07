from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def catalog_page(request):
    return render(request, 'catalog-page.html')