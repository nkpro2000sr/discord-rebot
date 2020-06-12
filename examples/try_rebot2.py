import discordRebot.tryrebot as rebot
from discordRebot import *

client = discord.Client()
Convert = Converter(bot=client)

rebot.add_rshell()
rebot.add_rpy(globals=globals())

key = Mapper(rebot.P2F)


@key("!ping")
def Ping(msg):
    return "pong"


@key("!exit")
async def Exit(msg):
    await msg.channel.send("Bye Bye")
    await client.close()


client.event(Manager(key).on_message)
client.run("token")
