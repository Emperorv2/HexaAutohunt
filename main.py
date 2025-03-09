from telethon import TelegramClient, events
from config import api_id, api_hash, phone_number, chat
from utils.helpers import handle_hunt, handle_catch
from constants import START_COMMAND, STOP_COMMAND

# Initialize the client
bot = TelegramClient('session', api_id, api_hash)

# Authenticate using the phone number
async def authenticate():
    if not await bot.is_user_authorized():
        await bot.send_code_request(phone_number)
        code = input("Enter the code you received: ")
        try:
            await bot.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input("Your 2FA password: ")
            await bot.sign_in(password=password)

# Start the bot
async def start_bot():
    await authenticate()
    print("Bot is running...")
    await bot.run_until_disconnected()

# Event handlers
@bot.on(events.NewMessage(outgoing=True, pattern=START_COMMAND))
async def begin(event):
    global hunt
    hunt = True
    await handle_hunt(bot, chat)

@bot.on(events.NewMessage(chats=chat, incoming=True))
async def hunt(event):
    global hunt
    if hunt:
        await handle