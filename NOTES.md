
2.
GET /find
    ?moviehash=753a8b67fefa64c7
    &query=Mr.Robot.S01E04
    &languages=pl

2.1 resp['data'][0]['attributes']['feature_details']['movie_name'] (optional)
    resp['data'][0]['attributes']['files'][0]['file_id']
    resp['data'][0]['attributes']['files'][0]['file_name']

3.
POST /download {
  "file_id": 186609,
  "file_name": "The.Meg.2018.BDRip.XviD.AC3-EVO",
  "sub_format": "srt"
}

3.1 
    resp['link']
    resp['allowed']
    resp['remaining']

https://www.opensubtitles.com/docs/api/html/index.htm#getting-started
https://github.com/billnapier/mp4file/blob/master/src/mp4file/atom.py
https://packaging.python.org/guides/using-testpypi/
https://realpython.com/python-interface/#using-abcabcmeta
https://www.yegor256.com/2016/04/19/object-must-not-be-configurable.html
https://www.yegor256.com/2014/11/20/seven-virtues-of-good-object.html

python3 setup.py sdist bdist_wheel
python3 -m pip install --user twine python-dateutil
python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload dist/*

pip install --index-url https://test.pypi.org/simple/ oscli

todo: dependencies
click
pytest