#!/bin/bash
set -e
REGISTRY_NAME='docker-registry.crt.nersc.gov'
REGISTRY_PORT=5000
DOCKER_IMAGE_NAME="alpine/modbus-worker:0.26"

main() {
    if [ ! -d omni-modbus-poller ] ; then
        #git clone git@bitbucket.org:crtsensors/pulsar.git
        git clone --single-branch --branch py2rabbit  https://gitlab.nersc.gov/nersc/otg/omni-modbus-poller.git
    else
        ( cd omni-modbus-poller  && git pull )

    fi

    if [ ! -d omni-modbus-poller/pulsar-docker ] ; then
        ( cd omni-modbus-poller && git submodule update --init --recursive )
    fi

    if [ ! -x "get-pip.py" ] ; then
        curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
        chmod 755 get-pip.py
    fi

    docker build -t ${DOCKER_IMAGE_NAME} .
    echo ">>> RUN TEST"
    docker run --rm --name=omni_modbus_test1 -w /application/omni-modbus-poller/test --entrypoint=python -ti $DOCKER_IMAGE_NAME -m unittest crt_pdu32_modbus_mock_test

    echo ">>> TAG AND PUSH"
    docker tag $DOCKER_IMAGE_NAME $REGISTRY_NAME:$REGISTRY_PORT/$DOCKER_IMAGE_NAME
    docker push $REGISTRY_NAME:$REGISTRY_PORT/$DOCKER_IMAGE_NAME
}

main
