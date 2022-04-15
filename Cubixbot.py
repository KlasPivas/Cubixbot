import aiohttp
import discord
from discord.ext import commands
from random import choice
from random import randint
import asyncio
from discord.ext.commands import Bot
import random
import time
import json

TOKEN = "OTY0MTg5MjYwMDkxNjIxNDI2.YlhBOQ.6zhdPNRfucSt6BtXQI_IIzS-KYQ"

intents = discord.Intents.default()
client = discord.Client()
bot = commands.Bot(command_prefix='+', intents = intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("мой любимый я готова")

@bot.command(name='Хуй')
async def truthoraction(ctx):
    await ctx.send("8=====D")

@bot.command(name="эстетика")
async def SendPepe(ctx):
    await ctx.send(choice(["https://media.discordapp.net/attachments/964235425390690305/964252304947691592/Screenshot_1.png?width=449&height=449","https://media.discordapp.net/attachments/964235425390690305/964252305211920424/Screenshot_2.png?width=451&height=449","https://media.discordapp.net/attachments/964235425390690305/964252305446817852/Screenshot_3.png?width=341&height=449","https://media.discordapp.net/attachments/964235425390690305/964252305706872922/Screenshot_4.png?width=384&height=449","https://media.discordapp.net/attachments/964235425390690305/964253022815416340/ffff.png?width=449&height=449","https://media.discordapp.net/attachments/964235425390690305/964253023046107226/7ae9116f57aaa744.png?width=449&height=449","https://media.discordapp.net/attachments/964235425390690305/964253023335493722/a23f306030b56630.png?width=674&height=449","https://media.discordapp.net/attachments/964235425390690305/964253023851405392/wWbIirh6Jjs.jpg"]))

@bot.command(name="мем")
async def Sendmem(ctx):
    await ctx.send(choice(["https://media.discordapp.net/attachments/943690794202697738/964460779451592784/unknown.png"]))
    
@bot.command(name="hentai")
async def Sendhentai(ctx):
    a = ['solog', 'smug', 'feet', 'smallboobs', 'lewdkemo', 'woof', 'gasm', 'solo', '8ball', 'goose', 'cuddle', 'avatar', 'cum', 'slap', 'les', 'v3', 'erokemo', 'bj', 'pwankg', 'nekoapi_v3.1', 'ero', 'hololewd', 'pat', 'gecg', 'holo', 'poke', 'feed', 'fox_girl', 'tits', 'nsfw_neko_gif', 'eroyuri', 'holoero', 'pussy', 'Random_hentai_gif', 'lizard', 'yuri', 'keta', 'neko', 'hentai', 'feetg', 'eron', 'erok', 'baka', 'kemonomimi', 'hug', 'cum_jpg', 'nsfw_avatar', 'erofeet', 'meow', 'kiss', 'wallpaper', 'tickle', 'blowjob', 'spank', 'kuni', 'classic', 'waifu', 'femdom', 'boobs', 'trap', 'lewd', 'pussy_jpg', 'anal', 'futanari', 'ngif', 'lewdk']
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://nekos.life/api/v2/img/" + random.choice(a)) as response:
            b = await response.json()
            await ctx.send(b.get("url"))
            

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    items = [
        {
             "name": "алмаз",
             "count": 1,
             "price": 1
        },
        {
             "name": "золото",
             "count": 2,
             "price": 1
        }
    ]
    if message.content.startswith("цена"):
        content = message.content.replace("цена ", "")
        for item in items:
            if content == item.get("name"):
                await message.channel.send("Цена {} за {} шт == {} кубиксов".format(item.get("name"), item.get("count"), item.get("price")))
                
@bot.command(name="Github")
async def sendGithub(ctx):
    embed = discord.Embed(
        title="Тык для перехода",
        description="Ссылка для перехода на GitHub",
        url='https://github.com/Flandi000/Cubixbot',
    )
    await ctx.send(embed=embed)

bot.run(TOKEN)
