#!/bin/bash

# Kulay para sa Installer
G='\e[92m'
R='\e[91m'
W='\e[0m'

clear
echo -e "${G}=========================================="
echo -e "      EDRIAN TOOLKIT - INSTALLER          "
echo -e "==========================================${W}"

echo -e "[*] Installing dependencies..."
pkg update && pkg upgrade -y
pkg install python figlet neofetch termux-api curl -y

echo -e "[*] Setting up directories..."
mkdir -p ~/mytools

echo -e "[*] Creating shortcuts..."
# Ginagawa nito ang shortcut para sa 'edrian-tool'
echo "alias edrian-tool='python ~/mytools/edrian-tool.py'" >> ~/.bashrc

echo -e "${G}[+] Installation Complete!${W}"
echo -e "Mangyaring i-restart ang Termux o i-type ang: ${R}source ~/.bashrc${W}"
echo -e "Pagkatapos, i-type ang: ${G}edrian-tool${W}"
