FROM openjdk:8

COPY SampleApp.java /SampleApp.java
RUN javac SampleApp.java

CMD java \
  -Djava.rmi.server.hostname=jvmapp \
  -Dcom.sun.management.jmxremote \
  -Dcom.sun.management.jmxremote.port=4000 \
  -Dcom.sun.management.jmxremote.rmi.port=4000 \
  -Dcom.sun.management.jmxremote.local.only=false \
  -Dcom.sun.management.jmxremote.authenticate=false \
  -Dcom.sun.management.jmxremote.ssl=false \
  SampleApp
