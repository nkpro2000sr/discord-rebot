Safely listen to other bot's message
====================================

At default Manager will not listen to bot's reply.
To do so enable listenBot while creating Manager object like ``manager = Manager(P2F, listenBot=True)``.

But now manager would also listen to our bot *client.user*. This may leads to infinite loop of messages.

So to safely listen to other bot's message we need to make a filter like
``skip_our_bot = lambda message: message.author != client.user``

Example::

   from discordRebot import *
   
   client = discord.Client()
   
   def skip_our_bot(msg):
       if msg.author == client.user:
           # don't reply to overself
           return False
       else:
           return True
   
   manager = Manager(key, listenBot=True, filter=skip_our_bot)
   
   client.event(manager.on_message)
