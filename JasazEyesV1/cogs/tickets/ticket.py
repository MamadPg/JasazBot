import discord
from discord.ext import commands

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="newticket")
    async def new_ticket(self, ctx, *, reason="پشتیبانی"):
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True)
        }

        ticket_channel = await ctx.guild.create_text_channel(f"ticket-{ctx.author.name}", overwrites=overwrites)
        await ticket_channel.send(
            f"🎫 سلام {ctx.author.mention}!\nتیکت شما ایجاد شد.\nموضوع: {reason}\nصبر کنید تا پشتیبان پاسخ بدهد.")

    @commands.command(name="closeticket")
    @commands.has_permissions(manage_channels=True)
    async def close_ticket(self, ctx):
        if ctx.channel.name.startswith("ticket-"):
            await ctx.send("✅ این تیکت در حال بسته شدن است...", delete_after=5)
            await ctx.channel.delete()
        else:
            await ctx.send("❌ این دستور فقط در کانال‌های تیکت قابل استفاده است!")

async def setup(bot):
    await bot.add_cog(Ticket(bot))
