import pytest
import re
import discord


@pytest.mark.asyncio
async def test_member_converter(msg):
    member = await Convert(msg, "TestUser", discord.Member)

    assert isinstance(member, discord.Member)
    assert member.name == "TestUser"
