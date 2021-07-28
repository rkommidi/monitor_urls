#!/usr/bin/env python3

from prometheus_client import start_http_server, Gauge, REGISTRY
import time
import requests

def check_urls(t):
    config_file = "urls.config"
    output = ''
    with open(config_file,'r') as fh:
        for line in fh:
            url = line.strip()
            res = requests.get(url)
            if res.status_code == 200:
                is_up = 1
            else:
                is_up = 0

            response_ms = res.elapsed.total_seconds()/1000
            up.labels(url).set(is_up)
            rt.labels(url).set(response_ms)
#            print(url)
#            print(is_up)
#            print(response_ms)
            time.sleep(t)

if __name__ == '__main__':
    #unregister default metrics
    for col in list(REGISTRY._collector_to_names.keys()):
        REGISTRY.unregister(col)

    up = Gauge('sample_external_url_up', 'Given URL is up or not', ['url'])
    rt = Gauge('sample_external_url_response_ms', 'Response Time in milliseconds', ['url'])

    start_http_server(9100)
    while True:
        #collects every 5 secs
        check_urls(5) 
