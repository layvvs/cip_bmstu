from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="/authapp/login/")
def show_document(request: HttpRequest, id):
    document = IpcArchive.objects.get(id_archive=id)
    obj_type = document.f_id_object_type.object_type
    classification = document.f_id_object_type.classifications
    sec_type = document.f_id_object_type.f_id_type_of_security_doc.type_of_security_doc
    authors = [item.f_id_author for item in ConnectingAuthors.objects.filter(f_id_archive=id)]
    countries = [item.f_id_countries for item in ConnectingCountries.objects.filter(f_id_archive=id)]

    if document.f_official_or_initiative.official_or_initiative == "Служебный":
        off_or_init = OfficialPatentTable.objects.get(p_of_id_archive=id)
    else:
        off_or_init = InitiativePatentTable.objects.get(p_in_id_archive=id)

    context = {
        'document': document,
        'obj_type': obj_type,
        'classification': classification if classification else 'Нет',
        'sec_type': sec_type,
        'authors': authors,
        'countries': countries,
        'off_or_init': off_or_init,
    }
    return render(request, 'documentapp/show-document.html', context)
