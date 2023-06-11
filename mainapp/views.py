from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def main_index(request: HttpRequest):
    record = IpcArchive.objects
    context = {
        "counter": record.count(),
        "all_records": record.all(),
    }
    return render(request, 'mainapp/main-index.html', context)

def new_doc(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        feel_bd(data)

        messages.success(request, "Документ успешно добавлен в базу.")
        return redirect('/')
    return render(request, 'mainapp/new-doc.html')

def show_document(request: HttpRequest, id):
    document = IpcArchive.objects.get(id_archive=id)

    context = {
        'document': document
    }
    return render(request, 'mainapp/show-document.html', context)

def date_handler_input(date):
    return date[6:] + '-' + date[3:5] + '-' + date[:2]

def date_handler_output(date):
    return date[8:] + '-' + date[5:7] + '-' + date[0:4]

def feel_bd(data):
    data_id = {
        "Authors": [],
        "Countries": [],
        "ObjectType": "",
        "OfficialOrInitiative": "",
        "ExclusiveRights": "",
        "AWARD": [],
        "IPCARCHIVE": "",
    }

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
        case "База данных":
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
    temp = ObjectType.objects.get_or_create(object_type=type_of_object, 
                                  classifications=classification, 
                                  f_id_type_of_security_doc=TypeOfSecurityDoc.objects.get(p_id_type_of_security_doc=type_of_sec_doc))
    data_id["ObjectType"] = temp[0]

    # Exclusive_Rigths
    exclusive_rights = data["type-of-contract"]
    data_id["ExclusiveRights"] = ExclusiveRights. \
                                 objects. \
                                 get(exclusive_rights=exclusive_rights)

    #official or initiative
    serive_proactive = data["select-service-proactive"] # Добавить в главную таблицу
    data_id["OfficialOrInitiative"] = OfficialOrInitiative. \
                                       objects. \
                                       get(official_or_initiative=serive_proactive)


    #IPCARHCIVE
    temp = IpcArchive.objects.get_or_create(f_id_object_type=data_id["ObjectType"], 
                                            security_doc_num=data["protection-document-number"], 
                                            primary_name=data["primary-name"], 
                                            application_num=data["application-number"], 
                                            application_data=date_handler_input(data["application-date"]), 
                                            final_name=data["final-name"], 
                                            responsible_person=data["responsible-person"], 
                                            accounting_in_is=data["accounting"], 
                                            date_reg_is=date_handler_input(data["date-of-security-document"]), 
                                            next_poshlina_date=date_handler_input(data["next-payment"]),
                                            f_official_or_initiative=data_id["OfficialOrInitiative"], 
                                            f_id_exclusive_rights=data_id["ExclusiveRights"]) 
    data_id["IPCARCHIVE"] = temp[0]
    print(data_id)

    #official or initiative 2
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
        service.p_of_id_archive = data_id["IPCARCHIVE"]
        service.f_id_official_patent_type = OfficialPatentType.objects.get(p_id_official_patent_type=off_patent_type)
        service.of_award_order_num = data["order-number"]
        service.of_award_contract_num = data["contract-number"]
        service.save()
    else:
        initiative = InitiativePatentTable()
        initiative.p_in_id_archive = data_id["IPCARCHIVE"]
        initiative.in_contract_num = data["contract-number"]
        initiative.in_contract_date = date_handler_input(data["contract-date"])
        initiative.save()

    # AWARD and Agreements
    if exclusive_rights != "Нет":
        date_of_conclusion = date_handler_input(data["date-of-conclusion"])
        number = data["number"]
        date_of_registration = date_handler_input(data["date-of-registration"])
        payment = int(data["payment"])
        date_of_payment = date_handler_input(data["date-of-payment"])
        agreements = Agreements()
        award = Award()

        if exclusive_rights == "Договор отчуждения":
            agreements.ag_p_id_archive = data_id["IPCARCHIVE"]
            agreements.ag_date_of_conclusion = date_of_conclusion
            agreements.ag_date_of_registration = date_of_registration  
            agreements.ag_num = number
            agreements.authorized_capital = ""
            agreements.save()

            award.date_of_award = date_of_payment
            award.award_sum = payment
            award.award_term = None
            award.awa_order_num = number
            award.save()
        elif exclusive_rights == "Лицензионный договор":
            due_date = date_handler_input(data["due-date"])
            license_agreement = data["license-agreement"]

            agreements.ag_p_id_archive = data_id["IPCARCHIVE"]
            agreements.ag_date_of_conclusion = date_of_conclusion
            agreements.ag_date_of_registration = date_of_registration
            agreements.ag_num = number
            agreements.authorized_capital = license_agreement
            agreements.save()

            award.date_of_award = date_of_payment
            award.award_sum = payment
            award.award_term = due_date
            award.awa_order_num = number
            award.save()
        
        ConnectingAwards.objects.create(f_id_award=award, f_id_archive=data_id["IPCARCHIVE"])

    #authors
    names = data.getlist("authors-name")
    units = data.getlist("authors-unit")
    posts = data.getlist("authors-post")
    for i in range(len(names)):
        temp = Authors.objects.get_or_create(author=names[i], \
                                      division=units[i], \
                                      post=posts[i])
        data_id["Authors"].append(temp[0])

    # countries
    security_abroad = data.getlist("security-abroad")
    countries = []
    for i in range(len(security_abroad)):
        data_id["Countries"].append(Countries. \
                                    objects. \
                                    get_or_create(co_name=security_abroad[i])[0])

    for author in data_id["Authors"]:
        ConnectingAuthors.objects.create(f_id_archive=data_id["IPCARCHIVE"], f_id_author=author)
    
    for country in data_id["Countries"]:
        ConnectingCountries.objects.create(f_id_archive=data_id["IPCARCHIVE"], f_id_countries=country)
    
    data_id.clear()