#!/bin/sh

pip install  pyserial
pip install  pyusb

yum install -y --nogpgcheck wget
yum install -y --nogpgcheck perl
yum install -y --nogpgcheck glusterfs-fuse

cd /opt/weewx
wget -r --no-parent http://weewx.com/downloads/weewx-3.8.2-1.rhel.noarch.rpm
rpm -i weewx.com/downloads/weewx-3.8.2-1.rhel.noarch.rpm

pip install -r /opt/weewx/requirements.txt

wee_extension --install ncsv-0.4.1.tgz

cd /opt/weewx 
cp weewx.conf /etc/weewx/weewx.conf
