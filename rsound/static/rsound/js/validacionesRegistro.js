const form_registro = document.getElementById("registroForm")
const btnregistro = document.getElementById("btnregistro")

function registrarUsuario(elemento) {
  var formRegistroValido = true;

  const nombre = document.getElementById('name').value;
  const apellido = document.getElementById('apellido').value;
  const nickname = document.getElementById('nickname').value;
  const telefono = document.getElementById('telefono').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const password2 = document.getElementById('password2').value;

  // Validación de Vacios
  if (!nombre || !apellido || !nickname || !telefono || !email || !password || !password2) {
    toastTextoColor('Campos Vacios 😅', 2)
    formRegistroValido = false;
  } else {
    var validacionCorreo = true;
    var validacionClave = true;

    // Validación de Nickname
    if (nickname.length < 3 && formRegistroValido) {
      toastTextoColor('Nickname menor a 3 caracteres 🥱', 2)
      formRegistroValido = false;
    } else if (nickname.length > 15) {
      toastTextoColor('Nickname mayor a 15 caracteres 🥱', 2)
      formRegistroValido = false;
    }

    // Validación de Clave (1 Digito, 1 Mayuscula, 8 - 15 caracteres)
    validacionClave = validarClave(password);
    // Validación de Correo
    validacionCorreo = validarFormatoCorreo(email);

    // Validación de Clave
    if (password !== password2 && formRegistroValido) {
      toastTextoColor('Las contraseñas no coinciden 😘', 2)
      formRegistroValido = false;
    }

    // "ENVIAR" FORMULARIO
    if (formRegistroValido && validacionClave && validacionCorreo) {
      aparecerCarga()
      toastTextoColor('Registrado 😘', 1)
      form_registro.submit()
    }
  }
}

function aparecerCarga() {
  const spinner = document.getElementById("spinner")
  const fondo = document.getElementById("fondito")
  spinner.style.display = "block"
  fondo.style.display = "block"
  setTimeout(function () {
    spinner.style.display = "none"
    fondo.style.display = "none"
  }, 3000)
}

function limitarInput(maxLength) {
  if (this.value.length > maxLength) {
    this.value = this.value.slice(0, maxLength);
  }
}

/* TOASTS */
var texto_toast = document.getElementById('texto-toast');
var toast = document.getElementById('liveToast');
function abrirToast(texto) {
  toast.querySelector('.toast-body').textContent = texto;
  var toastElList = [].slice.call(document.querySelectorAll('.toast'))
  var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl)
  })
  toastList.forEach(toast => {
    toast.show()
  })
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
  abrirToast(texto)
  toggleToastColor(color);
}

function validarFormatoCorreo(correo) {
  var patronCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const resultado = patronCorreo.test(correo);
  if (!resultado) {
    toastTextoColor('Correo Inválido 😒', 2)
  }
  return resultado;
}

function validarClave(clave) {
  var patronClave = /^(?=.*[A-Z])(?=.*\d).{8,15}$/;
  const resultado = patronClave.test(clave);
  if (!resultado) {
    toastTextoColor('Contraseña Inválida 🥵', 2)
  }
  return resultado;
}

function togglePasswordVisibility(id) {
  const input = document.getElementById(id);
  const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
  input.setAttribute('type', type);
}
