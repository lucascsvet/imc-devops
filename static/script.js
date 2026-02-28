function calcular() {
    const peso = document.getElementById("peso").value;
    const altura = document.getElementById("altura").value;

    fetch("/imc", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ peso: peso, altura: altura })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("resultado").innerText =
            "IMC: " + data.imc + " - " + data.classificacao;
    });
}
