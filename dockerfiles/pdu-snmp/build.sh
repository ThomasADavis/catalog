#!/bin/sh

apk add --update python py-pip openssl ca-certificates
apk add --update --virtual build-dependencies build-base git autoconf libtool automake fuse-dev swig python python-dev perl-dev avahi-dev py-pip linux-headers

# mkdir -p /application

cd /opt/snmp

pip install -r /application/pulsar/src/snmp/requirements.txt

cp /application/pulsar/src/snmp/*py .
cp /application/pulsar/src/snmp/*sh .

#
# Cleanup and remove cruft.
#
apk del build-dependencies
rm -rf /root/.cache /var/cache/apk/APK* /tmp/pip_build_root

mkdir /external

