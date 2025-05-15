import discord
from discord.ext import commands
import asyncio
import json
import os

# لود کردن تنظیمات از فایل config.json
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

TOKEN = config["token"]
PREFIX = config["prefix"]
LANG = config["language"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# شروع ربات
@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} is now online!")

# لود کردن Cogs
async def load_cogs():
    for folder in os.listdir('./cogs'):
        if os.path.isdir(f'./cogs/{folder}'):
            for filename in os.listdir(f'./cogs/{folder}'):
                if filename.endswith('.py'):
                    await bot.load_extension(f'cogs.{folder}.{filename[:-3]}')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
