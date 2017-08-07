#!/bin/sh

apk add --update python py-pip openssl ca-certificates tzdata redis
apk add --update --virtual build-dependencies build-base git autoconf libtool automake fuse-dev swig python python-dev perl-dev avahi-dev py-pip linux-headers

cp /usr/share/zoneinfo/US/Pacific /etc/localtime
echo "US/Pacific" > /etc/timezone

pip install -r /opt/bacnet/requirements.txt

cd /opt/bacnet

git clone https://github.com/ThomasADavis/pybacnet.git

cd /opt/bacnet/pybacnet/src

git clone https://github.com/ThomasADavis/bacnet-stack.git

mv bacnet-stack bacnet-stack-0.8.3

#
# pybacnet needs a file from bacnet-stack to compile correctly..
#

cp bacnet-stack-0.8.3/demo/object/device-client.c pybacnet/

cd bacnet-stack-0.8.3

make all

cd ..

python setup.py build
python setup.py install

cd /opt/bacnet 

cp /application/pulsar/src/bacnet/*py .
cp /application/pulsar/src/bacnet/*sh .

#
# Cleanup and remove cruft.
#
apk del build-dependencies
rm -rf /root/.cache /var/cache/apk/APK* /tmp/pip_build_root
#
#mkdir -p /application/config
mkdir /external

