commit:
	git commit -a
	git push -u origin main
format:
	black src/dearaj/*.py
clean:
	rm -rf src/dearaj/__pycache__