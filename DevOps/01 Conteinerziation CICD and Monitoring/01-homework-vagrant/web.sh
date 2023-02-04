#!/bin/bash

echo "* Add hosts ..."
echo "192.168.89.100 web.do1.lab web" >> /etc/hosts
echo "192.168.89.101 db.do1.lab db" >> /etc/hosts

echo "* Install Software ..."
sudo apt update
sudo apt install -y apache2 php php-mysqlnd git

echo "* Start HTTP ..."
sudo systemctl enable apache2
sudo systemctl start apache2

echo "* Firewall - open port 80 ..."
sudo ufw allow 80
sudo ufw allow "Apache"
sudo ufw reload

echo "* Copy web site files to /var/www/html/ ..."
sudo mv /var/www/html/index.html /var/www/html/index.html.old
sudo cp /vagrant/* /var/www/html/
