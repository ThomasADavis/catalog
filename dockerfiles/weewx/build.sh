#!/bin/sh

cd /etc
rm /etc/localtime
ln -s ../usr/share/zoneinfo/America/Los_Angeles localtime

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

cd /opt/weewx
wget -r --no-parent http://weewx.com/downloads/weewx-3.8.2-1.rhel.noarch.rpm
rpm -i weewx.com/downloads/weewx-3.8.2-1.rhel.noarch.rpm

pip install -r /opt/weewx/requirements.txt

wee_extension --install ncsv-0.4.1.tgz

cd /opt/weewx 
cp weewx.conf /etc/weewx/weewx.conf
