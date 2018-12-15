FROM alpine:3.8
MAINTAINER Cary Whitney clwhitney@lbl.gov

RUN mkdir -p /opt/pue

RUN addgroup -S -g 646 pue && adduser -G pue -u 646 -h /opt/pue -S -g "PUE Calculation,,,"-D pue && \
    chmod 755 /opt/pue

ADD requirements.txt /opt/pue
ADD pue_last.py /opt/pue
ADD run.sh /opt/pue
ADD build.sh /

RUN ./build.sh

WORKDIR /opt/pue

# ENVIRONMENT
ENV PYTHONPATH "/opt/pue/"

# Set the default command to execute
ENTRYPOINT [ "/bin/sh" ]
#CMD ["--help"]
