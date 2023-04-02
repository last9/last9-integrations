#!/usr/bin/env python

import logging
import random
import sys
import time
import json
from logging import INFO

from opentelemetry import metrics
from opentelemetry.exporter.prometheus_remote_write import (
    PrometheusRemoteWriteMetricsExporter,
)
from opentelemetry.metrics import Observation
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


exporter = PrometheusRemoteWriteMetricsExporter(
    endpoint=sys.argv[1],
    basic_auth={
        "username": sys.argv[2],
        "password": sys.argv[3],
    },
    headers={},
)
reader = PeriodicExportingMetricReader(exporter, 1000)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)

requests_counter = meter.create_counter(
    name=sys.argv[4],
    description="number of requests",
)

testing_labels = json.loads(sys.argv[5])

num = random.randint(0, 1000)
requests_counter.add(num % 131 + 200, testing_labels)
logger.log(level=INFO, msg="completed metrics collection cycle")
