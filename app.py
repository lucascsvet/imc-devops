from flask import Flask, request, jsonify, render_template, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter("imc_requests_total", "Total de requisições ao cálculo de IMC")
REQUEST_LATENCY = Histogram("imc_request_duration_seconds", "Tempo de resposta das requisições")


@app.route("/metrics")
def metrics():
    """Endpoint para métricas do Prometheus."""
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/imc", methods=["POST"])
def calcular_imc():
    with REQUEST_LATENCY.time():
        dados = request.get_json()
        peso = float(dados["peso"])
        altura = float(dados["altura"])
        imc = peso / ((altura / 100) ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        REQUEST_COUNT.inc()
        return jsonify({
            "imc": round(imc, 2),
            "classificacao": classificacao
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
