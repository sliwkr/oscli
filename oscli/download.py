from oscli.utils import request
from oscli.constants import URL_DOWNLOAD
import json
import os
"""
POST /download {
  "file_id": 186609,
  "file_name": "The.Meg.2018.BDRip.XviD.AC3-EVO",
  "sub_format": "srt"
}
"""
def download(file_id: str=None, file_name: str=None, sub_format: str='srt'):
    post_data = {'sub_format': sub_format}
    if file_id != None:
        post_data['file_id'] = file_id
    if file_name != None:
        post_data['file_name'] = file_name

    resp_json = json.loads(request('post', URL_DOWNLOAD, post_data).text)
    subtitle_dest = f"{os.getcwd()}/{resp_json['fname']}"

    # TODO: simple GET would do here too, GET on url with subtitle link has subtitles in response
    import requests
    with requests.get(resp_json['link'], stream=True) as r:
        r.raise_for_status()
        with open(subtitle_dest, 'wb') as f:
            for chunk in r.iter_content(chunk_size=None):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                if chunk:
                    f.write(chunk)

if __name__ == "__main__":
    response = download('3707257', 'blueyes-pusher3720.srt')
    print(response)