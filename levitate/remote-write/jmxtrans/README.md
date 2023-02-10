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

1. The above run should publish the [sample app](./jvmapp/SampleApp.java) metrics to Levitate.
2. By default, graphite metrics are dumped in `a.b.c.d` format. This can lead to increase in metric names and remove the flexibility of labels i.e. instead of having `requests{host='a'}`, without any
   transformation, the metric would show up as `requests.host.a`
3. To address this, we leverage vmagent [graphite relabeling](https://docs.victoriametrics.com/vmagent.html#graphite-relabeling). A sample setup is added in [vmagent.yaml](vmagent.yaml), which converts a flattened metric like

    ```
    "metric": {
      "__name__": "sample.service.jvmapp_4000.sun_management_MemoryImpl.HeapMemoryUsage_committed",
    },
    ```

    to

    ```
    "metric": {
      "__name__": "HeapMemoryUsage_committed",
      "service": "sample_service",
      "instance": "jvmapp_4000",
    }
    ```
4. This sample [vmagent.yaml](vmagent.yaml) can be modified for any other relabeling as required.
