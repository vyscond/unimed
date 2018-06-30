python=env/bin/python

test:
	$(python) test.py

test_install:
	virtualenv testenv
	source testenv/bin/activate && pip install .

