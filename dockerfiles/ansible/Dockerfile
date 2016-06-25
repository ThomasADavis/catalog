############################################################
# Dockerfile to build Ansible Master
# 
############################################################
FROM centos
MAINTAINER Joshua Boverhof

# Update the sources list
ADD master /opt/ansible/master/
ADD nodes /opt/ansible/nodes/
RUN mkdir /application
WORKDIR /application
RUN yum update -y
RUN yum install -y wget
RUN wget -r --no-parent -A 'epel-release-*.rpm' http://dl.fedoraproject.org/pub/epel/7/x86_64/e/
RUN rpm -Uvh dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-*.rpm
RUN yum update -y
RUN yum install -y openssh-clients ansible which 
RUN ( mv /etc/ansible/hosts /etc/ansible/hosts.orig && cp /opt/ansible/master/etc/ansible/hosts /etc/ansible && cp /opt/ansible/master/ansible_id_rsa  . && chmod 400 ansible_id_rsa && mkdir ~/.ssh && cp /opt/ansible/master/known_hosts ~/.ssh )

# Set the default command to execute
ENTRYPOINT ["ansible"]
#CMD ["--help"]
