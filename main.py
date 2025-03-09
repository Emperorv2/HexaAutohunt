from telethon import events, TelegramClient
  from config import api_id, api_hash, chat
  from utils.helpers import handle_hunt, handle_battle, handle_catch
  from constants import START_COMMAND, STOP_COMMAND

  bot = TelegramClient('session', api_id, api_hash)
  hunt = False

  @bot.on(events.NewMessage(outgoing=True, pattern=START_COMMAND))
  async def begin(event):
      global hunt
      hunt = True
      await handle_hunt(bot, chat)

  @bot.on(events.NewMessage(chats=chat, incoming=True))
  async def hunt(event):
      global hunt
      if hunt:
          await handle_hunt(bot, chat, event)

  @bot.on(events.NewMessage(chats=chat, incoming=True))
  async def battle(event):
      if event.message.text[:13] == "Battle begins":
          await handle_battle(bot, event)

  @bot.on(events.MessageEdited(chats=chat))
  async def catcher(event):
      await handle_catch(bot, event)

  @bot.on(events.NewMessage(outgoing=True, pattern=STOP_COMMAND))
  async def stop(event):
      global hunt
      hunt = False

  bot.start()
  bot.run_until_disconnected()