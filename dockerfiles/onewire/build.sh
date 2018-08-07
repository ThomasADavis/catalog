#!/bin/sh

apk add --update python py-pip openssl ca-certificates redis tzdata
apk add --update --virtual build-dependencies build-base git autoconf libtool automake fuse-dev swig python python-dev perl-dev avahi-dev py-pip linux-headers

# mkdir -p /application

cp /usr/share/zoneinfo/US/Pacific /etc/localtime
echo "US/Pacific" > /etc/timezone

cd /opt/onewire

git clone https://github.com/owfs/owfs.git owfs-code

cd owfs-code
./bootstrap
./configure --prefix=/usr --disable-usb --disable-w1 --disable-i2c --disable-perl5 --enable-static --disable-zero --disable-avahi
make
make install

pip install -r /application/config/requirements.txt

cd /opt/python-consul
python setup.py install

cd /opt/onewire 
rm -rf owfs-code

cp /application/pulsar/src/onewire/*py .
cp /application/pulsar/src/onewire/*sh .

#
# Cleanup and remove cruft.
#
apk del build-dependencies
rm -rf /root/.cache /var/cache/apk/APK* /tmp/pip_build_root

mkdir -p /application/config
mkdir /external

