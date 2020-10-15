import pytest
from oscli.config import Config


class TestConfig:
    def test_create(self):
        cfg = Config()
        cfg.create()
