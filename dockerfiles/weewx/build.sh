#!/bin/sh

yum makecache
yum install epel-release
yum makecache
yum install python-pip

yum install python-configobj
yum install python-cheetah
yum install python-imaging
yum install python-setuptools

pip install --upgrade pip
pip install  pyserial
pip install  pyusb

yum install wget

# mkdir -p /application

#
cd /opt/weewx
wget http://weewx.com/downloads/weewx-3.8.2-1.rhel.noarch.rpm
rpm -i weewx-3.8.2-1.rhel.noarch.rpm

#
#git clone git://git.code.sf.net/p/owfs/code owfs-code
#
#cd owfs-code
#./bootstrap
#./configure --prefix=/usr --disable-usb --disable-w1 --disable-i2c --disable-perl5 --enable-static --disable-zero --disable-avahi
#make
#make install
#
pip install -r /opt/weewx/requirements.txt

cd /opt/weewx 
#rm -rf owfs-code
#
#cp /opt/ionscraper/pulsar/src/scrape/*py .
#cp /opt/ionscraper/pulsar/src/scrape/ion-* .

#
# Cleanup and remove cruft.
#
#apk del build-dependencies
#rm -rf /root/.cache /var/cache/apk/APK* /tmp/pip_build_root
