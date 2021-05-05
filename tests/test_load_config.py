from app.load_config import get_config


def test_load_config():
    assert get_config() == {}
