#!/bin/sh

docker run -it --net host -v /home/tdavis/:/external docker-registry.crt.nersc.gov:5000/alpine/ion-web-scrape:0.2
