import os
import asyncio
from run_status import get_status
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
token = os.getenv("BOT_TOKEN")

if not token:
    raise SystemExit("Не задан BOT_TOKEN")


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("⏳ Запрашиваю статус сервера...")
    output = await asyncio.to_thread(get_status)
    await msg.edit_text(f"```\n{output}\n```", parse_mode="Markdown")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я слежу за сервером. Введи /status, чтобы узнать его состояние.")


app = Application.builder().token(token).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("status", status_command))

app.run_polling()