#!/bin/sh

docker run -it --net host -v /home/tdavis/:/external alpine/ion-web-scrape:0.2
