#!/bin/bash

TAG="0.2"
cd rq-dashboard

docker build -t mini/rq-dashboard:$TAG -t mini/rq-dashboard:latest .

docker tag  mini/rq-dashboard:$TAG  docker-registry.crt.nersc.gov:5000/mini/rq-dashboard:$TAG
docker push docker-registry.crt.nersc.gov:5000/mini/rq-dashboard:$TAG

docker tag  mini/rq-dashboard:latest  docker-registry.crt.nersc.gov:5000/mini/rq-dashboard:latest
docker push docker-registry.crt.nersc.gov:5000/mini/rq-dashboard:latest
