from config import pokemon_to_catch

   async def handle_hunt(bot, chat, event=None):
       if event:
           text = event.message.text
           message = await bot.get_messages(chat, ids=event.message.id)

           # Check if the encountered Pokémon is in the catch list
           if any(pokemon in text for pokemon in pokemon_to_catch):
               print(f"Encountered a Pokémon to catch: {text}")
               await message.click(text="Battle")
               await message.click(text="Battle")
               await message.click(text="Battle")
           elif "Shiny" in text:
               print("Shiny encountered! Stopping the bot.")
               bot.disconnect()
           elif "TM" in text:
               print(f"TM found: {text}")
               await zzz(randint(5, 6))
               await bot.send_message(chat, "/hunt")
           elif "A wild" in text or "An expert" in text:
               await zzz(randint(5, 6))
               await bot.send_message(chat, "/hunt")
       else:
           await bot.send_message(chat, "/hunt")
           for i in range(5, 10000):
               await zzz(randint(5000, 6020))
               await bot.send_message(chat, "/hunt")