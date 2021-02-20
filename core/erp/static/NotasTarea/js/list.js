
$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "tareaPre.id"},
            {"data": "tareaPre.tarea"},
            {"data": "tareaPre.user_creation.username"},
            {"data": "nota"},
            {"data": "observacion"},
            {"data": "observacion"},
        ],
        columnDefs: [
            {
                targets: [-5],
                class: 'text-center',
                orderable: false, 
                render: function (data, type, row) {
                    return buttons = '<a href="'+row.tareaPre.  tarea+'" class="btn btn-dark btn-xs btn-flat"><i class="fa fa-file-pdf"></i></a> '; 
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/notastarea/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/notastarea/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
