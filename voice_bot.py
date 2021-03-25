import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(pass_context=True)
async def pull(ctx, member : discord.Member):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await member.move_to(channel)
    else:
        await ctx.send("you are not in a voice channel")

@client.command(pass_context=True)
async def push(ctx, member : discord.Member, *, i=None):
    for channel in ctx.guild.channels:
        if channel.name == i:
            await member.move_to(channel)

client.run("ODI0NTc1NTY4NDE0NjM4MTUw.YFxX1w.6UwJhcciO4ahusvjMEURbujrayo")