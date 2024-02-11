## Introduction

This directory contains an example of a Prometheus receiver setup with OpenTelemetry collector which sends
data to [Levitate](https://last9.io/products/levitate)

Follow through the tutorial [here](https://docs.last9.io/docs/integration-opentelemetry) for a walk-through of the setup and the information flow, side by side.

### Running

Replace the following variables in `otel-collector-config.yaml` with the actual values from your Levitate cluster.

```sh
$levitate_username -> Cluster ID
$levitate_password -> Write Token
$levitate_write_endpoint -> Levitate Remote Write endpoint
```

Make sure that you have docker running and then perform:

```sh
docker-compose up -d
```

After that, the Golang application will start on port 9000, and the Open Telemetry collector will start on port `4317`.
Send a few HTTP requests on `http://localhost:9000/hello`.
It will emit metrics relayed to Levitate via Open Telemetry collector.


### Verification

Create a Read token for Levitate cluster and connect to [Grafana](https://docs.last9.io/docs/levitate-grafana-config) for verification.

If all goes well, you should see the metrics as follows:

```json
{
  "status": "success",
  "isPartial": false,
  "data": {
    "resultType": "matrix",
    "result": [
      {
        "metric": {
          "__name__": "levitate_request_counts_total",
          "__l9cluster__": "ebce9978-80f0-4976-9103-d435a7a4adf6",
          "__l9lake__": "prometheus",
          "__tenant__": "omecs",
          "env": "production",
          "instance": "app:8000",
          "job": "otel-collector-01",
          "otel_scope_name": "levitate-otel-demo",
          "program": "levitate",
          "via_cluster": "cs-test-levitate-01"
        },
        "values": [
          [
            1672307336,
            "3"
          ],
          [
            1672307396,
            "5"
          ]
        ]
      }
    ]
  }
}
```

## Related Articles

[What is OpenTelemetry](https://last9.io/blog/what-is-opentelemetry/)

[What is OpenTelemetry Collector](https://last9.io/blog/what-is-opentelemetry-collector/)

[Instrumenting Java applications using OpenTelemetry](https://last9.io/blog/how-to-instrument-java-applications-using-opentelemetry-tutorial-best-practices/)

Read more about the difference between [Prometheus vs. Otel](https://last9.io/blog/opentelemetry-vs-prometheus/#metrics-in-opentelemetry-vs-prometheus).

Here is a post on [How to filter metrics by labels using OpenTelemetry Collector](https://last9.io/blog/filtering-metrics-by-labels-in-opentelemetry-collector/).
