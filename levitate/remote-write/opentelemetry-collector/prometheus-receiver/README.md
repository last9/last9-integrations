## Introduction

This directory contains an example of a Prometheus receiver setup with OpenTelemetry collector which sends
data to [Last9](https://last9.io/metrics/)

Follow through the tutorial [here](https://docs.last9.io/docs/integration-opentelemetry) for a walk-through of the setup and the information flow, side by side.

### Running

Replace the following variables in `otel-collector-config.yaml` with the actual values from your Last9 cluster.

```sh
$last9_username -> Cluster ID
$last9_password -> Write Token
$last9_write_endpoint -> Last9 Remote Write endpoint
```

Make sure that you have docker running and then perform:

```sh
docker-compose up -d
```

After that, the Golang application will start on port 9000, and the Open Telemetry collector will start on port `4317`.
Send a few HTTP requests on `http://localhost:9000/hello`.
It will emit metrics relayed to Last9 via Open Telemetry collector.


### Verification

Create a Read token for Last9 cluster and connect to [Grafana](https://last9.io/docs/grafana-config/) for verification.

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
          "__name__": "last9_request_counts_total",
          "__l9cluster__": "ebce9978-80f0-4976-9103-d435a7a4adf6",
          "__l9lake__": "prometheus",
          "__tenant__": "omecs",
          "env": "production",
          "instance": "app:8000",
          "job": "otel-collector-01",
          "otel_scope_name": "last9-otel-demo",
          "program": "last9",
          "via_cluster": "cs-test-last9-01"
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
