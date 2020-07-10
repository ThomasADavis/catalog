############################################################
# Dockerfile to build Python MODBUS Application Containers
#
############################################################
FROM gliderlabs/alpine:3.9
MAINTAINER Joshua Boverhof

# Update the sources list
#ADD repositories /etc/apk/repositories
RUN apk add --update tar python python-dev py-pip

# Copy the folder inside the container
RUN mkdir /application
RUN mkdir /application/config
WORKDIR /application
ADD omni-modbus-poller/pulsar-docker/downloads /application/downloads
RUN tar xf /application/downloads/mblogic_all_2011-04-16.tar.gz
RUN tar xf mblogic_all/mbtools_2011-01-07.tar.gz
ADD omni-modbus-poller/logging.conf /application/
ADD omni-modbus-poller/requirements.txt /application/
RUN pip install --upgrade pip
RUN pip install  -r /application/requirements.txt
ADD omni-modbus-poller /application/omni-modbus-poller
ADD omni-modbus-poller/logging.conf  /application/omni-modbus-poller/test

# ENVIRONMENT
ENV PYTHONPATH "/application/mbtools_2011-01-07/mbprobe:/application/omni-modbus-poller/src:/application/mbtools_2011-01-07/pollmb"

# Set the default command to execute
ENTRYPOINT ["./omni-modbus-poller/scripts/modbus_rq_worker.py"]
#CMD ["--help"]
