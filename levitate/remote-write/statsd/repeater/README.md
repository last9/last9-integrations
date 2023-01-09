This folder contains demo code for statsd to Levitate remote write integration
using stasd_exporter repeater method.

Read more about the flow [here](https://docs.last9.io/docs/levitate-integrations-statsd#repeater-method)

### Steps

1. Update the following variables in [docker-compose.yaml](./docker-compose.yaml) or update export them as environment variables
   - $LEVITATE_REMOTE_WRITE_URL
   - $LEVITATE_REMOTE_WRITE_USERNAME
   - $LEVITATE_REMOTE_WRITE_PASSWORD
2. Run `docker-compose up --build --force-recreate --remove-orphans`

### Validate

1. Run a test app that sends metrics to statsd.
   ```
   pip install -r requirements.txt
   python ./test/statsd-test.py
   ```
2. After 5 minutes, query for a sample metric `performance_request_successful_count_value`.
