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
    
@bot.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message: str):

    # ลบข้อความคำสั่งของคนที่พิมพ์
    try:
        await ctx.message.delete()
    except:
        pass

    # สร้างกรอบประกาศ
    embed = discord.Embed(
        description=message,
        color=0xE74C3C
    )

    # ส่ง @here นอกกรอบ พร้อมประกาศในกรอบ
    await ctx.send(
        content="@here",
        embed=embed,
        allowed_mentions=discord.AllowedMentions(
            everyone=True
        )
    )


@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("คุณไม่มีสิทธิ์ใช้คำสั่งนี้", delete_after=5)

)

bot.run(TOKEN)
