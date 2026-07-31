import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
from scheduler import iniciar_scheduler

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! O bot está funcionando corretamente."
    )


def main():
    if not TOKEN:
        print("Erro: BOT_TOKEN não foi configurado.")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot iniciado...")
    iniciar_scheduler()
    app.run_polling()


if name == "main":
    main()
