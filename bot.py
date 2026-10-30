import os
from dotenv import load_dotenv
import andro_cfw
from telegram.ext import Application

load_dotenv()
token = os.getenv("BOT_TOKEN")

if not token:
    raise SystemExit("Не задан BOT_TOKEN")



session = andro_cfw.patch()
app = Application.builder().token(token).build()
app.run_polling()