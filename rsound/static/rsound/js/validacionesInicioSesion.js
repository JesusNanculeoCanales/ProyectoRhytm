document.addEventListener('DOMContentLoaded', function() {
  const loginButton = document.getElementById('btnLogin');
  const emailField = document.getElementById('emailModal');
  const passwordField = document.getElementById('passwordModal');

  loginButton.addEventListener('click', function(event) {
      const email = emailField.value;
      const password = passwordField.value;

      if (!validarFormatoCorreo(email)) {
          mostrarMensaje('Correo electrónico no válido.');
          event.preventDefault();
      }

      if (password.length < 8) {
          mostrarMensaje('La contraseña debe tener al menos 8 caracteres.');
          event.preventDefault();
      }
  });

  function validarFormatoCorreo(correo) {
      var patronCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return patronCorreo.test(correo);
  }

  function mostrarMensaje(mensaje) {
      const alertContainer = document.createElement('div');
      alertContainer.className = 'alert alert-danger';
      alertContainer.role = 'alert';
      alertContainer.innerText = mensaje;

      const modalBody = document.querySelector('.modal-body');
      modalBody.insertBefore(alertContainer, modalBody.firstChild);

      setTimeout(() => {
          alertContainer.remove();
      }, 3000);
  }

  const modalElement = document.getElementById('staticBackdrop');
  if (modalElement.classList.contains('show')) {
      const modalInstance = new bootstrap.Modal(modalElement);
      modalInstance.show();
  }
});