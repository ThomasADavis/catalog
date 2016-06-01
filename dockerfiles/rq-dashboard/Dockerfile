FROM mini/base

MAINTAINER tadavis@lbl.gov

RUN apk update
RUN apk add py-pip && pip install rq-dashboard rq 
EXPOSE 9181
ENTRYPOINT [ "rq-dashboard", "--redis-url", "redis://redis/2" ]
