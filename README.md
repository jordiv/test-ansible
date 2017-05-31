How it works
=========

Creates and deploys simple nginx reverse proxy configurations from supplied variables, optionally making use of the load balancing features as well.

At the time, this role does not expose all possible configurations of nginx's load balancing and proxying, but aims to use rational defaults with some configurability.

Requirements
------------

nginx with reverse proxy support installed on the server to be managed.

Role Variables
--------------

### Expected to Be Configured

* `nginx_reverse_proxy_proxies`:  list of reverse proxy configurations; each configuration needs the following variables
  * `nginx_reverse_proxy_backend_name:` string, name nginx config uses to refer to the backend
  * `nginx_reverse_proxy_domains`: list of public-facing domains to be proxied
  * `nginx_reverse_proxy_backends`: list of backend servers, including ports and [other valid parameters for `server` in the `upstream` context of an nginx config file](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#server)
  * `nginx_reverse_proxy_config_name`: name to use for the proxy file (do not include the '.conf' extension, role will add this)

### Proxy configuration options

Along with the variables that must be configured for each reverse proxy configuration, some configuration options are available on a per-proxy basis:

* `balancer_config`: specify a load balancing strategy other than the default round robin. Valid options include `least_conn` (for least connections) and `ip_hash` (for session persistence using IP hashing).

See the app2proxy definition in the example playbook below.

### Role Defaults

`nginx_reverse_proxy_config_directory:` location to store config files for nginx (default: `/etc/nginx/conf.d`)
`nginx_reverse_proxy_nginx_service`: name the nginx service runs under, for the handler restart if config files are changed (default: `nginx`)

