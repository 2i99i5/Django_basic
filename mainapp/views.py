from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def products(request):
    return render(request, 'mainapp/products.html')


def chair001(request):
    return render(request, 'mainapp/chair001.html')
