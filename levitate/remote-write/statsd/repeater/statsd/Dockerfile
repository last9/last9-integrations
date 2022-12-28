FROM node:latest

RUN apt-get update && apt-get install -y --force-yes git
RUN git clone https://github.com/etsy/statsd.git
# Install generic-pool module as it is required by repeater backend
RUN cd /statsd && npm install generic-pool@2.2.0

ADD config.js /statsd/config.js

EXPOSE 8125/udp
EXPOSE 8126/udp
EXPOSE 8125/tcp
EXPOSE 8126/tcp

CMD /usr/local/bin/node /statsd/stats.js /statsd/config.js
