(function() {
  return {
    port: parseInt(process.env.STATSD_PORT) || 8125,
    debug: process.env.STATSD_DEBUG || false,
    backends: ['./backends/console', './backends/repeater'],
    repeater: [ { host: 'statsd_exporter', port: 9125 }],
    server: "./servers/udp",
    includeStatsdMetrics: false,
    includeInfluxdbMetrics: false,
    keyNameSanitize: false
  };

})();
