# scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from report_generator import get_todays_sales, get_trade_in_the_provinces, get_order_count, get_amount_of_debt, get_money_amount
from config import BOT_TOKEN, ADMIN_CHAT_ID
from aiogram import Bot
import asyncio

bot = Bot(token=BOT_TOKEN)
scheduler = BackgroundScheduler()

def send_report():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def task():
        sales = get_todays_sales()
        regions = get_trade_in_the_provinces()
        orders = get_order_count()
        debt = get_amount_of_debt()
        money = get_money_amount()
        report = f"🕒 Avtomatik Hisobot:\n\n📅 {sales}\n\n📍 {regions}\n\n📦 {orders}\n\n {debt}\n\n {money}"
        await bot.send_message(chat_id=ADMIN_CHAT_ID, text=report)

    loop.run_until_complete(task())
    loop.close()  # ✅ event loop ni yopamiz

def start_scheduler():
    # Har kuni soat 08:00 da ishlaydi
    scheduler.add_job(send_report, 'cron', hour=11, minute=0)
    # scheduler.add_job(send_report, 'interval', minutes=2)
    scheduler.start()

