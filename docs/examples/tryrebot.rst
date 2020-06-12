TryREBOT
========

To host rshell (Remote Shell) and rpy (Remote Python Interpreter) in your machine
which can be accessed in discord using bot.

.. warning::
   Don't forgot to give **auth**, otherwise anyone in your guild can access your rshell and rpy.

**Example:**

``python -m discordRebot.tryrebot $DBToken --rshell 'Roles["Admin"]' --rpy 'Roles["Admin"],'``

.. list-table::
   :widths: 2 3

   * - .. image:: ../_static/img/tryrebot-rshell.jpg
          :width: 400
          :align: left
          :alt: rshell demo

     -  | This runs each command using ``subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE, shell=True)``
        |
        |
        | Every running subprocess is append to ``Shell.processes`` and removed after done. so we can kill any processes like ``Shell.processes[i].kill()``.
        |
        |
        | Each subprocess is running in seperate **Thread**. so we can run many processes parallelly and asynchronously.

   * - .. image:: ../_static/img/tryrebot-rpy.jpg
          :width: 400
          :align: left
          :alt: rpy demo

     - At default the globals and locals is **globals()**. But we can assaign any globals like ``--rpy 'None,{"rebot":client}'``
     
       .. warning::
          It is also possible to change ``Shell.auth`` and ``Exec.auth`` via rpy
