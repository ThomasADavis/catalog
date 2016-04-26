############################################################
# Dockerfile to build Python MODBUS Application Containers
# docker run  
#    --name=$i --net=bridge -d -v /root/downloads/:/opt/downloads:rw   
#    -t centos /bin/bash -c "(
#    yum update -y 
#    && cd /root && cp -r /opt/downloads .  
#    && cd downloads 
#    && tar xf mblogic_all_2011-04-16.tar  
#    && cd /root/downloads/mblogic_all 
#    && tar xf mbtools_2011-01-07.tar.gz 
#    && cd /root 
#    && python downloads/get-pip.py 
#    && python downloads/ez_setup.py 
#    && pip install pika==0.9.8 
#    && pip install redis 
#    && pip install mysql-connector-python --allow-external mysql-connector-python 
#    && pip install logstash-formatter 
#    && export PYTHONPATH='/root/downloads/mblogic_all/mbtools_2011-01-07/mbprobe:/root/downloads/pulsar/src' 
#    && cd downloads/pulsar/scripts 
#    && pwd 
#    && python run_collect_modbus_logs.py -s 1 \"$i\" )"
############################################################

# Set the base image
FROM centos

# File Author / Maintainer
MAINTAINER Joshua Boverhof

# Expose ports
#EXPOSE 80

# Update the sources list
RUN yum update -y

# Copy the folder inside the container
RUN mkdir /application
RUN mkdir /application/config
ADD pulsar /application/pulsar
ADD get-pip.py /application/
ADD pulsar-docker/downloads /application/downloads
ADD requirements.txt /application/config/
WORKDIR /application

#RUN rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
#RUN yum install -y python-pip
RUN python get-pip.py
RUN tar xf /application/downloads/mblogic_all_2011-04-16.tar.gz
RUN tar xf mblogic_all/mbtools_2011-01-07.tar.gz
RUN tar xf /application/downloads/mysql-connector-python-2.1.3.tar.gz
RUN ( cd mysql-connector-python-2.1.3 && python setup.py install )
RUN pip install  -r /application/config/requirements.txt --allow-external mysql-connector-python

# ENVIRONMENT
ENV PYTHONPATH "/application/mbtools_2011-01-07/mbprobe:/application/pulsar/src:/application/mbtools_2011-01-07/pollmb"

# Set the default command to execute
ENTRYPOINT ["./pulsar/scripts/pulsar_worker.py"]
#CMD ["--help"]
