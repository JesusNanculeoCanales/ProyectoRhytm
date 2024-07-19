const form_registro = document.getElementById("registroForm")  // Selecciona el formulario de registro
const btnregistro = document.getElementById("btnregistro")  // Selecciona el botón de registro

// Función principal para registrar un usuario
function registrarUsuario(elemento) {
  var formRegistroValido = true;  // Indicador de validación del formulario

  const nombre = document.getElementById('name').value;  // Obtiene el valor del campo nombre
  const apellido = document.getElementById('apellido').value;  // Obtiene el valor del campo apellido
  const nickname = document.getElementById('nickname').value;  // Obtiene el valor del campo nickname
  const telefono = document.getElementById('telefono').value;  // Obtiene el valor del campo telefono
  const email = document.getElementById('email').value;  // Obtiene el valor del campo email
  const password = document.getElementById('password').value;  // Obtiene el valor del campo contraseña
  const password2 = document.getElementById('password2').value;  // Obtiene el valor del campo repetir contraseña

  // Validación de campos vacíos
  if (!nombre || !apellido || !nickname || !telefono || !email || !password || !password2) {
    toastTextoColor('Campos Vacios 😅', 2)  // Muestra mensaje de campos vacíos
    formRegistroValido = false;
  } else {
    var validacionCorreo = true;
    var validacionClave = true;

    // Validación de longitud del nickname
    if (nickname.length < 3 && formRegistroValido) {
      toastTextoColor('Nickname menor a 3 caracteres 🥱', 2)  // Muestra mensaje si el nickname es menor a 3 caracteres
      formRegistroValido = false;
    } else if (nickname.length > 15) {
      toastTextoColor('Nickname mayor a 15 caracteres 🥱', 2)  // Muestra mensaje si el nickname es mayor a 15 caracteres
      formRegistroValido = false;
    }

    // Validación de la clave
    validacionClave = validarClave(password);  // Verifica la validez de la contraseña
    validacionCorreo = validarFormatoCorreo(email);  // Verifica la validez del correo electrónico

    // Validación de coincidencia de contraseñas
    if (password !== password2 && formRegistroValido) {
      toastTextoColor('Las contraseñas no coinciden 😘', 2)  // Muestra mensaje si las contraseñas no coinciden
      formRegistroValido = false;
    }

    // Enviar el formulario si todas las validaciones son correctas
    if (formRegistroValido && validacionClave && validacionCorreo) {
      aparecerCarga()  // Muestra spinner de carga
      toastTextoColor('Registrado 😘', 1)  // Muestra mensaje de éxito
      form_registro.submit()  // Envía el formulario
    }
  }
}

// Función para mostrar el spinner de carga
function aparecerCarga() {
  const spinner = document.getElementById("spinner")
  const fondo = document.getElementById("fondito")
  spinner.style.display = "block"
  fondo.style.display = "block"
  setTimeout(function () {
    spinner.style.display = "none"
    fondo.style.display = "none"
  }, 3000)  // Oculta el spinner después de 3 segundos
}

// Función para limitar la longitud del input
function limitarInput(maxLength) {
  if (this.value.length > maxLength) {
    this.value = this.value.slice(0, maxLength);  // Limita la longitud del input
  }
}

/* TOASTS */
var texto_toast = document.getElementById('texto-toast');  // Selecciona el contenedor del texto del toast
var toast = document.getElementById('liveToast');  // Selecciona el toast

// Función para abrir un toast
function abrirToast(texto) {
  toast.querySelector('.toast-body').textContent = texto;
  var toastElList = [].slice.call(document.querySelectorAll('.toast'))
  var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl)
  })
  toastList.forEach(toast => {
    toast.show()  // Muestra el toast
  })
}

// Función para cambiar el color del toast
function toggleToastColor(numero) {
  if (numero == 1 && !toast.classList.contains('text-bg-success')) {
    toast.classList.remove('text-bg-danger');
    toast.classList.add('text-bg-success');
  } else if (numero == 2 && !toast.classList.contains('text-bg-danger')) {
    toast.classList.remove('text-bg-success');
    toast.classList.add('text-bg-danger');
  }
}

// Función para mostrar el toast con el texto y color especificados
function toastTextoColor(texto, color) {
  abrirToast(texto)
  toggleToastColor(color);
}

// Función para validar el formato del correo
function validarFormatoCorreo(correo) {
  var patronCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const resultado = patronCorreo.test(correo);
  if (!resultado) {
    toastTextoColor('Correo Inválido 😒', 2)  // Muestra mensaje si el correo no es válido
  }
  return resultado;
}

// Función para validar la clave
function validarClave(clave) {
  var patronClave = /^(?=.*[A-Z])(?=.*\d).{8,15}$/;
  const resultado = patronClave.test(clave);
  if (!resultado) {
    toastTextoColor('Contraseña Inválida 🥵', 2)  // Muestra mensaje si la contraseña no es válida
  }
  return resultado;
}

// Función para alternar la visibilidad de la contraseña
function togglePasswordVisibility(id) {
  const input = document.getElementById(id);
  const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
  input.setAttribute('type', type);
}
