#!/bin/sh

apk add --update python py-pip openssl ca-certificates
apk add --update --virtual build-dependencies build-base git autoconf libtool automake fuse-dev swig python python-dev perl-dev avahi-dev py-pip linux-headers

# mkdir -p /application
#
cd /opt/ionscraper
#
#git clone git://git.code.sf.net/p/owfs/code owfs-code
#
#cd owfs-code
#./bootstrap
#./configure --prefix=/usr --disable-usb --disable-w1 --disable-i2c --disable-perl5 --enable-static --disable-zero --disable-avahi
#make
#make install
#
pip install -r /opt/ionscraper/requirements.txt

cd /opt/ionscraper 
#rm -rf owfs-code
#
cp /opt/ionscraper/pulsar/src/scrape/*py .
cp /opt/ionscraper/pulsar/src/scrape/ion-* .

#
# Cleanup and remove cruft.
#
apk del build-dependencies
rm -rf /root/.cache /var/cache/apk/APK* /tmp/pip_build_root

mkdir /external

