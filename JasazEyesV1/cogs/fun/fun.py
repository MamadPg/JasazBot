import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='randompick')
    async def randompick(self, ctx, *, choices):
        items = choices.split(',')
        pick = random.choice(items)
        await ctx.send(f"🎯 انتخاب من: **{pick.strip()}**")

    @commands.command(name='say')
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(name='userinfo')
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title="اطلاعات کاربر", color=discord.Color.random())
        embed.add_field(name="نام", value=member.name, inline=True)
        embed.add_field(name="تگ", value=member.discriminator, inline=True)
        embed.add_field(name="آیدی", value=member.id, inline=True)
        embed.add_field(name="عضویت در سرور", value=member.joined_at.strftime("%Y/%m/%d"), inline=True)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name='serverinfo')
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title="اطلاعات سرور", color=discord.Color.random())
        embed.add_field(name="نام سرور", value=guild.name, inline=True)
        embed.add_field(name="تعداد اعضا", value=guild.member_count, inline=True)
        embed.set_thumbnail(url=guild.icon.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))
