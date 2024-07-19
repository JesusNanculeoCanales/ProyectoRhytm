document.addEventListener('DOMContentLoaded', function() {
    // Al cargar el DOM, agrega un evento de clic al botón de alternar la barra lateral
    var sidebarToggle = document.getElementById('sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            // Alterna la visibilidad de la barra lateral
            var sidebar = document.getElementById('sidebar');
            if (sidebar.style.display === 'none' || sidebar.style.display === '') {
                sidebar.style.display = 'block'; // Muestra la barra lateral si está oculta
            } else {
                sidebar.style.display = 'none'; // Oculta la barra lateral si está visible
            }
        });
    }
});

// Funciones de validación

// Valida el formato del correo electrónico
function validarFormatoCorreo(correo) {
    var patronCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const resultado = patronCorreo.test(correo);
    if (!resultado) {
        toastTextoColor('Correo Inválido 😒', 2); // Muestra un mensaje de error si el formato del correo es incorrecto
    }
    return resultado; // Devuelve verdadero si el formato del correo es válido, de lo contrario falso
}

// Valida el formato de la contraseña
function validarClave(clave) {
    var patronClave = /^(?=.*[A-Z])(?=.*\d).{8,15}$/;
    const resultado = patronClave.test(clave);
    if (!resultado) {
        toastTextoColor('Contraseña Inválida 🥵', 2); // Muestra un mensaje de error si la contraseña es inválida
    }
    return resultado; // Devuelve verdadero si la contraseña es válida, de lo contrario falso
}

/* TOASTS */
// Variables para manejar los toasts
var texto_toast = document.getElementById('texto-toast');
var toast = document.getElementById('liveToast');

// Función para abrir un toast con el mensaje proporcionado
function abrirToast(texto) {
    toast.querySelector('.toast-body').textContent = texto;
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    var toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl);
    });
    toastList.forEach(toast => {
        toast.show(); // Muestra todos los toasts en la lista
    });
}

// Función para cambiar el color del toast
function toggleToastColor(numero) {
    if (numero == 1 && !toast.classList.contains('text-bg-success')) {
        toast.classList.remove('text-bg-danger');
        toast.classList.add('text-bg-success'); // Cambia el color a verde si el número es 1
    } else if (numero == 2 && !toast.classList.contains('text-bg-danger')) {
        toast.classList.remove('text-bg-success');
        toast.classList.add('text-bg-danger'); // Cambia el color a rojo si el número es 2
    }
}

// Función para mostrar un toast con el texto y el color especificados
function toastTextoColor(texto, color) {
    abrirToast(texto); // Muestra el toast con el texto proporcionado
    toggleToastColor(color); // Cambia el color del toast según el valor de color
}