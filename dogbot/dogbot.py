
import nextcord
from nextcord.ext import commands
import requests, json, random, datetime, asyncio

links = json.load(open("dogbot/gifs.json"))

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="dog ", intents=intents)

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send("Hello!")

@bot.command(name="pic")
async def Dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await ctx.send(image_link)

@bot.command(name="gif", aliases=["feed", "play", "sleep"])
async def Gif(ctx):
    await ctx.send(random.choice(links[ctx.invoked_with]))

#async def schedule_daily_message():
    #while True:
        #now = datetime.datetime.now()
        #then = now.replace(hour=8, minute=17)
        #3wait_time = (then-now).total_seconds()
       ## await asyncio.sleep(wait_time)

        #channel = bot.get_channel(1042730980538060863)
        #await channel.send("Good morning!!")
        #await channel.send(random.choice(links["play"]))



@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    #await schedule_daily_message()

if __name__ == '__main__':
    bot.run("MTA0Mzc2MzEwNjgzNDI4ODcxMA.Gf6JKQ.UN4b1luzKgacIbfs5gB1fGcP_kh7242n9blQQs")