import discordRebot.tryrebot as rebot
import asyncio
import nest_asyncio

nest_asyncio.apply()


def only_owner(msg):  # discordRebot.Authorize don't support coro
    member = msg.author
    info = asyncio.run(rebot.client.application_info())
    owner_id = info.owner.id

    return member.id == owner_id


rebot.add_rshell(auth=only_owner)
rebot.add_rpy(auth="nkpro#3766", globals={"tryrebot": rebot})
rebot.run("token")
