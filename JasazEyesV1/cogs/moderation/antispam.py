import discord
from discord.ext import commands

class AntiSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message_counts = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if "http://" in message.content or "https://" in message.content:
            await message.delete()
            await message.channel.send(f"🚫 {message.author.mention} ارسال لینک مجاز نیست!", delete_after=5)
            return

        author_id = message.author.id
        if author_id not in self.message_counts:
            self.message_counts[author_id] = 1
        else:
            self.message_counts[author_id] += 1

        if self.message_counts[author_id] > 50:
            await message.delete()
            await message.channel.send(f"🚫 {message.author.mention} لطفاً اسپم نکن!", delete_after=5)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        author_id = message.author.id
        if author_id in self.message_counts:
            self.message_counts[author_id] = max(0, self.message_counts[author_id] - 1)

async def setup(bot):
    await bot.add_cog(AntiSpam(bot))
