##
## Dockerfile.centos
##
FROM centos
MAINTAINER clwhitney@lbl.gov

RUN mkdir -p /opt/weewx

RUN adduser -U -u 642 -d /opt/weewx -c "Weather Station,,," -M weewx && chmod 755 /opt/weewx

ADD requirements.txt /opt/weewx
ADD run_weewx.sh /opt/weewx
ADD weewx.conf /opt/weewx
ADD /glusterfs/ec0/weewx/ncsv-0.4.1.tgz /opt/weewx
ADD build.sh /

RUN ./build.sh

VOLUME /glusterfs/ec0

#WORKDIR /glusterfs/ec0/weewx
#ENV PYTHONPATH /glusterfs/ec0/weewx

WORKDIR /opt/weewx
ENV PYTHONPATH /opt/weewx

ENTRYPOINT ["/bin/sh"]
