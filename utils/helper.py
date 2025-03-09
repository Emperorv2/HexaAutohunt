from asyncio import sleep as zzz
from random import randint
from config import pokemon_to_catch

async def handle_hunt(bot, chat, event=None):
    """
    Handles both initiating hunts and responding to encountered Pokémon.
    """
    if event:
        # Handle incoming messages during a hunt
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
        # Initiate a new hunt
        await bot.send_message(chat, "/hunt")
        for i in range(5, 10000):
            await zzz(randint(5000, 6020))
            await bot.send_message(chat, "/hunt")

async def handle_catch(bot, event):
    """
    Handles catching Pokémon during battles.
    """
    message = await bot.get_messages(event.chat_id, ids=event.message.id)
    text = event.message.text

    # Check if the Pokémon is in the catch list
    if any(pokemon in text for pokemon in pokemon_to_catch):
        print(f"Attempting to catch: {text}")
        await message.click(text="Poke Balls")
        await message.click(text="Poke Balls")
        await message.click(text="Poke Balls")
        if "Wild" in text:
            await zzz(2)
            await message.click(text="Ultra")
            await message.click(text="Ultra")
            await message.click(text="Ultra")
    if any(keyword in text for keyword in ['fled', 'fainted', 'caught']):
        await zzz(randint(5, 6))
        await bot.send_message(event.chat_id, "/hunt")