from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import *

def main_index(request: HttpRequest):
    counter = IpcArchive.objects.count()
    context = {
        'counter': counter
    }
    return render(request, 'mainapp/main-index.html', context)

def new_doc(request: HttpRequest):
    return render(request, 'mainapp/new-doc.html')

