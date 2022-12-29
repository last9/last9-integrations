package main

import (
	"log"
	"net/http"

	"github.com/prometheus/client_golang/prometheus/promhttp"
	"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/exporters/prometheus"
	"go.opentelemetry.io/otel/metric/instrument"
	"go.opentelemetry.io/otel/sdk/metric"
)

func main() {
	exporter, err := prometheus.New()
	if err != nil {
		log.Fatal(err)
	}
	provider := metric.NewMeterProvider(metric.WithReader(exporter))
	meter := provider.Meter("levitate-otel-demo")
	requestCount, _ := meter.SyncInt64().Counter(
		"levitate/request_counts",
		instrument.WithDescription("The number of requests received"),
	)

	programLabel := attribute.String("program", "levitate")
	envLabel := attribute.String("env", "production")
	labels := []attribute.KeyValue{programLabel, envLabel}

	// Start the prometheus HTTP server and pass the exporter Collector to it
	go serveMetrics()

	handler := http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
		ctx := req.Context()
		requestCount.Add(ctx, 1, labels...)

		if _, err := w.Write([]byte("Hello World")); err != nil {
			http.Error(w, "write operation failed.", http.StatusInternalServerError)
			return
		}

	})

	mux := http.NewServeMux()
	mux.Handle("/hello", otelhttp.NewHandler(handler, "/hello"))
	server := &http.Server{
		Addr:    ":9000",
		Handler: mux,
	}
	if err := server.ListenAndServe(); err != http.ErrServerClosed {
		log.Fatalf("%v", err)
	}
}

func serveMetrics() {
	log.Printf("serving metrics")
	mux := http.NewServeMux()
	mux.Handle("/metrics", promhttp.Handler())
	server := &http.Server{
		Addr:    ":8000",
		Handler: mux,
	}
	if err := server.ListenAndServe(); err != http.ErrServerClosed {
		log.Fatalf("%v", err)
	}
}
