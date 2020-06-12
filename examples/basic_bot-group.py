# https://github.com/Rapptz/discord.py/blob/b3d2e2496869bf42cbdb5cd3eb6cbbb108a90d37/examples/basic_bot.py#L51

import discord
import re
import discordRebot as rebot

import shlex

bot = discord.Client()

key = rebot.Mapper()


class cool:
    def __init__(self):
        self.subcommands = dict()

    async def callback(self, msg, args):
        """Says if a user is cool.
        
        In reality this just checks if a subcommand is being invoked.
        """
        args = shlex.split(args)
        if len(args) == 0:
            return "No, {0} is not cool".format(None)
        for subcmd, callback_ in self.subcommands.items():
            if subcmd == args[0]:
                return await callback_(msg, *args[1:])
        else:
            return "No, {0} is not cool".format(args[0])

    def __call__(self, *keys):  # supports aliases
        def map_(callback):
            if keys:
                for key in keys:
                    self.subcommands[key] = callback
            else:
                self.subcommands[callable.__name__] = callback

        return map_


cool = cool()
key(re.compile(r"^\?cool([\s\S]*)$"))(cool.callback)


@cool("bot")
async def _bot(msg):
    """Is the bot cool?"""
    return "Yes, the bot is cool."


bot.event(rebot.Manager(key).on_message)
bot.run("token")
