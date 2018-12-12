##
## Dockerfile.alpine
##
FROM alpine:3.8
MAINTAINER clwhitney@lbl.gov

RUN mkdir -p /opt/weewx

RUN addgroup -S -g 642 weewx && adduser -G weewx -u 642 -h /opt/weewx -S -g "Weather Station,,,"-D weewx && chmod 755 /opt/weewx

ADD requirements.txt /opt/weewx
ADD run_weewx.sh /opt/weewx
ADD build.sh /

RUN ./build.sh

VOLUME /glusterfs/ec0

WORKDIR /glusterfs/ec0/weewx
ENV PYTHONPATH /glusterfs/ec0/weewx

ENTRYPOINT ["/bin/sh"]
