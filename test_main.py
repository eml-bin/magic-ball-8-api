from fastapi.testclient import TestClient

from main import app  # Asegúrate de que tu archivo principal se llame main.py

# Cliente de prueba para ejecutar las pruebas
client = TestClient(app)


def test_read_root():
    """
    Prueba el endpoint raíz ('/').
    Verifica que la respuesta sea exitosa (código 200) y que el JSON
    contenga el saludo esperado.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"saludo": "MagicBall8 API. ¡Prueba tu suerte en /lucky!"}


def test_get_lucky_phrase():
    """
    Prueba el endpoint '/lucky'.
    Verifica que la respuesta sea exitosa (código 200) y que el JSON
    contenga la clave 'lucky_message'.
    """
    response = client.get("/lucky")
    assert response.status_code == 200
    data = response.json()
    # Verificamos que la clave exista en la respuesta
    assert "lucky_message" in data
    # Verificamos que el valor de la clave no esté vacío
    assert isinstance(data["lucky_message"], str)
    assert len(data["lucky_message"]) > 0
