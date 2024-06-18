document.addEventListener('DOMContentLoaded', function() {
    var sidebarToggle = document.getElementById('sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            var sidebar = document.getElementById('sidebar');
            if (sidebar.style.display === 'none' || sidebar.style.display === '') {
                sidebar.style.display = 'block';
            } else {
                sidebar.style.display = 'none';
            }
        });
    }

    var formLogin = document.getElementById('formLogin');
    if (formLogin) {
        formLogin.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario
            
            // Obtener valores del formulario
            const email = document.getElementById('emailModal').value;
            const password = document.getElementById('passwordModal').value;
            
            // Validar Correo y Clave
            const validacionCorreo = validarFormatoCorreo(email);
            const validacionClave = validarClave(password);
            
            // Simular el inicio de sesión si ambas validaciones son correctas
            if (validacionCorreo && validacionClave) {
                // Mostrar mensaje de éxito
                document.getElementById('loginMessageModal').style.display = 'block';
                // Redirigir a la página de inicio después de 2 segundos
                setTimeout(function() {
                    window.location.href = "../Index.html";
                }, 2000);
            } else {
                alert('Por favor, completa todos los campos correctamente.');
            }
        });
    }
});

// Funciones de validación
function validarFormatoCorreo(correo) {
    var patronCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const resultado = patronCorreo.test(correo);
    if (!resultado) {
        toastTextoColor('Correo Inválido 😒', 2);
    }
    return resultado;
}

function validarClave(clave) {
    var patronClave = /^(?=.*[A-Z])(?=.*\d).{8,15}$/;
    const resultado = patronClave.test(clave);
    if (!resultado) {
        toastTextoColor('Contraseña Inválida 🥵', 2);
    }
    return resultado;
}

/* TOASTS */
var texto_toast = document.getElementById('texto-toast');
var toast = document.getElementById('liveToast');
function abrirToast(texto) {
    toast.querySelector('.toast-body').textContent = texto;
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    var toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl);
    });
    toastList.forEach(toast => {
        toast.show();
    });
}

function toggleToastColor(numero) {
    if (numero == 1 && !toast.classList.contains('text-bg-success')) {
        toast.classList.remove('text-bg-danger');
        toast.classList.add('text-bg-success');
    } else if (numero == 2 && !toast.classList.contains('text-bg-danger')) {
        toast.classList.remove('text-bg-success');
        toast.classList.add('text-bg-danger');
    }
}

function toastTextoColor(texto, color) {
    abrirToast(texto);
    toggleToastColor(color);
}