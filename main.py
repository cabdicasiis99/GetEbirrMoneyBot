import os
from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI
import uvicorn

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = f"https://magaca-mashruucaaga.onrender.com{WEBHOOK_PATH}"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.process_update(telegram_update)
    return {"ok": True}

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Waa salaaman yahay! Bot-kii wuxuu ku shaqeynayaa Webhook.")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))