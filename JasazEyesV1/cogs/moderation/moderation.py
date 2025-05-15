import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="بدون دلیل"):
        await member.ban(reason=reason)
        await ctx.send(f"✅ کاربر {member.mention} بن شد! دلیل: {reason}")

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="بدون دلیل"):
        await member.kick(reason=reason)
        await ctx.send(f"✅ کاربر {member.mention} کیک شد! دلیل: {reason}")

    @commands.command(name='mute')
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            mute_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False)
        await member.add_roles(mute_role)
        await ctx.send(f"✅ کاربر {member.mention} میوت شد!")

    @commands.command(name='unmute')
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mute_role)
        await ctx.send(f"✅ کاربر {member.mention} آن‌میوت شد!")

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"✅ {amount} پیام پاک شد!", delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
