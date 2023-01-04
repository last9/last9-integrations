import statsd
from time import sleep
from random import randint, choice

c = statsd.StatsClient('localhost', 8125, prefix='performance2')

while True:
    incr = randint(1, 5)
    metric_type = choice(['A', 'B', 'C'])
    print(f"\radding metric: type: {metric_type}, incr: {incr}", end="")
    c.incr(f'request.successful.count,type={metric_type}', incr)
    sleep(1)
