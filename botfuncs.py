import random

from telegram import Update
from telegram.ext import ContextTypes

# Función para manejar el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.message is not None
    await update.message.reply_text(
        "¡Hola! Soy Bibot.\n"
        "Puedo ayudarte a buscar versículos de la Biblia.\n"
        "Escribe un versículo o una palabra clave y te responderé con el texto correspondiente."
    )

# Devuelve el mismo mensaje que recibe
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"tu mensaje: {update.message.text}") # type: ignore

# Devuelve un versículo aleatorio de la Biblia
async def random_verse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cant_libros = len(context.bot_data["biblia"])
    rnd_libro = random.randint(0, cant_libros - 1)
    libro = context.bot_data["biblia"][rnd_libro]
    rnd_capitulo = random.randint(0, len(libro["chapters"]) - 1)
    capitulo = libro["chapters"][rnd_capitulo]
    rnd_versiculo = random.randint(0, len(capitulo) - 1)
    versiculo = capitulo[rnd_versiculo]
    await update.message.reply_text(f"Libro: {libro['name']}, Capítulo: {rnd_capitulo + 1}, Versículo: {rnd_versiculo + 1}") # type: ignore
    await update.message.reply_text(f"{versiculo}") # type: ignore

# Devuelve información sobre la Biblia
async def bibinfo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cant_libros = len(context.bot_data["biblia"])
    assert update.message is not None
    await update.message.reply_text(
        "Información sobre la Biblia:\n"
        "- Versión: RVR1960\n"
        "- Idioma: Español\n"
        "- Contenido: Texto completo de la Biblia\n"
        f"- Cantidad de libros: {cant_libros}"
    )
