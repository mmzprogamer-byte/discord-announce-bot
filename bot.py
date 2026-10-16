import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
print("TOKEN ที่ได้:", TOKEN)  # เพิ่มบรรทัดนี้เพื่อเช็ค

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ล็อกอินสำเร็จในชื่อ {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message: str):
    # ลบข้อความของคนที่พิมพ์คำสั่งทิ้ง
    try:
        await ctx.message.delete()
    except:
        pass

    # ส่งประกาศ
    embed = discord.Embed(
        description=message,
        color=0xE74C3C
    )
    # ใส่ Discord ID ของสมาชิกที่ต้องการแท็ก
user_ids = [
    123456789012345678,
    987654321098765432
]

# สร้างข้อความแท็กสมาชิก
mentions = " ".join(f"<@{user_id}>" for user_id in user_ids)

# ส่ง @here และแท็กสมาชิก พร้อม Embed
await ctx.send(
    content=f"@here {mentions}",
    embed=embed,
    allowed_mentions=discord.AllowedMentions(
        everyone=True,
        users=True
    )
)

bot.run(TOKEN)
