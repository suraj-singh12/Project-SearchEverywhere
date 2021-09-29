#!/bin/bash
sudo apt update
sudo apt install build-essential -y 
sudo apt install python3 -y
sudo apt install libpoppler-cpp-dev pkg-config python-dev python3-pip -y
sudo apt install figlet -y
sudo apt install unoconv -y
pip install pdftotext 
sudo apt update

sudo cp dist/SearchEverywhere /usr/bin/
sudo apt update
figlet "Install Success"
echo "Write   SearchEverywhere --help   to know about the functioning of the program"
echo "You may like to test the program on given sample files"
echo "Contributions in code are always welcome. If any bug is found, kindly start an issue here https://github.com/suraj-singh12/Project-SearchEverywhere "
