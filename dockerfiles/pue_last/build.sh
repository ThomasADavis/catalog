#!/bin/sh

apk add --update python py-pip openssl ca-certificates tzdata redis

cp /usr/share/zoneinfo/US/Pacific /etc/localtime
echo "US/Pacific" > /etc/timezone

pip install -r /opt/pue/requirements.txt

cd /opt/pue

