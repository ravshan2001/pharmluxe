from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN, ALLOWED_USERS
from aiogram.types import BotCommand
from aiogram.dispatcher.handler import CancelHandler
from report_generator import (
    get_todays_sales,
    get_trade_in_the_provinces,
    get_order_count,
    get_money_amount,
    get_amount_of_debt
)


from scheduler import start_scheduler
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Boshqa foydalanuvchilarni cheklash
class AccessControlMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data:dict):
        if message.from_user.id not in ALLOWED_USERS:
            await message.answer("⛔ You are not allowed to use this bot")
            raise CancelHandler()
dp.middleware.setup(AccessControlMiddleware())

# 🔘 Tugmalarni yaratamiz
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("📅 Bugungi Savdo"),
)
main_menu.add(
    KeyboardButton("📦 Buyurtmalar Soni"),
    KeyboardButton("📍 Viloyatlardagi Savdo"),
    # KeyboardButton("💶 Tushgan summa")
)
main_menu.add(
    KeyboardButton("💶 Qarzdorlik miqdori"),
    KeyboardButton("🗓 Sanalar bo'yicha ma'lumotlarni olish")
)

async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="🏁 Botni ishga tushirish"),
        BotCommand(command="/report", description="📊 1C hisobotini olish"),
        BotCommand(command="/clear", description="🧹 Chatni tozalash"),
        BotCommand(command="/restart", description="♻️ Botni qayta ishga tushirish"),
        BotCommand(command="/stop", description="🛑 Botni to‘xtatish"),
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer(
        "Xush kelibsiz! Kerakli hisobotni tanlang:",
        reply_markup=main_menu
    )
    print("Foydalanuvchi chat_id:", message.chat.id)

@dp.message_handler(commands=['clear'])
async def clear_chat(message: types.Message):
    await message.answer("♻️ Chat tozalanmoqda...")

    try:
        # Oxirgi 20 xabarni orqaga qarab tekshiramiz
        for msg_id in range(message.message_id - 1, message.message_id - 1000, -1):
            try:
                await bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
            except:
                continue

        await message.answer("✅ Chat tozalandi.")
    except Exception as e:
        await message.answer(f"❌ Xatolik: {e}")

@dp.message_handler(commands=['report'])
async def send_report(message: types.Message):
    sales = get_todays_sales()
    regions = get_trade_in_the_provinces()
    orders = get_order_count()
    debt = get_amount_of_debt()
    money = get_money_amount()
    report = f"🕒 Avtomatik Hisobot:\n\n📅 {sales}\n\n📍 {regions}\n\n📦 {orders}\n\n {debt}\n\n {money}"
    await message.answer(text=report)


@dp.message_handler(commands=['restart'])
async def restart_bot(message: types.Message):
    await message.answer("🔄 Bot qayta ishga tushmoqda...")
    import sys
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)

@dp.message_handler(lambda message: message.text == "📅 Bugungi Savdo")
async def handle_today_sales(message: types.Message):
    await message.answer("⏳ Bugungi savdo olinmoqda...")
    try:
        report1 = get_todays_sales()
        report2 = get_money_amount()
        await message.answer(f"📅 Bugungi savdo:\n{report1}\n\n 💶Tushgan summa\n{report2}")
    except Exception as e:
        await message.answer(f"❌ Xatolik:\n{e}")

@dp.message_handler(lambda message: message.text == "📍 Viloyatlardagi Savdo")
async def handle_region_sales(message: types.Message):
    await message.answer("⏳ Viloyatlar bo‘yicha savdo olinmoqda...")
    try:
        report = get_trade_in_the_provinces()
        await message.answer(f"📍 Viloyatlar bo‘yicha savdo:\n{report}")
    except Exception as e:
        await message.answer(f"❌ Xatolik:\n{e}")
#
@dp.message_handler(lambda message: message.text == "📦 Buyurtmalar Soni")
async def handle_order_count(message: types.Message):
    await message.answer("⏳ Buyurtmalar soni olinmoqda...")
    try:
        report = get_order_count()
        await message.answer(f"📦 Buyurtmalar soni:\n{report}")
    except Exception as e:
        await message.answer(f"❌ Xatolik:\n{e}")

# @dp.message_handler(lambda message: message.text == "💶 Tushgan summa")
# async def handle_money_amount(message: types.Message):
#     await message.answer("⏳ Tushgan summa aniqlanmoqda...")
#     try:
#         report = get_money_amount()
#         await message.answer(f"💶Tushgan summa\n{report}")
#     except Exception as e:
#         await message.answer(f"❌ Xatolik:\n{e}")

@dp.message_handler(lambda message: message.text == "💶 Qarzdorlik miqdori")
async def handle_debt_amount(message: types.Message):
    await message.answer("⏳ Qarzdorlik aniqlanmoqda...")
    try:
        report = get_amount_of_debt()
        await message.answer(f"💶 Qarzdorlik miqdori\n{report}")
    except Exception as e:
        await message.answer(f"❌ Xatolik:\n{e}")


@dp.message_handler(lambda message: message.text == "🗓 Sanalar bo'yicha ma'lumotlarni olish")
async def handle_debt_amount(message: types.Message):
    await message.answer("⏳ Sanalar bo'yicha ma'lumotlar olinmoqda...")
    try:
        # report = get_money_debt()
        await message.answer(f"Hozircha bu funksiya ishlab chiqarish jarayonida!")
    except Exception as e:
        await message.answer(f"❌ Xatolik:\n{e}")

if __name__ == '__main__':
    from asyncio import get_event_loop
    loop = get_event_loop()

    loop.run_until_complete(set_commands(bot))  # 🟩 BU YERGA QO'YASIZ
    start_scheduler()
    executor.start_polling(dp, skip_updates=True)