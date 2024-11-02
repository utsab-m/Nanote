import discord
from discord.ext import commands
import requests
from PIL import Image
import random

with open("token.txt") as f:
    token = f.read()

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged in")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content == ".":
        await message.channel.send(f"Hey, {message.author.mention}! Type .help for help.")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="bot-test")
    await channel.send(f"{member} has arrived")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}, how are you doing today?")

@bot.command()
async def numberfact(ctx, number, type):
    response = requests.get(f"http://numbersapi.com/{number}/{type}")
    print(response.text)
    await ctx.send(response.text)

@bot.command()
async def qrcode(ctx, url):
   img = Image.open(requests.get(f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={url}", stream=True).raw)
   await ctx.send(file=discord.File(img))

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue(),
        description = "This is the bot for Nanote",
        title = "Nanote Bot"
    )
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/Ld1MygZaePg18KwsYsaWgwAwrXyGFfOrapP7NLsCVYM/%3Fsize%3D4096/https/cdn.discordapp.com/icons/1226754857906475018/6083a4741e9a37519376d9e92bd6caff.png?format=webp&quality=lossless")
    embed.set_footer(text=f"Made by ut1")
    await ctx.send(embed=embed)

@bot.command()
async def moviequote(ctx):
    response = requests.get("https://quoteapi.pythonanywhere.com/quotes/")
    rand = random.randint(0,82)
    randomQuotes = response.json()['Quotes'][0][rand]
    embed = discord.Embed(
        colour = discord.Colour.blue(),
        description = randomQuotes['quote'] + " - " + randomQuotes['actor_name'],
        title = randomQuotes['movie_title'] + " (" + randomQuotes['publish_date'] + ")"
    )
    await ctx.send(embed=embed)

@bot.command()
async def robloxgame(ctx):
    rand = 0
    success = False
    while success != True:
        rand = random.randint(0, 99999999999)
        print(rand)
        response = requests.get(f"https://games.roblox.com//v2/games/{rand}/media")
        if "200" in response:
            success = True
    
    print(rand)
    

bot.run(token);