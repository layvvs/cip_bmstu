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
        data = request.POST
        feel_bd(data)

        messages.success(request, 'Документ успешно добавлен в базу.')
        return redirect('/')
    return render(request, 'mainapp/new-doc.html')


def feel_bd(data):
    #authors
    names = data.getlist('authors-name')
    units = data.getlist('authors-unit')
    posts = data.getlist('authors-post')
    # add uniqueness check     
    for i in range(len(names)):
        author = Authors()

        author.author = names[i]
        author.division = units[i]
        author.post = posts[i]
        author.save()
