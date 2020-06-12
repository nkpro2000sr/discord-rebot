from discordRebot import *
import logging
import sys
import traceback
import random
import asyncio

client = discord.Client()

key = Mapper()


@key("$guess")
async def Guess(msg):
    yield "Guess a number between 1 and 10."

    def is_correct(m):
        return m.author == msg.author  # and m.content.isdigit()

    answer = random.randint(1, 10)

    try:
        guess = await client.wait_for("message", check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        yield "Sorry, you took too long it was {}.".format(answer)
        return

    if int(guess.content) == answer:
        yield "You are right!"
    else:
        yield "Oops. It is actually {}.".format(answer)


logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)

# Log everything
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

# Print exceptions
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.ERROR)
stdout_handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(stdout_handler)

# Print exceptions in event (above can't handle it)
@client.event
async def on_error(event, *args, **kwargs):
    if event == "on_message":
        msg = args[0]
        logger.error(msg.content + "\n" + traceback.format_exc())
        msg_logger.error(f"ERROR{sys.exc_info()} on: " + msg.content)
        await msg.channel.send("You caused an error!")
    else:
        logger.error(traceback.format_exc())


# all the aboves can't log messages
# To log all messages with author and channel
msg_logger = logging.getLogger("discord_messages")
msg_logger.setLevel(logging.INFO)

msg_handler = logging.FileHandler(filename="discord_messages.log", encoding="utf-8", mode="w")
msg_handler.setFormatter(logging.Formatter("%(asctime)s: %(message)s"))
msg_logger.addHandler(msg_handler)


def log_msg(msg):
    author = str(msg.author)
    channel = str(msg.channel)
    guild = msg.guild
    if guild:
        channel = str(guild) + ":" + channel
    msg_logger.info(author + ">" + channel + ": " + msg.content)

    return True


mybot = Manager(key, filter=log_msg)

client.event(mybot.on_message)
client.run("token")
