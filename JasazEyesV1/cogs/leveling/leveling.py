import discord
from discord.ext import commands
import sqlite3
import random

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('./database/users.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, xp INTEGER, level INTEGER)''')
        self.conn.commit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        user_id = message.author.id
        self.c.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = self.c.fetchone()

        if user is None:
            self.c.execute('INSERT INTO users (id, xp, level) VALUES (?, ?, ?)', (user_id, 0, 1))
            self.conn.commit()
            user = (user_id, 0, 1)

        xp = user[1] + random.randint(5, 15)
        level = user[2]

        if xp >= level * 100:
            xp = 0
            level += 1
            await message.channel.send(f"🎉 تبریک {message.author.mention}!\nشما به لول {level} رسیدید!")

        self.c.execute('UPDATE users SET xp = ?, level = ? WHERE id = ?', (xp, level, user_id))
        self.conn.commit()

    @commands.command(name='rank')
    async def rank(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        self.c.execute('SELECT * FROM users WHERE id = ?', (member.id,))
        user = self.c.fetchone()
        
        if user:
            xp, level = user[1], user[2]
            await ctx.send(f"🏆 {member.mention} در حال حاضر لول {level} با {xp} XP دارد!")
        else:
            await ctx.send("❌ شما هنوز هیچ XPای ندارید!")

async def setup(bot):
    await bot.add_cog(Leveling(bot))
