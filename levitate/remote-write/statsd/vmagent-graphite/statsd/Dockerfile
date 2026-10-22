# Pinned to the first Node 24 LTS that blocks the compromised eMudhra intermediates (nodejs/node#66871).
FROM node:24.22.1-bookworm@sha256:5630d96570d4ca4a8523fda3d169d0114554d0f48293e1ae3db6be7c79b42a17

RUN apt-get update && apt-get install -y --force-yes git
RUN git clone https://github.com/etsy/statsd.git
RUN cd /statsd

ADD config.js /statsd/config.js

EXPOSE 8125/udp
EXPOSE 8126/udp
EXPOSE 8125/tcp
EXPOSE 8126/tcp

CMD /usr/local/bin/node /statsd/stats.js /statsd/config.js
