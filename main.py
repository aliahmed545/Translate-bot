import hikari
import lightbulb
import os
from googletrans import Translator

SOURCE_CHANNEL_ID = int(os.getenv("SOURCE_CHANNEL_ID"))
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))
translator = Translator()

bot = lightbulb.Bot(prefix="!", token=os.getenv("DISCORD_TOKEN"), intents=hikari.Intents.ALL)

@bot.listen(hikari.MessageCreateEvent)
async def on_message(event):
    if event.channel_id == SOURCE_CHANNEL_ID and not event.is_bot:
        translated = translator.translate(event.content, dest="ar").text
        await bot.rest.create_message(TARGET_CHANNEL_ID, f"**ترجمة الرسالة:**\n{translated}")

bot.run()
