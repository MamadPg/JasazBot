import discord
from discord.ext import commands
import os
from datetime import datetime

class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        os.makedirs('./logs/bot_logs', exist_ok=True)
        os.makedirs('./logs/server_logs', exist_ok=True)

    async def log_bot_event(self, message):
        date = datetime.now().strftime("%Y-%m-%d")
        with open(f'./logs/bot_logs/bot_log_{date}.txt', 'a', encoding='utf-8') as f:
            f.write(f"[BOT] {datetime.now().strftime('%H:%M:%S')} - {message}\n")

    async def log_server_event(self, message):
        date = datetime.now().strftime("%Y-%m-%d")
        with open(f'./logs/server_logs/server_log_{date}.txt', 'a', encoding='utf-8') as f:
            f.write(f"[SERVER] {datetime.now().strftime('%H:%M:%S')} - {message}\n")

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            await self.log_server_event(f"{message.author} پیام داد: {message.content}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.log_server_event(f"{member} وارد سرور شد.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.log_server_event(f"{member} سرور رو ترک کرد.")

async def setup(bot):
    await bot.add_cog(Logger(bot))
