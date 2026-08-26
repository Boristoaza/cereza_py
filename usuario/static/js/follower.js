
// // funcion seguir usuario
// document.addEventListener('submit', function (event) {

//     console.log("SUBMIT DETECTADO");

//     if (!event.target.matches('#from_follower')) {
//         return;
//     }

//     console.log("FORMULARIO FOLLOWER DETECTADO");

//     event.preventDefault();

//     const formulario_follower = event.target;
//     const datos = new FormData(formulario_follower);

//     axios.post(formulario_follower.action, datos)
//         .then(response => {
//             console.log("RESPUESTA:");
//             console.log(response.data);
//         })
//         .catch(error => {
//             console.error("ERROR FATAL:", error);
//         });
// });

// funcion dejar de seguir usuario
// Función seguir usuario
document.addEventListener('submit', function (event) {

    console.log("SUBMIT DETECTADO");

    if (!event.target.matches('#from_follower')) {
        return;
    }

    console.log("FORMULARIO FOLLOWER DETECTADO");

    event.preventDefault();

    const formulario_follower = event.target;
    const datos = new FormData(formulario_follower);

    axios.post(formulario_follower.action, datos)
        .then(response => {
            console.log("RESPUESTA:");
            console.log(response.data);
        })
        .catch(error => {
            console.error("ERROR FATAL:", error);
        });
});


// Función dejar de seguir usuario
document.addEventListener('submit', function (event) {

    console.log("SE DETECTÓ EL SUBMIT");

    if (!event.target.matches("#form_eliminar_follow")) {
        return;
    }

    event.preventDefault();

    console.log("SE CANCELÓ EL SUBMIT");

    const formulario = event.target;
    const datos = new FormData(formulario);

    axios.post(formulario.action, datos)
        .then(response => {
            console.log("RESPUESTA:", response.data);
        })
        .catch(error => {
            console.error("Error al dejar de seguir:", error);
        });

});