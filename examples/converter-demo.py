from discordRebot import *

client = discord.Client()
Convert = Converter(bot=client)
key = Mapper()


@key(re.compile(r"^\?joined (\S*)$"))
async def joined_at(msg, member):
    """Says when a member joined."""
    member = await Convert(msg, member, discord.Member)
    return str(member.joined_at)


# "?joined nkpro" -> "2020-05-18 17:36:52.843000"


@key(re.compile(r"^\?discriminator (\S*)$"))
async def discriminator(msg, user):
    """Gives discriminator of user"""
    user = await Convert(msg, user, discord.User)
    return user.discriminator


# "?discriminator nkpro" -> "3766"


@key(re.compile(r"^\?reactions (\S*)$"))
async def reactions(msg, message):
    """Shows all reactions to a given message"""
    message = await Convert(msg, message, discord.Message)
    return str(message.reactions)


# "?reactions 1234567890-0987654321" -> "[<Reaction emoji=':smiley:' me=False count=1>]"


@key(re.compile(r"^>sendHI (\S*)$"))
async def send_hi(msg, channel):
    """Sends HI message to given channel"""
    channel = await Convert(msg, channel, discord.TextChannel)
    await channel.send("HI")


# ">sendHI general" -> "HI" (to the channel named 'general')


@key(re.compile(r"^\?connectednos (\S*)$"))
async def n_connected_members(msg, channel):
    """Gives no of connected members in given voice channel"""
    channel = await Convert(msg, channel, discord.VoiceChannel)
    return len(channel.voice_states.keys())


# "?connectednos General" -> "1"


@key(re.compile(r"^\?channelnos (\S*)$"))
async def n_channels(msg, category):
    """Gives no of channels in given category"""
    category = await Convert(msg, category, discord.CategoryChannel)
    return len(category.channels)


# "?channelnos category1" -> "2"


@key(re.compile(r"^\?members (\S*)$"))
async def members_in_role(msg, role):
    """Gives members name in given role"""
    role = await Convert(msg, role, discord.Role)
    return str([m.name for m in role.members])


# "?members Admin" -> "['nkpro', 'mybot']"


client.event(Manager(key).on_message)
import os

client.run(os.environ["DBToken"])
