import discord
from discord.ext import commands
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
translator = Translator()

SOURCE_CHANNEL_ID = int(os.getenv("SOURCE_CHANNEL_ID"))
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول كـ {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id == SOURCE_CHANNEL_ID and not message.author.bot:
        translated = translator.translate(message.content, dest='ar').text
        target_channel = bot.get_channel(TARGET_CHANNEL_ID)
        await target_channel.send(f"**ترجمة الرسالة:**\n{translated}")

bot.run(os.getenv("DISCORD_TOKEN"))
