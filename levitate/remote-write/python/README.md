## Getting started

Make sure that you have snappy installed as per instructions [here](https://github.com/andrix/python-snappy).

```sh
pip install python-snappy
pip install opentelemetry-exporter-prometheus-remote-write
```

This will install required dependencies. After that, pass the username and password of Prometheus backend. (It can be Levitate cluster).

```sh
python app.py LEVITATE_REMOTE_WRITE_URL LEVITATE_CLUSTER_USERNAME LEVITATE_CLUSTER_PASSWORD 'my_metric' '{"environment": "staging", "label": "9999"}'
```

After this you can explore the metric in Grafana to make sure it is accessible.

You can refer to complete tutorial [here](https://docs.last9.io/docs/using-open-telemetry-exporter-for-prometheus-remote-write).
