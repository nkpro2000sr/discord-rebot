Logging every message
=====================

discord.py logs errors and debug information via the logging python module. It is strongly recommended that the logging module is configured, as no errors or warnings will be output if it is not set up. Configuration of the logging module can be as simple as:

.. code-block:: python3

   import logging
   logging.basicConfig(level=logging.INFO)

Placed at the start of the application. This will output the logs from discord as well as other libraries that uses the logging module directly to the console.

The optional level argument specifies what level of events to log out and can any of CRITICAL, ERROR, WARNING, INFO, and DEBUG and if not specified defaults to WARNING.

More advance setups are possible with the logging module. To for example write the logs to a file called discord.log instead of outputting them to to the console the following snippet can be used:

.. code-block:: python3

   import discord
   import logging

   logger = logging.getLogger('discord')
   logger.setLevel(logging.DEBUG)
   handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
   handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
   logger.addHandler(handler)

This is recommended, especially at verbose levels such as INFO, and DEBUG as there are a lot of events logged and it would clog the stdout of your program.

But all of these is for debugging purpose and it will not logs the message content.

To do so we have to make a seperate listner which listens on every message and logs them.
For this we can use the filter in Manager class like::

   def log_msg(msg):
       # log msg.content
       return True
   Manager(filter=log_msg)

Manager skips bot's message after the filter, so no need to `enable listening to bot's message <listen-to-bot.html>`_

Example:

.. literalinclude:: ../../examples/logger.py
   :language: python3
   :emphasize-lines: 16,18,21
   :lines: 61-81

`full code in examples dir`
