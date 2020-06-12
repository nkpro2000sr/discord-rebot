CallBack for commands
=====================

CallBack for each commands can be of types

*   Functions
*   Generators
*   Asynchronous Functions
*   Asynchronous Generators

Function type
-------------

Functions can't be a better since we can't call asynchronous functions (including ``msg.channel.send``) from non asynchronous functions
so we can reply only once.

Example::

   @key(re.compile(r"^!repeat (\d*) (.*)$"))
   def repeat(msg, times, string):
       times = int(times)
       return '\n'.join([string]*times)

Generator type
--------------

With Generators we can reply multiple times even though it is non asynchronous.

Example::

   @key(re.compile(r"^!repeat (\d*) (.*)$"))
   def repeat(msg, times, string):
       times = int(times)
       for i in range(times):
           yield string

Asynchronous Function type
--------------------------

Asynchronous Functions is recommended since we can call both asynchronous functions and non asynchronous functions.
Also most of the discord.py methods are asynchronous.

Example::

   @key(re.compile(r"^!repeat (\d*) (.*)$"))
   async def repeat(msg, times, string):
       times = int(times)
       for i in range(times):
           await msg.channel.send(string)

Asynchronous Generator type
---------------------------

Asynchronous Generators has a benefit of reply multiple times. (Asynchronous Functions also can using ``msg.channel.send``)

Example::

   @key(re.compile(r"^!repeat (\d*) (.*)$"))
   async def repeat(msg, times, string):
       times = int(times)
       for i in range(times):
           yield string


Updating callback at runtime
============================

It supports updating callbacks at runtime, since it is literally changing value of key(s) in python dictionary.

.. literalinclude:: ../../examples/update-callback-demo.py
   :language: python3
   :emphasize-lines: 1,9
   :lines: 7-17, 21-28
