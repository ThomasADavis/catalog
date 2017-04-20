#!/bin/sh

apk add --update python py-pip openssl ca-certificates util-linux
apk add --update --virtual build-dependencies build-base git autoconf libtool automake fuse-dev swig python python-dev perl-dev avahi-dev py-pip linux-headers

# mkdir -p /application

cd /opt/snmp
mkdir tmp
cd tmp
wget https://www.ibr.cs.tu-bs.de/projects/libsmi/download/libsmi-0.5.0.tar.gz

tar xfv libsmi-0.5.0.tar.gz

cd libsmi-0.5.0

./configure --prefix=/usr --sysconfdir=/etc/ mandir=/usr/share/man --localstatedir=/var --libexecdir=/usr/lib
make
make install

cd /opt/snmp

pip install -r /application/pulsar/src/snmp/requirements.txt

cp /application/pulsar/src/snmp/*py .
cp /application/pulsar/src/snmp/*sh .

mkdir mib
cp /application/pulsar/src/snmp/mib/* mib

#
# Cleanup and remove cruft.
#
apk del build-dependencies
rm -rf /root/.cache /var/cache/apk/APK* /tmp/pip_build_root
rm -rf /opt/snmp/tmp

mkdir /external

