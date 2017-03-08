############################################################
# Dockerfile to build Python MODBUS Application Containers
# 
############################################################
FROM gliderlabs/alpine:3.4
MAINTAINER Joshua Boverhof

# Update the sources list
#ADD repositories /etc/apk/repositories
RUN apk add --update tar python python-dev py-pip

# Copy the folder inside the container
RUN mkdir /application
RUN mkdir /application/config
ADD pulsar /application/pulsar
#ADD get-pip.py /application/
ADD pulsar-docker/downloads /application/downloads
ADD requirements.txt /application/config/
WORKDIR /application

#RUN python get-pip.py
RUN tar xf /application/downloads/mblogic_all_2011-04-16.tar.gz
RUN tar xf mblogic_all/mbtools_2011-01-07.tar.gz
#RUN tar xf /application/downloads/mysql-connector-python-2.1.3.tar.gz
#RUN ( cd mysql-connector-python-2.1.3 && python setup.py install )
RUN pip install  -r /application/config/requirements.txt --allow-external mysql-connector-python

# ENVIRONMENT
ENV PYTHONPATH "/application/mbtools_2011-01-07/mbprobe:/application/pulsar/src:/application/mbtools_2011-01-07/pollmb"

# Set the default command to execute
ENTRYPOINT ["./pulsar/scripts/pulsar_worker.py"]
#CMD ["--help"]
