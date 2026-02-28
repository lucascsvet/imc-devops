import pytest
from app import app

client = app.test_client()

@pytest.mark.parametrize("peso, altura, esperado", [
    (70, 175, "Peso normal"),
    (50, 175, "Abaixo do peso"),
    (85, 175, "Sobrepeso"),
    (110, 175, "Obesidade"),
])
def test_classificacoes(peso, altura, esperado):
    response = client.post("/imc", json={
        "peso": peso,
        "altura": altura
    })

    data = response.get_json()
    assert response.status_code == 200
    assert data["classificacao"] == esperado