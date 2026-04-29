document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("formulario");
    const resposta = document.getElementById("resposta");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        resposta.innerText = "Enviando...";

        const formData = new FormData(form);

        fetch(window.location.origin + "/enviar", {
            method: "POST",
            body: formData
        })
        .then(res => res.text())
        .then(() => {
            resposta.innerText = "✅ Enviado!";
            form.reset();
        })
        .catch(err => {
            console.error(err);
            resposta.innerText = "❌ Erro!";
        });
    });

});