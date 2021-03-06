[![Latest version on
PyPi](https://badge.fury.io/py/discord-rebot.svg)](https://badge.fury.io/py/discord-rebot)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/discord-rebot.svg)](https://pypi.org/project/discord-rebot/)
[![Documentation
status](https://readthedocs.org/projects/discord-rebot/badge/?version=latest&style=flat-square)](https://discord-rebot.readthedocs.io/en/latest/?badge=latest)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) <!--
[![Downloads](https://pepy.tech/badge/discord-rebot/month)](https://pepy.tech/project/discord-rebot/month)-->
<a href="https://discord-rebot.readthedocs.io">
    <img src="https://raw.githubusercontent.com/nkpro2000sr/discord-rebot/master/docs/_static/img/discordRebot.png"
         alt="discord-rebot logo"
         height="200px"
         align="left">
</a>

# Welcome to discord-rebot (py)

**discordRebot** is a RegEx based command mapping discord BOT framework
with **authorization**.

</br>

## Why discordRebot?

**discordRebot** is easy to use, minimal, and async ready framework
using [discord.py](https://discordpy.readthedocs.io/en/latest "discord.py Documentation")

Most of the bots uses a single prefix, string to match command and args
split by spaces, example `!cmd arg1 arg2`.

But discordRebot uses RegEx for both matching the command and capturing
the arguments. It gives more control over both matching the command and
parsing arguments.

Also, it provides authorization to authorize the author of the message
before executing the command.

## Basic Example

A minimal bot with echo command

```python3
from discordRebot import *

client = discord.Client()
key = Mapper()

@key(re.compile(r"^!echo (.*)$")) # Eg: '!echo hello' -> 'hello'
def echo(msg, string):
    return string
echo.auth = None

client.event(Manager(key).on_message)
import os; client.run(os.environ["DBToken"])
```
You can find more examples in the examples directory.

## Features

*   It also supports  
    *   [generators](https://wiki.python.org/moin/Generators "About Generators")  
    *   [asynchronousfunctions](https://docs.python.org/library/asyncio.html "About Asynchronous Functions")  
    *   [asynchronousgenerators](https://www.python.org/dev/peps/pep-0525 "About Asynchronous Generators")  
    ##### Example:
    ```python3
    @key(re.compile(r"^!ticker (\d*) (\d*)$"))
    async def ticker(msg, delay, to):
        delay, to = int(delay), int(to)
        for i in range(to):
            yield i
            await asyncio.sleep(delay)
    ```

*   Authorizes the message author  
    based on  
    *   user\_id example:`1234567890`  
    *   user\_name example:`'user#1234'`  
    *   roles server *(not applicable for DM)*  
    *   permissions of members in server *(not applicable for DM)*  
    *   custom **Callable[[message], bool]**  
    ##### Example:
    ```python3
    @key("am i authorized ?")
    def amiauthorized(msg):
        return "Authorized"
    amiauthorized.auth = {1234567890, 'user#1234'}
    # only executable by user1 (with id 1234567890) and user2 (with username 'user#1234')
    ```

*   Can match multiple commands with a message  
    ##### Example:
    ```python3
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
    ```

## Links
* [Documentation](https://discord-rebot.readthedocs.io/en/latest/ "discord-rebot.rtfd.io")
* [PyPi](https://pypi.org/project/discord-rebot/ "pip install discord-rebot")

</br></br>
<sup> [discord-reargparse](https://github.com/nkpro2000sr/discord-reargparse) (for full featured Discord Bot with RegEx based argparsing in commands) </sup>
