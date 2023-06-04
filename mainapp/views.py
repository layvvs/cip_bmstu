from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def main_index(request: HttpRequest):
    counter = IpcArchive.objects.count()
    context = {
        'counter': counter
    }
    return render(request, 'mainapp/main-index.html', context)

def new_doc(request: HttpRequest):
    if request.method == "POST":
        print(request.POST)
        messages.success(request, 'Документ успешно добавлен в базу.')    
        return redirect('/')
    return render(request, 'mainapp/new-doc.html')
