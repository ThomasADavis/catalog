#!/bin/sh

PATH=/sbin:/usr/sbin:/bin:/usr/bin
WEEWX_BIN=/usr/bin/weewxd
WEEWX_CFG=/etc/weewx/weewx.conf
WEEWX_USER=weewx.weewx
NAME=weewx
PIDFILE=/opt/weewx/$NAME.pid
LOCKFILE=/opt/weewx/$NAME
DAEMON_ARGS="--pidfile=$PIDFILE $WEEWX_CFG"

$WEEWX_BIN $DAEMON_ARGS 
