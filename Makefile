test:
	python3 test_minidoc.py -v

code:
	vim -c 'so proj.vim'

sdist:
	python3 setup.py sdist
