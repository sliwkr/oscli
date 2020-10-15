from oscli import auth, config
import requests


def request(method:str, url:str, post_data: dict=None, **kwargs):
    """
  Generic request method with authentication added.
  Accepts specific request object parameters in kwargs.

  param method: get, post, put, etc.

  param url: url to query
  """
    if method == 'get':
      return requests.get(
        url=url,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": config.Config().read_token()
        },
        **kwargs
      )
    if method == 'post':
      if post_data == None:
        print('post_data is empty, fail')
        return 1

      return requests.post(
        url=url,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": config.Config().read_token()
        },
        json=post_data
      )