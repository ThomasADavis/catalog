FROM gliderlabs/alpine:3.4
MAINTAINER Thomas Davis tadavis@lbl.gov

RUN mkdir -p /opt/ionscraper

RUN addgroup -S -g 604 ionscraper && adduser -G ionscraper -u 604 -h /opt/ionscraper -S -g "ion HTTP scraper,,,"-D ionscraper && \
    chmod 755 /opt/ionscraper

ADD build.sh /
ADD pulsar /opt/ionscraper/pulsar
ADD requirements.txt /opt/ionscraper

RUN ./build.sh

WORKDIR /opt/ionscraper
VOLUME /external

# ENVIRONMENT
ENV PYTHONPATH "/opt/ionscraper/"

# Set the default command to execute
#ENTRYPOINT ["./pulsar/scripts/pulsar_worker.py"]
ENTRYPOINT [ "/bin/sh" ]
#CMD ["--help"]
