To use this repo:

1) Create a new virtual environment:
	./make_virtual_env.sh

2) Switch to this virtual environment:
	source ./use_virtual_env.sh

3) Install required packages:
	pip install -r requirements.txt

4) Run the test:
	python sample-oauth.py


The sample-oauth.py defines a number of variables that need to be updated for your environment such as the client id, client secret, token url, and the resource url for the resource secured via OAuth2.