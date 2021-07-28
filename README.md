
- Metrics URL
http://localhost:80/metrics

- Sample Response
```sh
# HELP sample_external_url_up Given URL is up or not
# TYPE sample_external_url_up gauge
sample_external_url_up{url="https://httpstat.us/503"} 0.0
sample_external_url_up{url="https://httpstat.us/200"} 1.0
sample_external_url_up{url="https://google.com"} 1.0
# HELP sample_external_url_response_ms Response Time in milliseconds
# TYPE sample_external_url_response_ms gauge
sample_external_url_response_ms{url="https://httpstat.us/503"} 0.000204703
sample_external_url_response_ms{url="https://httpstat.us/200"} 0.00020199600000000002
sample_external_url_response_ms{url="https://google.com"} 0.000102991
```

- Config File - List of URLS to check
```sh
cat urls.config 
https://httpstat.us/503
https://httpstat.us/200
https://google.com
```
