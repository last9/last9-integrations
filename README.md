# last9-integrations

Integrations and reference code used for Last9 products.

## Levitate Integrations

[Levitate](https://last9.io/products/levitate) is Last9’s managed Time Series database.

We built Levitate to give engineering teams a cost-effective tool to monitor large, complex systems. Now, engineering hours are not spent monitoring your monitor i.e. managing TSDB availability, scaling, replication, and multiple instances.

#### Solves High Cardinality

Levitate is built to handle the massive scales of data, and can handle queries at any cardinality. Above all, it gives you real-time insights into what metrics are unused.

#### Pay for what you use, reduce costs

Levitate reduces storage costs by up to 50% compared to similar TSDBs. This is over and above the engineering time and overheads spent maintaining internal infrastructure.
With Levitate's data retention policies & tiered storage, you pay for the metrics you use. Scale without having to tune the configuration, & having to run a whole setup for data scaling.

#### Increase engineering productivity

Levitate is fully managed. No need to worry about adding more machines, managing replication, or multiple Prometheus instances. Just change the remote-write endpoint of your one or many TSDBs. A simple UI manages it all.

With Levitate, you can resolve incidents faster with decreased querying times, and allow engineering to focus on building the product.

Levitate is easy to integrate with any source that can send metrics to Prometheus. 

----

Find sample applications of supported integrations and some useful exporter demo setups below.

### remote-write

Sample setups of common remote write integrations.

- [opentelemetry collector via prometheus receiver](./levitate/remote-write/opentelemetry-collector/prometheus-receiver)
- [statsd](./levitate/remote-write/statsd)
- [telegraf](./levitate/remote-write/telegraf)
- [vmagent](./levitate/remote-write/vmagent) - WIP 🏗️

### exporters

Sample setups of common Prometheus exporters.

- [kube-state-metrics](./levitate/exporter/kube-state-metrics) - Pending
- [statping](./levitate/exporter/statping) - WIP 🏗️
