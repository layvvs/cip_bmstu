from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def main_index(request: HttpRequest):
    return render(request, 'mainapp/main-index.html')
