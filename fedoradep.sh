#!/bin/bash
sudo dnf check-update
sudo dnf install build-essential --assumeyes 
sudo dnf install python3 --assumeyes
sudo dnf install libpoppler-cpp-dev pkg-config python-dev python3-pip --assumeyes
sudo dnf install figlet --assumeyes
sudo dnf install unoconv --assumeyes
pip install pdftotext 
sudo dnf check-update
