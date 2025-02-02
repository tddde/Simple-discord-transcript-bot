import discord
from discord.ext import commands
import chat_exporter
import os

TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="+", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def transcript(ctx, channel: discord.TextChannel = None):
    """Exports the transcript of a given channel and sends it as an HTML file."""
    channel = channel or ctx.channel
    transcript = await chat_exporter.export(channel)

    if transcript is None:
        await ctx.send("Failed to generate transcript.")
        return
    
    transcript_file = f"transcript-{channel.name}.html"
    with open(transcript_file, "w", encoding="utf-8") as file:
        file.write(transcript)
    
    await ctx.send(file=discord.File(transcript_file))
    os.remove(transcript_file)

bot.run(TOKEN)
