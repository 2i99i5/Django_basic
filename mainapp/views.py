from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    locations = [
        {
            'phone': '1900 - 1234 - 5678',
            'email': 'info@interior.com',
            'address': '12 W 1st St, 90001 Los Angeles, California',
            'city': 'California',
        },
        {
            'phone': '7495 - 0000 - 1111',
            'email': 'msc@interior.com',
            'address': '10 Chelyuskin St, 10000 Moscow, Russia',
            'city': 'Moscow',
        },
        {
            'phone': '7812 - 0000 - 1111',
            'email': 'spb@interior.com',
            'address': '55 Lenina St, 20000 Saint-Petersburg, Russia',
            'city': 'Saint-Petersburg',
        },
    ]
    context = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    context = {
        'page_title': 'каталог',
    }
    return render(request, 'mainapp/products.html', context)
