import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Este endpoint devuelve un saludo de bienvenida."""
    return {"saludo": "MagicBall8 API. ¡Prueba tu suerte en /lucky!"}


# --- Endpoint 2: La frase de la suerte ---
@app.get("/lucky")
def get_lucky_phrase():
    """
    Este endpoint devuelve una frase aleatoria al estilo de una
    bola mágica de la suerte (Magic 8-Ball).
    """
    # 1. Lista de frases para nuestra "bola mágica"
    magic_phrases = [
        "Sí, definitivamente.",
        "Todo apunta a que sí.",
        "Sin duda.",
        "Puedes contar con ello.",
        "Como yo lo veo, sí.",
        "Es muy probable.",
        "Probablemente.",
        "Las perspectivas son buenas.",
        "Los signos apuntan a que sí.",
        "Respuesta dudosa, vuelve a intentar.",
        "Pregunta en otro momento.",
        "Mejor no decírtelo ahora.",
        "No puedo predecirlo en este momento.",
        "Concéntrate y vuelve a preguntar.",
        "No cuentes con ello.",
        "Mi respuesta es no.",
        "Mis fuentes dicen que no.",
        "Las perspectivas no son buenas.",
        "Muy dudoso.",
    ]

    # Usamos random.choice() para seleccionar una frase de la lista
    lucky_lucky = random.choice(magic_phrases)
    return {"lucky_message": lucky_lucky}
