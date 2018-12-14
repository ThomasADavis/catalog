#!/bin/sh

apk add --update python py-pip openssl ca-certificates tzdata redis
apk add --update --virtual build-dependencies build-base git autoconf libtool automake fuse-dev swig python python-dev perl-dev avahi-dev py-pip linux-headers

cp /usr/share/zoneinfo/US/Pacific /etc/localtime
echo "US/Pacific" > /etc/timezone

pip install -r /opt/pue/requirements.txt

cd /opt/pue

