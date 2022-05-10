# Duplicate Requests

A PoC to demo request duplication to multiple upstreams with Nginx.

Using (Nginx's mirror module)[http://nginx.org/en/docs/http/ngx_http_mirror_module.html], we can send an incoming request (including body) to a secondary upstream. Responses from the secondary upstream are ignored.

# Diagram

```sh
                                      ┌──────────────┐
                            ┌────────▶│  Upstream 1  │
                            │         └──────────────┘
┌──────────┐        ┌───────────────┐         │
│   HTTP   ├───────▶│     Nginx     │         │
│  Client  │◀───────┤ Reverse Proxy │◀────────┘
└──────────┘        └───────────────┘
                            │         ┌──────────────┐
                            └────────▶│  Upstream 2  │
                                      └──────────────┘
```

# Usage

1. Start the server

`docker-compose up -d`

2. Start log monitoring

`docker-compose logs -f`

3. Issue requests

In a separate terminal window, run

```sh
➜  ~ curl -H "content-type: application/json" -X POST -d '{"name": "foo"}' http://localhost/greet
{"greeting":"Hello foo!","host":"2e26ebf00f37"}%
```

The logs should indicate request being processed by both backends.

```sh
duplicate-requests-app1-1   | INFO:     172.20.0.2:42386 - "POST /greet HTTP/1.0" 200 OK
duplicate-requests-app1-1   | INFO:     Received payload for host '2e26ebf00f37': {'name': 'foo'}
duplicate-requests-app2-1   | INFO:     Received payload for host 'f620b8b3f6ea': {'name': 'foo'}
duplicate-requests-app2-1   | INFO:     172.20.0.2:41580 - "POST /greet HTTP/1.0" 200 OK
duplicate-requests-nginx-1  | 172.20.0.1 - - [10/May/2022:04:08:44 +0000] "POST /greet HTTP/1.1" 200 47 "-" "curl/7.79.1" "-"
```

4. Teardown

`docker-compose down`
