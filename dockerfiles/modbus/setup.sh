#!/bin/bash
set -e
REGISTRY_NAME='docker-registry.crt.nersc.gov'
REGISTRY_PORT=5000
DOCKER_IMAGE_NAME="alpine/modbus-worker:0.17"

main() {
    if [ ! -d pulsar ] ; then
        #git clone git@bitbucket.org:crtsensors/pulsar.git
        git clone https://bitbucket.org/crtsensors/pulsar.git
    else
        ( cd pulsar && git pull )
    fi

    if [ ! -d pulsar-docker ] ; then
        #git clone git@bitbucket.org:crtsensors/pulsar-docker.git
        git clone https://bitbucket.org/crtsensors/pulsar-docker.git
    fi

    if [ ! -x "get-pip.py" ] ; then
        curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
        chmod 755 get-pip.py
    fi

    docker build -t ${DOCKER_IMAGE_NAME} .
    echo ">>> RUN TEST"
    docker run --rm --name=pulsar_test1 -w /application/pulsar/test --entrypoint=python -ti $DOCKER_IMAGE_NAME -m unittest crt_modbus_mock_test

    echo ">>> TAG AND PUSH"
    docker tag $DOCKER_IMAGE_NAME $REGISTRY_NAME:$REGISTRY_PORT/$DOCKER_IMAGE_NAME
    docker push $REGISTRY_NAME:$REGISTRY_PORT/$DOCKER_IMAGE_NAME
}

main
