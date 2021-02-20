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
            {"data": "fecha"},
            {"data": "periodo"},
            {"data": "cur.nivel"},
            {"data": "cur.Paralelo"},
            {"data": "user_creation.username"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/matricula/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/matricula/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    buttons += '<a href="/erp/matricula/pdf/'+row.id+'/" target="_blank" type="button" class="btn btn-info btn-xs btn-flat"><i class="fas fa-file-pdf"></i></a>';
                    return buttons;
                }
                
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
