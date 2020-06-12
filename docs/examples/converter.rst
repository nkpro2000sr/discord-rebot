Converter
=========

To convert **string** to actual **discord.\*** class objects.

| Example:
| ``"nkpro" => <Member id=1234567890 name='nkpro' discriminator='3766' bot=False nick=None guild=<Guild id=0987654321 name='GUILD' shard_id=None chunked=True member_count=2>>``

:class:`discord.ext.commands.Bot` do this convertions while calling the commands callback based on their annotations *(callback.__annotations__)*.

We can do the same with :class:`discordRebot.converter.Converter` which uses :func:`discord.ext.commands.Command._actual_conversion` for conversions.
But it requires context which, needs both bot and message to lookup for conversions.

So the usage of :class:`discordRebot.converter.Converter` would like::

   Convert = Converter(bot=client)
   
   member = Convert(msg, "nkpro", discord.Member) # msg is the :obj:`discord.Message` passed to every callback

Convertions
-----------

MemberConvertions (**string** -> **discord.Member**) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The lookup strategy is as follows (in order):
| 1. Lookup by ID.
| 2. Lookup by mention.
| 3. Lookup by name#discrim
| 4. Lookup by name
| 5. Lookup by nickname

Example:

.. literalinclude:: ../../examples/converter-demo.py
   :language: python3
   :emphasize-lines: 4
   :lines: 8-15


UserConvertions (**string** -> **discord.User**)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The lookup strategy is as follows (in order):
| 1. Lookup by ID.
| 2. Lookup by mention.
| 3. Lookup by name#discrim
| 4. Lookup by name

Example:

.. literalinclude:: ../../examples/converter-demo.py
   :language: python3
   :emphasize-lines: 4
   :lines: 18-25


MessageConvertions (**string** -> **discord.Message**)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The lookup strategy is as follows (in order):
| 1. Lookup by "{channel ID}-{message ID}" (retrieved by shift-clicking on "Copy ID")
| 2. Lookup by message ID (the message **must** be in the context channel)
| 3. Lookup by message URL

Example:

.. literalinclude:: ../../examples/converter-demo.py
   :language: python3
   :emphasize-lines: 4
   :lines: 28-35


TextChannelConvertions (**string** -> **discord.TextChannel**)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The lookup strategy is as follows (in order):
| 1. Lookup by ID.
| 2. Lookup by mention.
| 3. Lookup by name

Example:

.. literalinclude:: ../../examples/converter-demo.py
   :language: python3
   :emphasize-lines: 4
   :lines: 38-45


VoiceChannelConvertions (**string** -> **discord.VoiceChannel**)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The lookup strategy is as follows (in order):
| 1. Lookup by ID.
| 2. Lookup by mention.
| 3. Lookup by name

Example:

.. literalinclude:: ../../examples/converter-demo.py
   :language: python3
   :emphasize-lines: 4
   :lines: 48-55


CategoryChannelConvertions (**string** -> **discord.CategoryChannel**)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The lookup strategy is as follows (in order):
| 1. Lookup by ID.
| 2. Lookup by mention.
| 3. Lookup by name

Example:

.. literalinclude:: ../../examples/converter-demo.py
   :language: python3
   :emphasize-lines: 4
   :lines: 58-65


RoleConvertions (**string** -> **discord.Role**)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The lookup strategy is as follows (in order):
| 1. Lookup by ID.
| 2. Lookup by mention.
| 3. Lookup by name

Example:

.. literalinclude:: ../../examples/converter-demo.py
   :language: python3
   :emphasize-lines: 4
   :lines: 68-75


OtherConvertions
~~~~~~~~~~~~~~~~

*  InviteConverter
*  GameConverter
*  ColourConverter
*  EmojiConverter
*  PartialEmojiConverter
