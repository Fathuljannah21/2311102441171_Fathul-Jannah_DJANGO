from django.shortcuts import render
from berita.models import Artikel, Kategori
from django.http import HttpResponse

def home(request):
    template_name = 'halaman/index.html'
    data_artikel = Artikel.objects.all()
    data_kategori = Kategori.objects.all()
    context = {
        'title' : 'Selamat Datang',
        'data_artikel' : data_artikel,
        'data_kategori': data_kategori,
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title' : 'about me',
        'welcome' : 'ini page about',
    }
    return render(request, template_name, context)