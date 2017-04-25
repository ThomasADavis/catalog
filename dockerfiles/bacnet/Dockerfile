FROM gliderlabs/alpine:3.4
MAINTAINER Thomas Davis tadavis@lbl.gov

RUN mkdir -p /opt/bacnet

RUN addgroup -S -g 603 bacnet && adduser -G bacnet -u 603 -h /opt/bacnet -S -g "Bacnet System,,,"-D bacnet && \
    chmod 755 /opt/bacnet

ADD requirements.txt /opt/bacnet
ADD build.sh /

RUN mkdir -p /application
ADD pulsar /application/pulsar

RUN ./build.sh

WORKDIR /opt/bacnet
VOLUME /external

# ENVIRONMENT
ENV PYTHONPATH "/opt/bacnet/"

# Set the default command to execute
#ENTRYPOINT ["./pulsar/scripts/pulsar_worker.py"]
ENTRYPOINT [ "/bin/sh" ]
#CMD ["--help"]
