
$(document).ready(function() {
    $('input[type="checkbox"][id^="price-"]').on('change', function() {
        updateProducts();
    });

    $('input[type="checkbox"][id^="color-"]').on('change', function() {
        updateProducts();
    });

    $('input[type="checkbox"][id^="size-"]').on('change', function() {
        updateProducts();
    });

    function updateProducts() {
        var selectedPrices = $('input[type="checkbox"][id^="price-"]:checked').map(function() {
            return this.value;
        }).get();
        
        var selectedColors = $('input[type="checkbox"][id^="color-"]:checked').map(function() {
            return this.value;
        }).get();
        
        var selectedSizes = $('input[type="checkbox"][id^="size-"]:checked').map(function() {
            return this.value;
        }).get();

        $.ajax({
            type: 'GET',
            url: '{% url "home" %}',  // Ajusta esto según tu URL de la vista
            data: {
                category: '{{ request.GET.category }}',  // Puedes necesitar ajustar esto según tu lógica
                color: selectedColors,
                size: selectedSizes,
                page: '{{ productos.number }}'  // Ajusta esto según tu lógica
            },
            success: function(data) {
                $('#productos-container').html(data.html_content);
            },
            error: function() {
                console.log('Error en la solicitud AJAX');
            }
        });
    }
});
