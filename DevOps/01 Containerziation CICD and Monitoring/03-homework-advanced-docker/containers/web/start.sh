#!/bin/bash

service php8.1-fpm start

/usr/sbin/nginx -g "daemon off;"
