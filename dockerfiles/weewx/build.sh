#!/bin/sh

cd /etc
rm /etc/localtime
ln -s ../usr/share/zoneinfo/America/Los_Angeles localtime

yum makecache -y
yum install -y --nogpgcheck epel-release
yum makecache -y
yum install -y --nogpgcheck python-pip
