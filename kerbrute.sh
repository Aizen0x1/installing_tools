#!/bin/bash
RED='\033[0;31m'
NC='\033[0m'
echo -e "${RED}1 Installing Kerbrute${NC}"
echo ""
wget https://github.com/ropnop/kerbrute/releases/latest/download/kerbrute_linux_amd64 -O kerbrute
echo ""
echo -e "${RED}2 Changing mode {chmod +x kerbrute}${NC}"
chmod +x kerbrute
