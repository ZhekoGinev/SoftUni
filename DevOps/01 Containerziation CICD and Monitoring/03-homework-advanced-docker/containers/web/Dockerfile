FROM ubuntu:jammy

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt update && apt install -y nginx
RUN apt-get install -yqq php8.1-fpm && apt install -yq php-mysql

COPY ./default /etc/nginx/sites-available/default
COPY ./www /var/www/html
COPY ./start.sh /start.sh

RUN chmod 777 /start.sh
RUN chmod -R 777 /var/www/html

ENTRYPOINT /start.sh
