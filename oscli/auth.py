import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG)
_log = logging.getLogger(__name__)


def fetch_token(username: str, password: str):
    logging.info('Trying to get auth token with username & password pair...')

    with requests.post('https://www.opensubtitles.com/api/v1/login',
                       json={
                           "username": username,
                           "password": password
                       },
                       headers={
                           "Accept": "application/json",
                           "Content-Type": "application/json"
                       }) as response:

        logging.info(f'Got a response. Status: {response.status_code}')

        if response.status_code == 200:
            logging.info('Returning the token...')
            return json.loads(response.content)['token']

        logging.error('Failed to fetch the auth token.')
        logging.debug(f'Server response: {json.loads(response.content)}')
