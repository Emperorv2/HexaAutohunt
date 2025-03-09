from telethon import TelegramClient, events
from config import api_id, api_hash, phone_number, chat
from utils.helpers import handle_hunt, handle_catch
from constants import START_COMMAND, STOP_COMMAND

# Initialize the client
bot = TelegramClient('session', api_id, api_hash)
hunt = False

# Authenticate using the phone number
async def authenticate():
    if not await bot.is_user_authorized():
        await bot.send_code_request(phone_number)
        code = input("Enter the code you received: ")
        await bot.sign_in(phone_number, code)

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
    await handle_hunt(bot, chat)  # Start hunting

@bot.on(events.NewMessage(chats=chat, incoming=True))
async def hunt(event):
    global hunt
    if hunt:
        await handle_hunt(bot, chat, event)  # Handle encounters

@bot.on(events.NewMessage(chats=chat, incoming=True))
async def battle(event):
    if event.message.text[:13] == "Battle begins":
        await handle_catch(bot, event)  # Handle catching

@bot.on(events.NewMessage(outgoing=True, pattern=STOP_COMMAND))
async def stop(event):
    global hunt
    hunt = False

# Run the bot
with bot:
    bot.loop.run_until_complete(start_bot())