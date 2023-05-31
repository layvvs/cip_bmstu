let counter = 0
$("#add-author-btn").on('click', function (ev){
    counter ++;
    $(".new-authors-form").append(
        `<div class="mt-3 mb-1">\
            <input type="text" class="form-control" id="authors-name-${counter}" placeholder="ФИО" required>\
            <input type="text" class="form-control mt-1" id="authors-unit-${counter}" placeholder="Подразделение" required>\
            <input type="text" class="form-control mt-1" id="authors-post-${counter}" placeholder="Должность" required>\
        </div>`
        );
});


$("#select-service-proactive").on('click', function(ev){

    if ($('#select-service-proactive').val() == "Служебный"){
        $('#ser-proac-forms').replaceWith(
            '<div class="mt-3" id="ser-proac-forms">\
                <select class="form-control custom-select mt-1" id="exampleFormControlSelect1" required>\
                    <option selected>Распоряжение</option>\
                    <option>Приказ</option>\
                    <option>Служебное задание</option>\
                </select>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Номер приказа" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Номер договора" required>\
            </div>'

        );
    }
    else{
        $('#ser-proac-forms').replaceWith(
            '<div class="mt-3" id="ser-proac-forms">\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Номер договора" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Дата договора" required>\
            </div>'
        );
    }
});

$("#type-of-contract").on('click', function(ev){

    if ($('#type-of-contract').val() == "Лицензионный договор"){
        $('#type-of-contract-forms').replaceWith(
            '<div class="mt-3" id="type-of-contract-forms">\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Дата заключения" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Номер" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Дата регистрации" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Срок оплаты" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Оплата" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Дата оплаты" required>\
                <label for="license-agreement-1">Использование в уставном капитале</label> <br>\
                <div class="form-check form-check-inline">\
                    <input class="form-check-input" type="radio" name="license-agreement" id="license-agreement-1" value="option1" checked>\
                    <label class="form-check-label" for="license-agreement-1">Да</label>\
                </div>\
                <div class="form-check form-check-inline">\
                    <input class="form-check-input" type="radio" name="license-agreement" id="license-agreement-2" value="option2">\
                    <label class="form-check-label" for="license-agreement-2">Нет</label>\
                </div>\
            </div>'
        );
    }
    else if ($('#type-of-contract').val() == "Договор отчуждения"){
        $('#type-of-contract-forms').replaceWith(
            '<div class="mt-3" id="type-of-contract-forms">\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Дата заключения" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Номер" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Дата регистрации" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Оплата" required>\
                <input type="text" class="form-control mt-1" id="formGroupExampleInput2" placeholder="Дата оплаты" required>\
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
