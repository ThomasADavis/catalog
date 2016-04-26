#!/bin/bash
if [ ! -d pulsar ] ; then
    git clone https://boverhof@bitbucket.org/crtsensors/pulsar.git
fi
if [ ! -d pulsar-docker ] ; then
    git clone https://boverhof@bitbucket.org/crtsensors/pulsar-docker.git
fi

if [ ! -x "get-pip.py" ] ; then
    curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
    chmod 755 get-pip.py
fi

docker build -t test/pulsar_worker:0.1 .
