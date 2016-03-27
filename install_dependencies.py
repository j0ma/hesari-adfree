# install_dependencies.py
# Installs required non-stdlib python 
# libraries for running hesari_adfree.py

# NOTE: REQUIRES pip!
# (c) j0ma, 2016

import os
import sys

# install function
def install_libraries(libraries):
    os.system("clear")
    print "Starting..."
    for lib in libraries:
        print "Installing: %s" % lib
        cmd = "sudo pip install %s" % lib
        os.system(cmd)

def main():

    # libraries to install
    libs_to_install = ["lxml", "requests", "feedparser"]
    
    # install
    install_libraries(libs_to_install)

if __name__ == "__main__":
    main()
