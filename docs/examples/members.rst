Members
=======

Members are the users of bot (or) users in guild which has this bot.

Members can be defined in different ways:

*   id (user_id) eg:``445601328488644610`` *user with user.id 445601328488644610*
*   | name (user_name+user_discriminator) eg:``"nkpro#3766"`` *user with user.name+user.discriminator "nkpro#3766"*
    | > why not simply user_name ? 
    | > because, discord allows users to have same username so to differentiate users with same username user_discriminator is required.
*   roles (roles in guild) eg: ``Roles['Admin']`` *members having 'Admin' role in any guild*
*   permissions (permissions in guild) eg: ``Permissions['administrator']`` *member having 'Administrator' permission in any guild*
*   name pattern (pattern(user_name+user_discriminator)) eg:``re.pattern("^nkpro#")`` *user with user.name "nkpro"*
*   callable (custom definitions)

Roles
-----

To group members based on roles in guild requires both **guild-id and role-name** or **role-id** *(since role-id is unique)*

Some examples:

.. list-table::
   :widths: 2 3

   * - ``Roles['Admin', 'Mod']`` 
     - Members with both 'Admin' and 'Mod' roles in any guild
   * - ``Roles[12345, 67890]``
     - Members with both roles with id 12345 and 67890
   * - ``{Roles['Admin'], Roles[12345]}``
     - Members with 'Admin' role in any guild (or) with role id 12345 (or) with both
   * - ``Roles(123456789)['Admin', 67890]``
     - Members with both roles 'Admin' and id:67890 in guild with id:123456789

Permissions
-----------

To group members based on permissions in guild requires both **permissions and guild-id**

``Permissions(guildID, 123, administrator=False, manage_guild=True)`` is similar to ::

   p1 =  discord.permissions.Permissions(123, administrator=False, manage_guild=True)
   p1.guild_id = guildID

.. note::
   ``Permissions(guildID, 123, administrator=False, manage_guild=True)`` is same as ``Permissions(guildID)[123, '!administrator', 'manage_guild']``

Some examples:

.. list-table::
   :widths: 2 3

   * - ``Permissions['manage_guild', 'manage_roles']`` 
     - Members with both 'Manage Server' and 'Manage Roles' permissions in any guild
   * - ``Permissions[268435488]``
     - Members with both 'Manage Server' and 'Manage Roles' permissions in any guild
   * - ``{Permissions['manage_channels'], Permissions[268435456]}``
     - Members with 'Manage Channels' permission in any guild (or) 'Manage Roles' permission in any guild (or) with both
   * - ``Permissions(123456789)['administrator']``
     - Members with 'Administrator' permission in guild with id:123456789


Example
-------

.. code-block:: python3

   >>> groups = Members({'Admin':{Permissions['administrator'], "mybot#1234"},
   ...                   'Mod':{Roles['Moderators']},
   ...                   'users':{1234567890, "user#1234"}
   ...                   })
   >>> groups
   MemberGroups({'Admin': {<Permissions guild_id=None value=8>, 'mybot#1234'}, 'Mod': {<Roles guild_id=None roles=('Moderators',)>}, 'users': {1234567890, 'user#1234'}})
   
   >>> admins = groups['Admin'] # {Permissions['administrator'], "mybot#1234"}
   >>> admins
   Members({<Permissions guild_id=None value=8>, 'mybot#1234'})
   
   >>> only_admins = groups['Admin'] - {"mybot#1234"} # {Permissions['administrator']}
   >>> only_admins
   Members({<Permissions guild_id=None value=8>})
   
   >>> non_admins = groups['Mod']|groups['users'] # {Roles['Moderators'], 1234567890, "user#1234"}
   >>> non_admins
   Members({1234567890, <Roles guild_id=None roles=('Moderators',)>, 'user#1234'})

.. code-block:: python3

   >>> level = Members([{"nkpro#3766"},{Permissions['administrator']},{Roles['Moderators']},{1234567890,"user#1234"}])
   >>> level
   MemberGroups([{'nkpro#3766'}, {<Permissions guild_id=None value=8>}, {<Roles guild_id=None roles=('Moderators',)>}, {'user#1234', 1234567890}])
   >>> owner = level[0]
   >>> owner
   Members({'nkpro#3766'})
   >>> admins = level[1]
   >>> admins
   Members({<Permissions guild_id=None value=8>})
   >>> privileged_users = level[0:2]
   >>> privileged_users
   Members({<Permissions guild_id=None value=8>, 'nkpro#3766'})
   >>> all_users = level[:]
   >>> all_users
   Members({'user#1234', 1234567890, 'nkpro#3766', <Roles guild_id=None roles=('Moderators',)>,<Permissions guild_id=None value=8>})
   >>> all_users.members == level.members
   True
