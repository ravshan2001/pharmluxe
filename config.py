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
