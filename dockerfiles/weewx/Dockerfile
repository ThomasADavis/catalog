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
ADD build.sh /

RUN ./build.sh

VOLUME /glusterfs/ec0/weather
VOLUME /glusterfs/ec0/weewx

WORKDIR /glusterfs/ec0/weewx
ENV PYTHONPATH /glusterfs/ec0/weewx

ENTRYPOINT ["/bin/sh"]
