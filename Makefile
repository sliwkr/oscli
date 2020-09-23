clean:
	rm -rf dist build oscli.egg-info

deploy:
	python setup.py sdist bdist_wheel
	python3 -m twine upload --repository testpypi dist/*

install:
	pip install --index-url https://test.pypi.org/simple/ oscli

uninstall:
	pip uninstall oscli -y