function buscadorBuscar(elemento){
    toastTextoColor('En Desarrollo 🥵',2);
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
