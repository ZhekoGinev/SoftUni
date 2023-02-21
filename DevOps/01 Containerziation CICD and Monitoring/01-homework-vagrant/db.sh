#!/bin/bash

echo "* Add hosts ..."
echo "192.168.89.100 web.do1.lab web" >> /etc/hosts
echo "192.168.89.101 db.do1.lab db" >> /etc/hosts

echo "* Install Software ..."
sudo apt update
sudo apt install -y mariadb-server mariadb-client

echo "* Start HTTP ..."
sudo systemctl enable mariadb
sudo systemctl start mariadb

echo "* Firewall - open port 3306 ..."
sudo ufw allow 3306
sudo ufw reload

echo "* Create and load the database ..."
mysql -u root < /vagrant/db_setup.sql

echo "* fixing bind address 127.0.0.1 > 0.0.0.0 *"
sudo cp /vagrant/50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf
sudo systemctl restart mariadb
