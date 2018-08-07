FROM gliderlabs/alpine:3.4
MAINTAINER Thomas Davis tadavis@lbl.gov

RUN mkdir -p /opt/onewire

RUN addgroup -S -g 600 onewire && adduser -G onewire -u 600 -h /opt/onewire -S -g "Onewire System,,,"-D onewire && \
    chmod 755 /opt/onewire

ADD build.sh /

RUN mkdir -p /opt/python-consul
ADD python-consul /opt/python-consul

RUN mkdir -p /application/config
ADD pulsar /application/pulsar
ADD pulsar-docker/downloads /application/downloads
ADD requirements.txt /application/config

RUN ./build.sh

WORKDIR /opt/onewire
VOLUME /external

# ENVIRONMENT
ENV PYTHONPATH "/opt/onewire/"

# Set the default command to execute
#ENTRYPOINT ["./pulsar/scripts/pulsar_worker.py"]
ENTRYPOINT [ "/bin/sh" ]
#CMD ["--help"]
