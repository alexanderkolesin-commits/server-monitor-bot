import os
import asyncio
import subprocess
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
token = os.getenv("BOT_TOKEN")

if not token:
    raise SystemExit("Не задан BOT_TOKEN")


def run_ansible_status():
    inventory_path = "/home/alexandr/server-monitor-bot/ansible/inventory.ini" 
    cmd = [
        "ansible", "bot_servers", "-i", inventory_path,
        "-m", "command", "-a", "bash /home/alex/server-monitor-bot-deployed/scripts/status.sh"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return f"Ошибка Ansible:\n{result.stderr}"

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("⏳ Запрашиваю статус сервера...")
    output = await asyncio.to_thread(run_ansible_status)
    await msg.edit_text(f"```\n{output}\n```", parse_mode="Markdown")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я слежу за сервером. Введи /status, чтобы узнать его состояние.")


app = Application.builder().token(token).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("status", status_command))

app.run_polling()