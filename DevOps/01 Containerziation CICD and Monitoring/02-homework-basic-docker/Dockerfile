FROM centos:7

RUN yum update -y
RUN yum install -y httpd

COPY . /var/www/html/

ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]
