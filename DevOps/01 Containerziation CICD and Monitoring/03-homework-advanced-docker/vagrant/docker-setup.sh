#!/bin/bash

echo "* Prepare system and install docker..."
sudo apt update -y
sudo apt install -y apt-transport-https ca-certificates curl tree software-properties-common git
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
apt-cache policy docker-ce
sudo apt install -y docker-ce

echo "* Setup docker group"
sudo groupadd docker
sudo chmod 666 /var/run/docker.sock
sudo usermod -aG docker vagrant
su - vagrant

echo "* Enable and start Docker ..."
sudo systemctl enable docker
sudo systemctl start docker

echo "* Enable firewall, open ports ..."
sudo ufw allow 2376/tcp
sudo ufw allow 2377/tcp
sudo ufw allow 7946/tcp
sudo ufw allow 7946/udp
sudo ufw allow 4789/udp
sudo ufw allow 8080/tcp
sudo ufw reload

echo "* Add hosts ..."
echo "192.168.99.100 docker1.do1.lab docker1" >> /etc/hosts
echo "192.168.99.101 docker2.do1.lab docker2" >> /etc/hosts
echo "192.168.99.102 docker3.do1.lab docker3" >> /etc/hosts

sudo systemctl restart docker
sleep 3