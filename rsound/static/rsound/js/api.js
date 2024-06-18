$(document).ready(function() {
    const feriados_container = document.getElementById('feriados_container')

    function api_feriados() {
        return new Promise(function (resolve, reject) {
            $.ajax({
                url: 'https://apis.digital.gob.cl/fl/feriados/2024',
                method: 'GET',
                success: function (response) {

                    for (var i = 0; i < response.length; i++) {
                        const fechaStr = convertirFechaATexto(response[i].fecha)

                        var nuevoDiv = document.createElement('div');

                        nuevoDiv.classList.add('feriado');
                        nuevoDiv.classList.add('card');
                        const numeracion = i + 1;
                        nuevoDiv.innerHTML = `
                        <p class="nombre-feriado">`+`(`+numeracion+`)`+response[i].nombre+`</p>
                        <p class="fecha-feriado">`+fechaStr+`</p>
                        `

                        feriados_container.appendChild(nuevoDiv)
                    }
                    resolve(true)
                },
                error: function (xhr, status, error) {
                    console.log('ERROR: ' + error)
                    reject(error)
                }
            });
        });
    }

    function convertirFechaATexto(fechaStr) {
        var meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
        var partesFecha = fechaStr.split("-");
        var annio = partesFecha[0];
        var mes = meses[parseInt(partesFecha[1]) - 1];
        var dia = partesFecha[2];
        return dia + " de " + mes + " de " + annio;
    }
    
    function probar_api() {
        api_feriados().then(function () {
        }).catch(function (error) {
            console.error('Error en api_feriados:', error);
        });
    }
    
    probar_api()
});


