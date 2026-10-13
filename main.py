import os
import telegram
# from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import bibfuncs
import botfuncs

token = os.environ.get("TELEGRAM_BOT_TOKEN")
if token is None:
    raise SystemExit("No se encontró la variable de entorno TELEGRAM_BOT_TOKEN. " \
    "Por favor, configúrala antes de ejecutar el script.")
biblia = bibfuncs.cargar_biblia()

print()
print("-------------------------------------")
print("Iniciando Bibot de Telegram...")
print(f"Versión de Telegram: {telegram.__version__}")
print(f"Token: {token}")

libro = biblia[0]

print("-------------------------------------")
print()
print(libro["chapters"][0][0])      # Génesis 1:1
print()
print("-------------------------------------")

# Crear la aplicación
app = Application.builder().token(token).build() # type: ignore

# Agregar manejadores de comandos y mensajes
app.add_handler(CommandHandler("start", botfuncs.start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, botfuncs.echo))

print("Bibot de Telegram iniciado. Esperando mensajes... para salir presiona Ctrl+C")

# Iniciar el bot
app.run_polling()

# finalizar el bot
print("Amén")
print()