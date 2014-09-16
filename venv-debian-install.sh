#!/bin/sh

# Install the Ubuntu system packages dependencies of this project for the production environment
cat requirements.apt | grep -v "#" | xargs sudo apt-get install -y

# Install the python dependencies of this project for the production environment
# for local development or test , do:
# local development:
# pip install -r requirements/local.txt
# test:
# pip install -r requirements/test.txt
pip install -r requirements.txt
