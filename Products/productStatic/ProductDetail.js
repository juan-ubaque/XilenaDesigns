function disminuirCantidad() {
    var quantityInput = document.getElementById("input-cuantity");
    var currentValue = parseInt(quantityInput.value, 10);
    if (currentValue > 1) {
        quantityInput.value = currentValue - 1;
    }
}

function aumentarCantidad() {
    var quantityInput = document.getElementById("input-cuantity");
    var currentValue = parseInt(quantityInput.value, 10);
    quantityInput.value = currentValue + 1;
}



// Añadir al carrito
const AddInCart = async (id,idcantidad) => {
    try {
        
        const cantidad = document.getElementById(idcantidad).value;

        if (cantidad <= 0) {
            Swal.fire({
                position: "top-end",
                icon: 'error',
                title: 'Ups... Algo salió mal',
                text: 'La cantidad debe ser mayor a 0',
                showConfirmButton: false,
                timer: 1500
            });
            return;
        }
        const response = await fetch(`/addInCart/${id}?cantidad=${cantidad}`, {
                method: "GET",
            });
            // Si el servidor responde con un redirect
            if (response.redirected) {
                window.location.href = response.url;
                return;
            }

            const data = await response.json();
            if (data.error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Ups... Algo salió mal',
                    text: data.error,
                });
            }else{

                Swal.fire({
                    position: "top-end",
                    icon: "success",
                    title: "Producto agregado al carrito.",
                    text: "El producto se agregó correctamente al carrito de compras.",
                    showConfirmButton: false,
                    timer: 1500
                    });
                
            }

        
    } catch (error) {
        Swal.fire({
            position: "top-end",
            icon: 'error',
            title: 'Ups... Algo salió mal',
            text: 'No tienes Conexión con el servidor',
            showConfirmButton: false,
                    timer: 1500
        });
    }
}


const AddInCartOneItem = async (id,cantidad) => {
    try {
        if (cantidad <= 0) {
            Swal.fire({
                position: "top-end",
                icon: 'error',
                title: 'Ups... Algo salió mal',
                text: 'La cantidad debe ser mayor a 0',
                showConfirmButton: false,
                timer: 1500
            });
            return;
        }
        const response = await fetch(`/addInCart/${id}?cantidad=${cantidad}`, {
                method: "GET",
            });
            // Si el servidor responde con un redirect
            if (response.redirected) {
                window.location.href = response.url;
                return;
            }

            const data = await response.json();
            if (data.error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Ups... Algo salió mal',
                    text: data.error,
                });
            }else{

                Swal.fire({
                    position: "top-end",
                    icon: "success",
                    title: "Producto agregado al carrito.",
                    text: "El producto se agregó correctamente al carrito de compras.",
                    showConfirmButton: false,
                    timer: 1500
                    });
                
            }

        
    } catch (error) {
        Swal.fire({
            position: "top-end",
            icon: 'error',
            title: 'Ups... Algo salió mal',
            text: 'No tienes Conexión con el servidor',
            showConfirmButton: false,
                    timer: 1500
        });
    }
}