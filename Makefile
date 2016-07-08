test:
	python -m unittest discover tests

publish:
	python setup.py sdist upload

