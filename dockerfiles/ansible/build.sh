#!/bin/bash

#TAG="0.2"
REGISTRY_IP="172.17.0.3"
IMAGE_NAME="ansible-master"

docker rmi nersc/${IMAGE_NAME}

cp ~/.ssh/ansible_id_rsa master/ && chmod +r master/ansible_id_rsa && docker build -t nersc/${IMAGE_NAME} .
rm -f master/ansible_id_rsa

#docker tag  nersc/${IMAGE_NAME}  $REGISTRY_IP:5000/nersc/${IMAGE_NAME}
#docker push $REGISTRY_IP:5000/nersc/${IMAGE_NAME}
