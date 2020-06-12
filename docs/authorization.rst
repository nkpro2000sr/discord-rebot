Command Authorization
=====================

Each command is authorized using :func:`discordRebot.manager.AuthorizeCallBack`. 

Which checks for function attributes

* auth `(members) <examples/members.html#members>`_
* has_roles `(roles) <examples/members.html#roles>`_
* has_permissions `(permissions) <examples/members.html#permissions>`_

And each attribute is authorized using :func:`discordRebot.manager.Authorize`.

Example::

   Fn.auth = groups['AllUser']
   Fn.has_roles = Roles['Admin']
   
   # Authorizes all users who both **belong to a group** and **having admin role**

.. advanced_hacky_usecase

   actualy auth, has_roles and has_permissions works similar.
   so you can use them as 'and' condition.
   
   Example::
   
      Fn.auth = groups['AllUser']
      Fn.has_roles = level[0]
      Fn.has_permissions = lambda msg: not msg.author.bot
      
      # Authorizes all not bot users who belongs to (groups['AllUser'] <set_intersection> level[0])
