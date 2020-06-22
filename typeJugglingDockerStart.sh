#!/bin/bash

# Running Exercise: sudo docker run -it --rm uexpl0it/type-juggling:latest
# From github repository: https://github.com/TROUBLE-1/Type-juggling

sed -i 's/None/All/g' /etc/apache2/apache2.conf
service apache2 start > /dev/null 2>&1 && \
        echo "[#] Challenge can be accessed at: http://$(hostname -I)" && \
        tail -f /dev/null
