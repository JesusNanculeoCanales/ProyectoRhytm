document.addEventListener('DOMContentLoaded', function() {
    // Selecciona los elementos del DOM necesarios
    const loginButton = document.getElementById('btnLogin');
    const emailField = document.getElementById('emailModal');
    const passwordField = document.getElementById('passwordModal');

    // Agrega un evento de clic al botón de inicio de sesión
    loginButton.addEventListener('click', function(event) {
        const email = emailField.value;
        const password = passwordField.value;

        // Valida el formato del correo electrónico
        if (!validarFormatoCorreo(email)) {
            mostrarMensaje('Correo electrónico no válido.', 3000);  // Mensaje desaparece después de 3 segundos
            event.preventDefault();  // Previene el envío del formulario
        }

        // Verifica que la contraseña tenga al menos 8 caracteres
        if (password.length < 8) {
            mostrarMensaje('La contraseña debe tener al menos 8 caracteres.', 3000);  // Mensaje desaparece después de 3 segundos
            event.preventDefault();  // Previene el envío del formulario
        }
    });

    // Función para validar el formato del correo electrónico
    function validarFormatoCorreo(correo) {
        var patronCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return patronCorreo.test(correo);
    }

    // Función para mostrar mensajes de alerta
    function mostrarMensaje(mensaje, duracion = 5000) {  // Duración predeterminada de 5 segundos
        const alertContainer = document.createElement('div');
        alertContainer.className = 'alert alert-danger';
        alertContainer.role = 'alert';
        alertContainer.innerText = mensaje;

        // Inserta el mensaje de alerta al principio del cuerpo del modal
        const modalBody = document.querySelector('.modal-body');
        modalBody.insertBefore(alertContainer, modalBody.firstChild);

        // Elimina el mensaje después de la duración especificada
        setTimeout(() => {
            alertContainer.remove();
        }, duracion);
    }

    // Asegura que el modal de inicio de sesión se muestre si está presente en la página
    const modalElement = document.getElementById('staticBackdrop');
    if (modalElement.classList.contains('show')) {
        const modalInstance = new bootstrap.Modal(modalElement);
        modalInstance.show();
    }

    // Muestra los mensajes de error del servidor al cargar la página
    const serverMessages = document.querySelectorAll('.server-message');
    if (serverMessages.length > 0) {
        serverMessages.forEach(message => {
            mostrarMensaje(message.innerText, 5000);  // Mensaje desaparece después de 5 segundos
        });
    }
});