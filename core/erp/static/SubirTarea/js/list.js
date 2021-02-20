
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
            {"data": "tarea"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: false, 
                render: function (data, type, row) {
                    return buttons = '<a href="'+row.tarea+'" class="btn btn-dark btn-xs btn-flat"><i class="fa fa-file-pdf"></i></a> '; 
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/subirtarea/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/subirtarea/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
