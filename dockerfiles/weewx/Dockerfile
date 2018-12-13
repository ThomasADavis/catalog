##
## Dockerfile.centos
##
FROM centos
MAINTAINER clwhitney@lbl.gov

RUN mkdir -p /opt/weewx

RUN adduser -U -u 642 -d /opt/weewx -c "Weather Station,,," -M weewx && chmod 755 /opt/weewx

COPY requirements.txt /opt/weewx
COPY run_weewx.sh /opt/weewx
COPY weewx.conf /opt/weewx
COPY ncsv-0.4.1.tgz /opt/weewx
COPY build.sh /
COPY build2.sh /
COPY build3.sh /

RUN ./build.sh
COPY . .

RUN ./build2.sh
COPY . .

RUN ./build3.sh
COPY . .

VOLUME /glusterfs/ec0

WORKDIR /opt/weewx

#WORKDIR /glusterfs/ec0/weewx
#ENV PYTHONPATH /glusterfs/ec0/weewx

ENV PYTHONPATH /opt/weewx

ENTRYPOINT ["/bin/sh"]
