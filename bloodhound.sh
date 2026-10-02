#!/bin/bash
RED='\033[0;31m'
NC='\033[0m'
echo -e "${RED}1 Installing Bloodhound${NC}"
echo ""
wget https://github.com/SpecterOps/bloodhound-cli/releases/latest/download/bloodhound-cli-linux-amd64.tar.gz
echo ""
echo -e "${RED}2 tar -xvzf bloodhound-cli-linux-amd64.tar.gz${NC}"
tar -xvzf bloodhound-cli-linux-amd64.tar.gz
echo ""
echo -e "${RED}3 sudo ./bloodhound-cli install${NC}"
sudo ./bloodhound-cli install
echo ""
echo -e "${RED}Run sudo ./bloodhound-cli up ${NC}"
echo -e "${RED}visit 127.0.0.1:8080/ui/login${NC}"
echo -e "${RED}username : admin${NC}"
echo -e "${RED}To check password : sudo ./bloodhound-cli config${NC}"
echo -e "${RED}If docker based error run${NC}"
echo -e "${RED}sudo apt update${NC}"
echo -e "${RED}sudo apt install -y docker.io docker-compose${NC}"
