.. discordRebot documentation master file, created by
   sphinx-quickstart on Wed May 27 00:20:05 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to discordRebot
=======================

**discordRebot** is a RegEx based command mapping discord BOT framework with **authorization**.

Why discordRebot?
-----------------

**discordRebot** is easy to use, minimal, and async ready framework using `discord.py`_

Most of the bots uses a single prefix, string to match command and args splited by spaces. example ``!cmd arg1 arg2``

But discordRebot uses RegEx for both matching the command and capturing the arguments. It gives more control over both matching the command and parsing arguments.

Also it provides authorization to authorize the author of the message before executing the command.

Basic Example
-------------

A minimal bot with echo command

.. code-block:: python3
   :linenos:

   from discordRebot import *
   
   client = discord.Client()
   key = Mapper()
   
   @key(re.compile(r"^!echo (.*)$")) # Eg: '!echo hello' -> 'hello'
   def echo(msg, string):
       return string
   echo.auth = None
   
   client.event(Manager(key).on_message)
   import os; client.run(os.environ["DBToken"])

You can find more examples in the examples directory.

Features
--------

* It supports

   * functions
   * `generators`_
   * `asynchronous functions`_
   * `asynchronous generators`_

  Example::
  
     @key(re.compile(r"^!ticker (\d*) (\d*)$"))
     async def ticker(msg, delay, to):
         delay, to = int(delay), int(to)
         for i in range(to):
             yield i
             await asyncio.sleep(delay)

* Authorizes the message author

   based on

   * `user_id`_ example:``1234567890``
   * `user_name`_ example:``'user#1234'``
   * `roles`_ in server *(not applicable for DM)*
   * `permissions`_ of members in server *(not applicable for DM)*
   * custom **Callable[[message], bool]**

  Example::
  
     @key("am i authorized ?")
     def amiauthorized(msg):
         return "Authorized"
     amiauthorized.auth = {1234567890, 'user#1234'}
     # only executable by user1 (with id 1234567890) and user2 (with username 'user#1234')

* Can match multiple commands with a message

  Example::
  
     @key(re.compile(r"^([\s\S]*)$"))
     def printmsg(msg, content):
         print(f"@{msg.author}:")
         print(content)
     
     @key("whereami")
     def whereami(msg):
         if msg.guild:
             return msg.guild.name
         else:
             return "DM"


.. toctree::
   :hidden:
   :maxdepth: 1

   examples
   authorization


discordRebot package
====================

* :ref:`modindex`
* `Modules Source code`_
* :ref:`search`

.. * :ref:`genindex`


.. _`discord.py`: https://discordpy.readthedocs.io/en/latest

.. _`Modules Source code`: _modules/index.html

.. _`generators`: https://wiki.python.org/moin/Generators

.. _`asynchronous functions`: https://docs.python.org/library/asyncio.html

.. _`asynchronous generators`: https://www.python.org/dev/peps/pep-0525

.. _`user_id`: discordRebot.html#discordRebot.members.Members

.. _`user_name`: discordRebot.html#discordRebot.members.Members

.. _`roles`: discordRebot.html#discordRebot.members.Roles

.. _`permissions`: discordRebot.html#discordRebot.members.Permissions


.. Key features that are missing
   * Cooldown
   * Type conversion based on CallBack.__annotations__ (Have to think more)
   * args for string based command matching in Manager like discord.ext.commands (May be) 
