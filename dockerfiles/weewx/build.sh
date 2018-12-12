#!/bin/sh

yum makecache -y
yum install -y epel-release
yum makecache -y
yum install -y python-pip

yum install -y python-configobj
yum install -y python-cheetah
yum install -y python-imaging
yum install -y python-setuptools

pip install --upgrade pip
pip install  pyserial
pip install  pyusb

yum install -y wget
yum install -y perl

# mkdir -p /application

#
cd /opt/weewx
wget -r --no-parent http://weewx.com/downloads/weewx-3.8.2-1.rhel.noarch.rpm
rpm -i weewx.com/downloads/weewx-3.8.2-1.rhel.noarch.rpm

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
