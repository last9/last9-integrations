<a href="https://last9.io"><img src="https://last9.github.io/assets/last9-github-badge.svg" align="right" /></a>

# last9-integrations

Integrations and reference code used for Last9 products.

## Last9 Integrations

[Last9](https://last9.io/metrics/) is Last9’s managed time series data warehouse.

We built Last9 to give engineering teams a cost-effective tool to monitor large, complex systems. Now, engineering hours are not spent monitoring your monitor i.e. managing TSDB availability, scaling, replication, and multiple instances.

#### Solves High Cardinality

Last9 is built to handle the massive scales of data and can handle queries at any cardinality. Above all, it gives you real-time insights into what metrics are unused.

#### Pay for what you use, reduce costs

Last9 reduces storage costs by up to 50% compared to similar TSDBs. This is over and above the engineering time, and overheads spent maintaining internal infrastructure.
With Last9's data retention policies & tiered storage, you pay for the metrics you use. Scale without having to tune the configuration & having to run a whole setup for data scaling.

#### Increase engineering productivity

Last9 is fully managed. No need to worry about adding more machines, managing replication, or multiple Prometheus instances. Just change the remote-write endpoint of your one or many TSDBs. A simple UI manages it all.

With Last9, you can resolve incidents faster with decreased querying times, and allow engineering to focus on building the product.

Last9 is easy to integrate with any source that can send metrics to Prometheus. 

----

Find sample applications of supported integrations and some useful exporter demo setups below.

### remote-write

Sample setups of common remote write integrations.

- [opentelemetry collector via prometheus receiver](./levitate/remote-write/opentelemetry-collector/prometheus-receiver)
- [statsd](./levitate/remote-write/statsd)
- [telegraf](./levitate/remote-write/telegraf)
- [jmxtrans](./levitate/remote-write/jmxtrans)
- [vmagent](./levitate/remote-write/vmagent) - WIP 🏗️

### exporters

Sample setups of common Prometheus exporters.

- [kube-state-metrics](./levitate/exporter/kube-state-metrics) - WIP 🏗️
- [statping](./levitate/exporter/statping) - WIP 🏗️
