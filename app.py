from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/imc", methods=["POST"])
def calcular_imc():
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

    return jsonify({
        "imc": round(imc, 2),
        "classificacao": classificacao
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
