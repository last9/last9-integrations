(function() {
  return {
    port: 8125,
    debug: false,
    backends: ['./backends/console'],
    server: "./servers/udp",
    includeStatsdMetrics: false,
    includeInfluxdbMetrics: false,
    keyNameSanitize: false
  };

})();
