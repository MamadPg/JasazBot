import discord
from discord.ext import commands
import json
import os

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings_file = 'welcome_settings.json'
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r', encoding='utf-8') as f:
                self.settings = json.load(f)
        else:
            self.settings = {"welcome_message": "سلام @user عزیز به server خوش اومدی! 🎉",
                             "goodbye_message": "خداحافظ @user عزیز! 🌙"}

    def save_settings(self):
        with open(self.settings_file, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, ensure_ascii=False, indent=4)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel:
            welcome = self.settings["welcome_message"]
            welcome = welcome.replace("@user", member.mention).replace("server", member.guild.name)
            embed = discord.Embed(title="🎉 خوش آمدی!", description=welcome, color=discord.Color.green())
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel:
            goodbye = self.settings["goodbye_message"]
            goodbye = goodbye.replace("@user", member.name).replace("server", member.guild.name)
            embed = discord.Embed(title="😢 خداحافظی", description=goodbye, color=discord.Color.red())
            await channel.send(embed=embed)

    @commands.command(name="setwelcome")
    @commands.has_permissions(administrator=True)
    async def set_welcome(self, ctx, *, message):
        self.settings["welcome_message"] = message
        self.save_settings()
        await ctx.send("✅ پیام خوشامد جدید ذخیره شد!")

    @commands.command(name="setgoodbye")
    @commands.has_permissions(administrator=True)
    async def set_goodbye(self, ctx, *, message):
        self.settings["goodbye_message"] = message
        self.save_settings()
        await ctx.send("✅ پیام خداحافظی جدید ذخیره شد!")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
