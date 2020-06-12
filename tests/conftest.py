# For pytest
#
# Tested on:
#  | pytest          5.4.2
#  | pytest-asyncio  0.12.0
#  | dpytest         0.0.20
#
import src.discordRebot as rebot
import discord.ext.test as dpytest  # pip install dpytest
import pytest  # pip install pytest pytest-asyncio


def pytest_configure():
    """To pass pytest.rebot and pytest.dpytest to all tests"""
    pytest.rebot = rebot
    pytest.dpytest = dpytest
