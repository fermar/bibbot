import os
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import bibfuncs

token = os.environ.get("TELEGRAM_BOT_TOKEN")
biblia = bibfuncs.cargar_biblia()

print("Iniciando Bibot de Telegram...")
print(f"Versión de Telegram: {telegram.__version__}")
print(f"Token: {token}")

# print(type(biblia))        # list o dict
# print(biblia[0].keys())    # si es una lista de libros
print("-------------------------------------")
libro = biblia[0]
print(libro["abbrev"], libro["name"])
print(type(libro["chapters"][0]))   # list
print(libro["chapters"][0][0])      # Génesis 1:1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    assert update.message is not None
    await update.message.reply_text("¡Hola! Soy tu Bibot de Telegram.")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"tu mensaje: {update.message.text}") # type: ignore

app = Application.builder().token(token).build() # type: ignore
app.add_handler(CommandHandler("start", start))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
print("Bibot de Telegram iniciado. Esperando mensajes... para salir presiona Ctrl+C")
app.run_polling()


print("Amén")
print()