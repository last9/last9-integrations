(function() {
  return {
    port: 8125,
    debug: true,
    backends: ["./backends/console", "./backends/graphite"],
    graphiteHost: "vmagent_levitate",
    graphitePort: 2003,
    server: "./servers/udp",
    includeStatsdMetrics: false,
    includeInfluxdbMetrics: false,
    keyNameSanitize: false
  };
})();
