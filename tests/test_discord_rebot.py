import pytest

rebot = pytest.rebot


def test_version():
    assert rebot.__version__ == "0.0.2"
