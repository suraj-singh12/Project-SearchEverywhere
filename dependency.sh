#!/bin/bash

#for Arch Linux manjaro endeavouros etc
function If_pacman () {
    sudo pacman -Sy base-devel python3 figlet poppler-glib python-pip unoconv --noconfirm
    pip install pdftotext
    exit 0
}

#for debian & other debian-based distros 
function If_apt () {
    sudo apt update
    sudo apt install build-essential python3 libpoppler-cpp-dev pkg-config libpython3-dev python3-pip figlet poppler-utils unoconv -y 
    pip install pdftotext 
    exit 0
}

#for Void Linux
function If_xbps () {
    sudo xbps-install -Syu
    sudo xbps-install base-devel python3 python3-pip figlet poppler-glib unoconv -y
    pip install wheel pdftotext
    exit 0
}

#for Redhat, CentOS, Fedora, Oracle Linux etc
function If_dnf () {
    sudo dnf check-update 
    sudo yum install python3 gcc-c++ pkgconfig poppler-cpp-devel python3-devel figlet unoconv -y
    pip install pdftotext 
    exit 0
}

# detect the package manager and call the required function to make installation of dependencies
type apt 1>/dev/null 2>&1 && If_apt
type xbps 1>/dev/null 2>&1 && If_xbps
type dnf 1>/dev/null 2>&1 && If_dnf
type pacman 1>/dev/null 2>&1 && If_pacman
