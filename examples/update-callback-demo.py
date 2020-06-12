from discordRebot import *

bot = discord.Client()
key = Mapper()


@key(re.compile(r"^repeat (.*)$"), re.compile(r"^twice (.*)$"))
def twice(msg, string):
    return string * 2


@key("upgrade-to-thrice")
def upgrade(msg):
    thrice = lambda msg, x: x * 3
    key(re.compile(r"^repeat (.*)$"))(thrice)
    return "repeat is upgrade to thrice the string"


bot.event(Manager(key).on_message)
bot.run("token")

"""
'repeat hello' -> "hellohello"
'twice world' -> "worldworld"
'upgrade-to-thrice' -> "repeat is upgrade to thrice the string"
'repeat hello' -> "hellohellohello"
'twice world' -> "worldworld"
"""
