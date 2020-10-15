clean:
	rm -rf dist build oscli.egg-info

release_test:
	python setup.py sdist bdist_wheel
	python3 -m twine upload --repository testpypi dist/*

release:
	python setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

install:
	pip install --editable .

uninstall:
	pip uninstall oscli -y