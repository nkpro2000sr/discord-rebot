import pytest

rebot = pytest.rebot
dpytest = pytest.dpytest

client = rebot.discord.Client()
dpytest.configure(client)
Convert = rebot.Converter(client)


@pytest.fixture(autouse=True, scope="module")
def set_global(request):
    """To add client and Convert to module globals"""
    request.module.client = client
    request.module.Convert = Convert


@pytest.fixture
async def msg(scope="module"):
    return await dpytest.message("dummy")
