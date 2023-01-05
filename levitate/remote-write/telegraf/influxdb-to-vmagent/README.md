This folder contains demo code for Telegraf to Levitate remote write integration
using InfluxDB output plugin pointing to vmagent.


### Steps

1. Update the following variables in [docker-compose.yaml](./docker-compose.yaml) or update export them as environment variables
   - $LEVITATE_REMOTE_WRITE_URL
   - $LEVITATE_REMOTE_WRITE_USERNAME
   - $LEVITATE_REMOTE_WRITE_PASSWORD
2. Run `docker-compose up --build --force-recreate --remove-orphans`

### Validate

1. The above run should publish the [test app](./test/statsd-test.py) metrics to Levitate. Query for a sample metric `performance_request_successful_count_value` to validate.
