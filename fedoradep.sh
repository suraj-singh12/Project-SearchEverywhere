#!/bin/bash
sudo dnf check-update 
sudo dnf install python3 -y
sudo yum install gcc-c++ pkgconfig poppler-cpp-devel python3-devel
sudo dnf install figlet -y
sudo dnf install unoconv -y
pip install pdftotext 
sudo dnf check-update
