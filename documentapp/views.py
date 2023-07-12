from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainapp.views import date_handler_input


def get_document_data(id: int) -> tuple:
    document = IpcArchive.objects.get(id_archive=id)
    obj_type = document.f_id_object_type.object_type
    classification = document.f_id_object_type.classifications
    sec_type = document.f_id_object_type.f_id_type_of_security_doc.type_of_security_doc
    connecting_authors = [item for item in ConnectingAuthors.objects.filter(f_id_archive=id)]
    connecting_countries = [item for item in ConnectingCountries.objects.filter(f_id_archive=id)]

    if ConnectingAwards.objects.filter(f_id_archive=id).exists():
        connecting_award = ConnectingAwards.objects.get(f_id_archive=id)
    else: 
        connecting_award = None
    if Agreements.objects.filter(ag_p_id_archive=id).exists():
        agreements = Agreements.objects.get(ag_p_id_archive=id)
    else:
        agreements = None

    if document.f_official_or_initiative.official_or_initiative == "Служебный":
        off_or_init = OfficialPatentTable.objects.get(p_of_id_archive=id)
    else:
        off_or_init = InitiativePatentTable.objects.get(p_in_id_archive=id)
    
    return (document, obj_type, classification, sec_type, connecting_authors, connecting_countries, connecting_award, agreements, off_or_init)

@login_required(login_url="/authapp/login/")
def show_document(request: HttpRequest, id: int):
    data = get_document_data(id)
    authors = [item.f_id_author for item in data[4]]
    countries = [item.f_id_countries for item in data[5]]
    award = data[6].f_id_award if data[6] else None

    context = {
        'document': data[0],
        'obj_type': data[1],
        'classification': data[2] if data[2] else 'Нет',
        'sec_type': data[3],
        'authors': authors,
        'countries': countries,
        'off_or_init': data[8],
        'award': award if award else None,
        'agreements': data[7] if data[7] else None,
    }
    return render(request, 'documentapp/show-document.html', context)

@login_required(login_url="/authapp/login/")
def delete_document(request: HttpRequest, id):
    data = get_document_data(id)
    for author in data[4]:
        author.delete()
    for country in data[5]:
        country.delete()
    data[6].delete()
    data[7].delete()
    data[8].delete()
    data[0].delete()

    messages.success(request, "Документ успешно удален.")
    return redirect('/')

@login_required(login_url="/authapp/login/")
def edit_document(request: HttpRequest, id):
    if request.method == "POST":
        data = request.POST
        document = IpcArchive.objects.get(id_archive=id)
        document.primary_name = data['primary-name']
        document.final_name = data['final-name']
        document.security_doc_num = data['protection-document-number']
        document.application_num = data['application-number']
        document.application_data = date_handler_input(data['application-date'])
        document.responsible_person = data['responsible-person']
        document.accounting_in_is = data['accounting']
        document.date_reg_is = date_handler_input(data['date-of-security-document'])
        document.next_poshlina_date = date_handler_input(data['next-payment'])
        document.royalty_payment = data['reward-payment']
        document.security_document_payment = data['sec-doc-pay']
        document.save()
        return redirect(f'/document/{id}')
    document = IpcArchive.objects.get(id_archive=id)
    context = {
        'document': document
    }
    return render(request, 'documentapp/edit-document.html', context)
