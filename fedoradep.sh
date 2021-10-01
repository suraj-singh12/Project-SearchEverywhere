#!/bin/bash
sudo dnf check-update
sudo dnf install build-essential -y 
sudo dnf install python3 -y
sudo dnf install libpoppler-cpp-dev pkg-config python-dev python3-pip -y
sudo dnf install figlet -y
sudo dnf install unoconv -y
pip install pdftotext 
sudo dnf check-update
