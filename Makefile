all:
	python3 setup.py sdist bdist_wheel
commit:
	git commit -a
	git push -u origin main
format:
	black src/dearaj/*.py
	mypy src/dearaj/*.py
clean:
	rm -rf src/dearaj/__pycache__ dist build src/dearaj.egg-info