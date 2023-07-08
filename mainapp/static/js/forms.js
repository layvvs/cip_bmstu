let authorCounter = 0;
let securityCounter = 0;

//Сделать так, чтобы данная функция срабатывала постоянно 


setInterval(function() {

    $(document).ready(function() {
        $('#date1').mask('00-00-0000');
        $('#date2').mask('00-00-0000');
        $('#date3').mask('00-00-0000');
        $('#date4').mask('00-00-0000');
        $('#date5').mask('00-00-0000');
        $('#date6').mask('00-00-0000');
        $('#date7').mask('00-00-0000');
        $('#date8').mask('00-00-0000');
        $('#date9').mask('00-00-0000');
        $('#date10').mask('00-00-0000');
        $('#date11').mask('00-00-0000');
      });

}, 1000);

function addAuthor(){
    authorCounter += 1;
    $(".new-authors-form").append(
        `<div class="mt-3 mb-1" id="author-${authorCounter}">
            <input type="text" class="form-control" name="authors-name" placeholder="ФИО" required>
            <input type="text" class="form-control mt-1" name="authors-unit" placeholder="Подразделение" required>
            <input type="text" class="form-control mt-1" name="authors-post" placeholder="Должность" required>
            <button type="button" class="btn btn-primary mt-3" name="remove-author-btn-${authorCounter}" onclick="removeAuthor(${authorCounter})">Удалить автора</button>
        </div>`
        );
}

function addSecurity(){
    securityCounter += 1;
    $(".new-security-form").append(
        `<div class="mt-3 mb-1" id="security-${securityCounter}">
            <input type="text" class="form-control mt-1" name="security-abroad" required>
            <button type="button" class="btn btn-primary mt-3" id="remove-author-btn-${securityCounter}" onclick="removeSecurity(${securityCounter})">Удалить поле</button>
        </div>`
        );
}


function removeAuthor(id){
    document.getElementById(`author-${id}`).remove();
}

function removeSecurity(id){
    document.getElementById(`security-${id}`).remove();
}

$("#select-service-proactive").on('click', function(ev){

    if ($('#select-service-proactive').val() == "Служебный"){
        $('#ser-proac-forms').replaceWith(
            '<div class="mt-3" id="ser-proac-forms">\
                <select class="form-control custom-select mt-1" name="select-type-service" required>\
                    <option selected>Распоряжение</option>\
                    <option>Приказ</option>\
                    <option>Служебное задание</option>\
                </select>\
                <input type="text" class="form-control mt-1" name="order-number" placeholder="Номер приказа" required>\
                <input type="text" class="form-control mt-1" name="contract-number" placeholder="Номер договора" required>\
            </div>'

        );
    }
    else{
        $('#ser-proac-forms').replaceWith(
            '<div class="mt-3" id="ser-proac-forms">\
                <input type="text" class="form-control mt-1" name="contract-number" placeholder="Номер договора" required>\
                <input type="text" class="form-control mt-1" id="date4" name="contract-date" placeholder="Дата договора" required>\
            </div>'
        );
    }
});

$("#type-of-contract").on('click', function(ev){

    if ($('#type-of-contract').val() == "Лицензионный договор"){
        $('#type-of-contract-forms').replaceWith(
            '<div class="mt-3" id="type-of-contract-forms">\
                <input type="text" class="form-control mt-1" id="date5" name="date-of-conclusion" placeholder="Дата заключения" required>\
                <input type="text" class="form-control mt-1" name="number" placeholder="Номер" required>\
                <input type="text" class="form-control mt-1" id="date6" name="date-of-registration" placeholder="Дата регистрации" required>\
                <input type="text" class="form-control mt-1" id="date7" name="due-date" placeholder="Срок оплаты" required>\
                <input type="text" class="form-control mt-1" name="payment" placeholder="Сумма оплаты" required>\
                <input type="text" class="form-control mt-1" id="date8" name="date-of-payment" placeholder="Дата оплаты" required>\
                <label for="license-agreement-1">Использование в уставном капитале</label> <br>\
                <div class="form-check form-check-inline">\
                    <input class="form-check-input" type="radio" name="license-agreement" id="license-agreement-1" value="Да" checked>\
                    <label class="form-check-label" for="license-agreement-1">Да</label>\
                </div>\
                <div class="form-check form-check-inline">\
                    <input class="form-check-input" type="radio" name="license-agreement" id="license-agreement-2" value="Нет">\
                    <label class="form-check-label" for="license-agreement-2">Нет</label>\
                </div>\
            </div>'
        );
    }
    else if ($('#type-of-contract').val() == "Договор отчуждения"){
        $('#type-of-contract-forms').replaceWith(
            '<div class="mt-3" id="type-of-contract-forms">\
                <input type="text" class="form-control mt-1" id="date9" name="date-of-conclusion" placeholder="Дата заключения" required>\
                <input type="text" class="form-control mt-1" name="number" placeholder="Номер" required>\
                <input type="text" class="form-control mt-1" id="date10" name="date-of-registration" placeholder="Дата регистрации" required>\
                <input type="text" class="form-control mt-1" name="payment" placeholder="Сумма оплаты" required>\
                <input type="text" class="form-control mt-1" id="date11" name="date-of-payment" placeholder="Дата оплаты" required>\
            </div>'
        );
    }
    else{
        $('#type-of-contract-forms').replaceWith(
            '<div id="type-of-contract-forms">\
            </div>'
        );
    }
});
