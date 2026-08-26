document.addEventListener("shown.bs.modal", function (event) {

    const modal = event.target;

    const contenedorComentario =
        modal.querySelector("#lista_comentarios");

    const idPost = modal.id.replace("exampleModal", "");

    contenedorComentario.innerHTML = `
        <div class="spinner_comentarios">
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Cargando...</span>
            </div>
        </div>
    `;

    axios.get(`/comentarios/ver_comentarios/${idPost}/`)
        .then(response => {

            console.log("Comentarios:ññññ", response.data);

            const datos = response.data[0];

            contenedorComentario.innerHTML = "";

            datos.comentarios.forEach(comentario => {
                contenedorComentario.innerHTML += `
                    <div class="comentario">

                        <img
                            class="comentario_avatar"
                            src="/media/${comentario.avatar}"
                        >

                        <div class="comentario_contenido">

                            <div class="comentario_texto">
                                <strong>
                                    ${comentario.nombre_usuario}
                                </strong>

                                <span>
                                    ${comentario.comentario}
                                </span>
                            </div>

                            <div class="comentario_info">
                                Me gusta
                            </div>

                        </div>

                    </div>
                `;

            });

        })
        .catch(error => {

            console.error("Error al obtener comentarios:", error);

            contenedorComentario.innerHTML = `
                <div class="error_comentarios">
                    <p>No se pudieron cargar los comentarios.</p>
                </div>
            `;

        });

});

document.addEventListener("submit", function (event) {

    if (!event.target.matches("#form_comentar")) {
        return;
    }

    event.preventDefault();

    const formulario = event.target;
    const datos = new FormData(formulario);

    axios.post(formulario.action, datos)

        .then(response => {

            console.log("Comentario enviado:", response.data);

            const comentario = response.data.comentario;

            const modal = formulario.closest(".modal");

            const contenedorComentario =
                modal.querySelector("#lista_comentarios");

            contenedorComentario.innerHTML += `
                <div class="comentario">
                    <p>${comentario}</p>
                </div>
            `;

            formulario.reset();

        })

        .catch(error => {

            console.error("Error al enviar comentario:", error);

        });

});