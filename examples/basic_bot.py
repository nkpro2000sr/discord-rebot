# https://github.com/Rapptz/discord.py/blob/master/examples/basic_bot.py

import discord
import re
import discordRebot as rebot
import random

import shlex

bot = discord.Client()
Convert = rebot.Converter(bot)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


key = rebot.Mapper()


@key(re.compile(r"^\?add (\d+) (\d+)$"))
async def add(msg, left, right):
    """Adds two number together."""
    left, right = int(left), int(right)
    return left + right  # or msg.channel.send(str(left + right))


@key(re.compile(r"^\?roll (\S+)$"))
async def roll(msg, dice):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        return "Format has to be in NdN!"

    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
    return result


@key(re.compile(r"^\?choose ([\s\S]+)$"))
async def choose(msg, choices):
    """Chooses between multiple choices."""
    choices = shlex.split(choices)
    return random.choice(choices)


@key(re.compile(r"^\?repeat (\d+)(?: ([\s\S]+))?$"))
async def repeat(msg, times, content=None):
    """Repeats a message multiple times."""
    times = int(times)
    if content is None:
        content = "repeating..."
    for _ in range(times):
        yield content


@key(re.compile(r"^\?joined (\S+)$"))
async def joined(msg, member):
    """Says when a member joined."""
    member = await Convert(msg, member, discord.Member)
    return "{0.name} joined in {0.joined_at}".format(member)


@key(re.compile(r"^\?cool([\s\S]*)$"))
async def cool(msg, args):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    args = shlex.split(args)
    if len(args) == 0:
        return "No, {0} is not cool".format(None)
    elif args[0] == "bot":
        return await _bot(msg, *args[1:])
    else:
        return "No, {0} is not cool".format(args[0])


async def _bot(msg):
    """Is the bot cool?"""
    return "Yes, the bot is cool."


bot.event(rebot.Manager(key).on_message)
bot.run("token")
