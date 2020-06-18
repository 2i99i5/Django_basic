from django.urls import path, re_path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    re_path(r'^products/$', mainapp.products, name='products'),
    # path('products/', mainapp.products, name='products'),
    path('contact/', mainapp.contact, name='contact'),
]
