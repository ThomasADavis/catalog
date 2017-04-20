FROM gliderlabs/alpine:3.4
MAINTAINER Thomas Davis tadavis@lbl.gov

RUN mkdir -p /opt/snmp

RUN addgroup -S -g 604 snmp && adduser -G snmp -u 600 -h /opt/snmp -S -g "SNIMPY System,,,"-D snmp && \
    chmod 755 /opt/snmp

ADD build.sh /

RUN mkdir -p /application/
ADD pulsar /application/pulsar
# ADD pulsar-docker/downloads /application/downloads
# ADD requirements.txt /application/config

RUN ./build.sh

WORKDIR /opt/snmp
VOLUME /external

# ENVIRONMENT
ENV PYTHONPATH "/opt/snmp/"

# Set the default command to execute
#ENTRYPOINT ["./pulsar/scripts/pulsar_worker.py"]
ENTRYPOINT [ "/bin/sh" ]
#CMD ["--help"]
