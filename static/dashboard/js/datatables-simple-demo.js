let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2,3] },//centrar contenido de las columnas
        { orderable: false, targets: [1,3] },//no se puede ordenar por acciones
        { searchable: false, targets: [0, ] }//no se puede buscar por el id
    ],
    pageLength: 4,
    destroy: true,
    language: {
        info: 'Mostrando página _PAGE_ de _PAGES_',
        infoEmpty: 'No hay registros disponibles',
        infoFiltered: '(filtrado de _MAX_ registros totales)',
        lengthMenu: 'Mostrar _MENU_ registros por página',
        zeroRecords: 'No se encontraron resultados - lo siento',
        paginate: {
            first: 'Primero',
            last: 'Último',
            previous: 'Anterior',
            next: 'Siguiente'
        },
        search: 'Buscar:',
    }
        
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listCategories();

    dataTable = $("#datatable-categories").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listCategories = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/adminCustom/getCategories");
        const data = await response.json();
        console.log(data);
        let content = ``;
        data.categories.forEach((categories, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${categories.id}</td>
                    <td>${categories.name_categories}</td>
                    <td>
                        <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button>
                        <button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button>
                    </td>
                </tr>`;
        });
        //Un id se puede referenciar solamenete con su nombre de id 
        tableBody_categories.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});