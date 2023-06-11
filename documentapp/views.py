from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def show_document(request: HttpRequest, id):
    document = IpcArchive.objects.get(id_archive=id)

    context = {
        'document': document
    }
    return render(request, 'documentapp/show-document.html', context)
