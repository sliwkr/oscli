import json
from oscli.utils import request
from oscli.constants import URL_FIND

def find(query, language='en'):
    return request('get', f"{URL_FIND}?query={query}&languages={language}")

if __name__ == "__main__":
    response = json.loads(find('Mr.Robot.S01E01').text)
    print(response)