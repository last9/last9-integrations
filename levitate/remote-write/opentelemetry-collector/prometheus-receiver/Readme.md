## Introduction

This directory contains an example of prometheus receiver setup with opentelemetry collector which sends
data to [Levitate](https://last9.io/products/levitate)

Please go through the tutorial [here]() for a walk-through of the setup and the information flow.

### Running

Make sure that you have docker running and then perform:

```sh
docker-compose up -d
```

After that the Golang application will start on port 9000 and Open Telemetry application wil start on port `4317`.
Send few HTTP requests on `http://localhost:9000/hello`. It will emit metrics which will be relayed to Levitate
via Open Telemetry coolector.
