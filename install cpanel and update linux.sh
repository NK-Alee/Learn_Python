#!/bin/bash
# Update the system
sudo apt update
sudo apt upgrade
# install python
sudo apt install python3
sudo apt install python3-pip
echo "Update and python installed"
sleep 5
# Config SSH Port 
read -p "Enter the new SSH port: " port
sudo sed -i "s/#Port 22/Port $port /g" /etc/ssh/sshd_config
sudo sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/g' /etc/ssh/sshd_config
sudo sed -i "s/#AuthorizedKeysFile[[:space:]]\+.ssh\/authorized_keys[[:space:]]\+.ssh\/authorized_keys2/AuthorizedKeysFile     .ssh\/authorized_keys .ssh\/authorized_keys2/g" /etc/ssh/sshd_config
echo "SSH port changed to $port"
sleep 5
# Create and copy key public ssh   
sudo ssh-keygen -t rsa -b 4096 
# Create dictionary .ssh and copy keyprivate ssh to root user 
sudo cp ~/.ssh/id_rsa.pub /root/.ssh/authorized_keys
sudo chmod 600 /root/.ssh/authorized_keys
sudo chmod 700 /root/.ssh
echo "SSH KEY CREATED AND COPIED TO ROOT USER"
sleep 5
# install cpanel
clear
echo "Installing cpanel"
cd /home && curl -o latest -L https://securedownloads.cpanel.net/latest && sh latest
echo "Cpanel installed successfully"
sleep 10
# enable ufw open port ssh
sudo ufw enable
sudo ufw allow $port #< port ssh
# cpanel port enable
sudo ufw allow 1
sudo ufw allow 7
sudo ufw allow 20
sudo ufw allow 21
sudo ufw allow 22
sudo ufw allow 25
sudo ufw allow 26 
sudo ufw allow 37
sudo ufw allow 43
sudo ufw allow 53
sudo ufw allow 80
sudo ufw allow 110
sudo ufw allow 113
sudo ufw allow 143
sudo ufw allow 443
sudo ufw allow 465
sudo ufw allow 579
sudo ufw allow 587
sudo ufw allow 783
sudo ufw allow 873
sudo ufw allow 953
sudo ufw allow 993
sudo ufw allow 995
sudo ufw allow 2077
sudo ufw allow 2078
sudo ufw allow 2079
sudo ufw allow 2080
sudo ufw allow 2082
sudo ufw allow 2083
sudo ufw allow 2086
sudo ufw allow 2087
sudo ufw allow 2089
sudo ufw allow 2095
sudo ufw allow 2096
sudo ufw allow 2195
sudo ufw allow 2703
sudo ufw allow 3306
sudo ufw allow 6277
sudo ufw allow 11371
sudo ufw allow 24441
echo "Cpanel installed and firewall enabled"
# show key private ssh
echo "Your private key is: "
sudo cat ~/.ssh/id_rsa 
# Restart ssh service
sudo systemctl restart ssh
echo "restart ssh service"