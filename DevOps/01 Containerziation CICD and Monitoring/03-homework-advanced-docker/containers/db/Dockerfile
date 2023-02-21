FROM ubuntu:latest

RUN apt-get update && apt-get install -y mariadb-server mariadb-client

COPY ./db.sql /db.sql
COPY ./50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf

RUN chmod 644 /db.sql

RUN service mariadb start && mariadb -u root < /db.sql

EXPOSE 3306

CMD ["mysqld", "--user=mysql", "--console"]
