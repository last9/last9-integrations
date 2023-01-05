This directory contains demo code for jmxtrans to Levitate remote write integration
using jmxtrans Graphite output plugin pointing to vmagent.

[jmxtrans/jmxtrans](https://hub.docker.com/r/jmxtrans/jmxtrans) image does not work on MacOS M1 chipset. To test this docker-compose
setup, please use a Linux variant.

### Steps

1. Update the following variables in [docker-compose.yaml](./docker-compose.yaml) or update export them as environment variables
   - $LEVITATE_REMOTE_WRITE_URL
   - $LEVITATE_REMOTE_WRITE_USERNAME
   - $LEVITATE_REMOTE_WRITE_PASSWORD
2. Run `docker-compose up --build --force-recreate --remove-orphans`

### Validate

1. The above run should publish the [sample app](./jvmapp/SampleApp.java) metrics to Levitate. Query for a sample metric `sample.service.jvmapp_4000.sun_management_MemoryImpl.HeapMemoryUsage_committed` to validate.
