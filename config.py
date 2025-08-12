BOT_TOKEN = '8259714661:AAFouer9Sus2yOKVRvAymtY9DNncKYR2QXw'
ADMIN_CHAT_ID = 634731252
ONE_C_URL = "https://1c-uz.pharmlux.uz/phl/hs/bot_api/"
ALLOWED_USERS = {
634731252, 1281264805
}
ONE_C_USER = 'Exchange'
ONE_C_PASS = "Exchanger"

from aiogram.types import BotCommand

async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="🏁 Botni ishga tushirish"),
        BotCommand(command="/report", description="📊 1C hisobotini olish"),
        BotCommand(command="/clear", description="🧹 Chatni tozalash"),
        BotCommand(command="/restart", description="♻️ Botni qayta ishga tushirish"),
        BotCommand(command="/stop", description="🛑 Botni to‘xtatish"),
    ]
    await bot.set_my_commands(commands)
