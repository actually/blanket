#!/bin/bash

# This probably only works on Mac OS X, and even then may need finagling.
# I include it more as a bread crumb than a real solution.

sudo easy_install pip
sudo pip install cherrypy
sudo pip install soaplib  # Mac OS X probably already has the latest soaplib

# add something here to install GCC

sudo pip install fabric