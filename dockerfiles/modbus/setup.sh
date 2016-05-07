#!/bin/bash
REGISTRY_NAME='docker-registry.crt.nersc.gov'
REGISTRY_PORT=5000
DOCKER_IMAGE_NAME="mini/modbus-worker:0.3"

main() {
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

    docker build -t ${DOCKER_IMAGE_NAME} . \
    && docker tag $DOCKER_IMAGE_NAME $REGISTRY_NAME:$REGISTRY_PORT/$DOCKER_IMAGE_NAME \
    && docker push $REGISTRY_NAME:$REGISTRY_PORT/$DOCKER_IMAGE_NAME
}

main