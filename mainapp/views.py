from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def main_index(request: HttpRequest):
    counter = IpcArchive.objects.count()
    context = {
        "counter": counter
    }
    return render(request, 'mainapp/main-index.html', context)

def new_doc(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        feel_bd(data)

        messages.success(request, "Документ успешно добавлен в базу.")
        return redirect('/')
    return render(request, 'mainapp/new-doc.html')


def feel_bd(data):
    data_id = {
        "Authors": [],
        "Countries": [],
        "ObjectType": [],
        "OfficialOrInitiative": [],
        "OfficialPatentTable": [],
        "InitiativePatentTable": [],
        "Agreements": [],
        "AWARD": [],
        "IPCARCHIVE": [],
    }

    #authors
    names = data.getlist("authors-name")
    units = data.getlist("authors-unit")
    posts = data.getlist("authors-post")
    for i in range(len(names)):
        temp = Authors.objects.get_or_create(author=names[i], \
                                      division=units[i], \
                                      post=posts[i])
        data_id["Authors"].append(temp[0].p_id_author)

    # countries
    security_abroad = data.getlist("security-abroad")
    countries = []
    for i in range(len(security_abroad)):
        data_id["Countries"].append(Countries.\
                                    objects.\
                                    get_or_create(co_name=security_abroad[i])[0].p_id_countries)

    #object type (Пересмотреть суть)
    object_type_model = ObjectType()
    type_of_object = data["type-of-object"]
    type_of_sec_doc = ""
    classification = ""
    match type_of_object:
        case "Изобретение":
            type_of_sec_doc = 1
            classification = "МПК"
        case "Полезная модель":
            type_of_sec_doc = 1
            classification = "МПК"
        case "Промышленный образец":
            type_of_sec_doc = 1
            classification = "МКПО"
        case "Программа для ЭВМ":
            type_of_sec_doc = 2 
            classification = ""
        case "База Данных":
            type_of_sec_doc = 2
            classification = ""
        case "Ноу-хау":
            type_of_sec_doc = 3
            classification = ""
        case "Топология интегральных микросхем":
            type_of_sec_doc = 2
            classification = ""
        case "Товарный знак":
            type_of_sec_doc = 2
            classification = "МКТУ"
        case "Программа для ЭВМ и БД без регистрации":
            type_of_sec_doc = 3
            classification = ""
    object_type_model.object_type = type_of_object
    object_type_model.classifications = classification
    object_type_model.f_id_type_of_security_doc = type_of_sec_doc
    object_type_model.save()
    data_id["ObjectType"].append(object_type_model.p_id_object_type)

    #official or initiative
    serive_proactive = data["select-service-proactive"] # Добавить в главную таблицу
    data_id["OfficialOrInitiative"].append(OfficialOrInitiative.\
                                           objects.\
                                           get_or_create(OfficialPatentType=serive_proactive)[0].p_id_official_or_initiative)
    if serive_proactive == "Служебный":
        service = OfficialPatentTable()
        off_patent_type = ""
        match data["select-type-service"]:
            case "Распоряжение":
                off_patent_type = 1
            case "Приказ":
                off_patent_type = 2
            case "Служебное задание":
                off_patent_type = 3
        service.f_id_official_patent_type = off_patent_type
        service.of_award_order_num = data["order-number"]
        service.of_award_contract_num = data["contract-number"]
        service.save()
        data_id["OfficialPatentTable"].append(service.p_of_id_archive)
    else:
        initiative = InitiativePatentTable()
        initiative.in_contract_num = data["contract-number"]
        initiative.in_contract_date = data["contract-date"]
        initiative.save()
        data_id["InitiativePatentTable"].append(initiative.p_in_id_archive)


