// document.addEventListener("submit", function (event) {

//     const formulario = event.target;

//     if (!formulario.matches(".form_tab")) {
//         return;
//     }

//     event.preventDefault();

//     const datos = new FormData(formulario);

//     axios.post(formulario.action, datos)
//         .then(response => {

//             console.log(response.data);

//         })
//         .catch(error => {

//             console.error(error);

//         });

// });