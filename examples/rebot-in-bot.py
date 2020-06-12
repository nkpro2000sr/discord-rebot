import discord
from discord.ext import commands
from discordRebot import *

description = "An example bot to show 'how to use rebot commands in bot'"
bot = commands.Bot(command_prefix="!", description=description)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command(name=">", brief="rebot commands eg:`!> echo hi`")
async def rebot_commands(ctx, *args):
    await rebot.on_message(ctx.message)


key = Mapper()


@key(re.compile(r"^!> echo (.*)$"))  # Eg: '!> echo hello' -> 'hello'
def echo(msg, string):
    return string


echo.auth = None

rebot = Manager(key)

bot.run("token")
