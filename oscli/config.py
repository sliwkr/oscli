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

        self.config = configparser.ConfigParser()  # TODO: {'token': '', 'expires': ''}
        self.config.read(self.config_path)

    def create(self):
        _log.info(f'Creating new user config at {self.config_path}...')
        self.config_path.touch(0o600)
        # TODO: not needed, just write ConfigParser straight to file
        self.config_path.write_text(
            data="[auth]username = ''\npassword = ''\ntoken = ''\ntimestamp = ''\n\n", encoding='utf-8')
        _log.info('OK.')

    def read_token(self):
        """
        Returns saved auth token from config file.
        """
        return self.config.get('auth', 'token')

    def save(self):
        _log.info('Saving user config...')
        with open(self.config_path, mode='w') as config_fd:
            self.config.write(config_fd)
        _log.info('OK.')

    def update_token(self, token):
        self.config.set('auth', 'token', token)
        self._update_timestamp()

    def update_username(self, username):
        self.config.set('auth', 'username', username)

    def update_password(self, password):
        self.config.set('auth', 'password', password)

    def _update_timestamp(self):
        self.config.set('auth', 'timestamp', str(int(time.time())))

    def is_token_valid(self) -> bool:
        timestamp = self.config.get('auth', 'timestamp')
        if timestamp == "''":
            return False
        return int(time.time()) - int(timestamp) > 7200

if __name__ == "__main__":
    stuff = Config()
