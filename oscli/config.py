from pathlib import Path
import logging
import configparser
import time

logging.basicConfig(level=logging.DEBUG)
_log = logging.getLogger(__name__)


class Config:
    def __init__(self, filepath='~/.oscli'):
        self.config_path = Path(filepath).expanduser().absolute()
        if (not self.config_path.is_file()):
            self.create()

        self.config = configparser.ConfigParser({'token': '', 'expires': ''})
        self.config.read(self.config_path)

    def create(self):
        _log.info(f'Creating new user config at {self.config_path}...')
        self.config_path.touch(0o600)
        # TODO: not needed, just write ConfigParser straight to file
        self.config_path.write_text(
            data="[auth]\ntoken = ''\nexpires = ''\n\n", encoding='utf-8')
        _log.info('OK.')

    def read_token(self):
        """
        Returns saved auth token from config file.
        """
        return self.config.get('auth', 'token')

    def update(self):
        pass

    def save_token(self, token):
        self.config.set('auth', 'token', token)
        # self.config.set('secrets', 'timestamp', ) # TODO: set time.now()
        with open(self.config_path, mode='w') as config_fd:
            _log.info(f'Writing new config to {self.config_path}...')
            self.config.write(config_fd)
        _log.info('OK.')


if __name__ == "__main__":
    stuff = Config()
