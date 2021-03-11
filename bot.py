#imports lol
import discord
import random
from discord.ext import commands
from discord.ext import tasks
import os
from itertools import cycle
import logging

#-----------------------------------#

#command prefix
client = commands.Bot(command_prefix = '#')
status = cycle(['Buiscits are cool','Use # for commands',])

#debug logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready!')

# Ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@tasks.loop(seconds=360)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#cogs
@client.command()
@commands.has_permissions(ban_members=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f' ***Loaded*** {extension} ')

@client.command()
@commands.has_permissions(ban_members=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f' ***Unloaded*** {extension} ')





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODE4MTE0OTQyOTAxMTU3OTI4.YETW6g.YtIMCYXhVdFNwIa3t-YlZ_ywpl8')
