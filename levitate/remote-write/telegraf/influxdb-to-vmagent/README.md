### Overview

This directory contains demo code for Telegraf to Levitate remote write integration
using InfluxDB output plugin pointing to vmagent.

Read more about the flow [here](https://docs.last9.io/docs/levitate-integrations-telegraf).


### Steps

1. Update the following variables in [docker-compose.yaml](./docker-compose.yaml) or update export them as environment variables
   - $LEVITATE_REMOTE_WRITE_URL
   - $LEVITATE_REMOTE_WRITE_USERNAME
   - $LEVITATE_REMOTE_WRITE_PASSWORD
2. Run `docker-compose up --build --force-recreate --remove-orphans`

### Validate

1. Run a test app that sends metrics to Telegraf.
   ```
   pip install -r requirements.txt
   python ./test/statsd-test.py
   ```
2. After few minutes, query for a sample metric `performance_request_successful_count_value` using Levitate read endpoint.
