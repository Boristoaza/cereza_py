document.addEventListener("submit", function (event) {

    const formulario_like = event.target;

    console.log("Submit detectado");

    if (!formulario_like.matches(".form_like")) {
        return;
    }

    event.preventDefault();

    console.log("Formulario like detectado");

    const datos = new FormData(formulario_like);

    axios.post(formulario_like.action, datos)
        .then(response => {

            console.log(response.data);
            console.log(response.data.like);
            console.log(response.data.usuario);

        })
        .catch(error => {
            console.error(error);
        });

});