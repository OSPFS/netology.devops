### Домашняя работа к занятию "3.9. Элементы безопасности информационных систем"

ДЗ выполнил по пунктам, всё получилось. 
```
root@vagrant:/usr/local/share/ca-certificates# curl -v https://netology.example.com
*   Trying 127.0.0.1:443...
* TCP_NODELAY set
* Connected to netology.example.com (127.0.0.1) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: CN=netology.example.com
*  start date: Sep 28 06:07:38 2020 GMT
*  expire date: Oct  8 06:08:07 2020 GMT
*  subjectAltName: host "netology.example.com" matched cert's "netology.example.com"
*  issuer: CN=example.com Intermediate Authority
*  SSL certificate verify ok.
> GET / HTTP/1.1
> Host: netology.example.com
> User-Agent: curl/7.68.0
> Accept: */*
>
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.18.0 (Ubuntu)
< Date: Mon, 28 Sep 2020 06:22:25 GMT
< Content-Type: text/html
< Content-Length: 612
< Last-Modified: Mon, 28 Sep 2020 06:08:54 GMT
< Connection: keep-alive
< ETag: "5f717df6-264"
< Accept-Ranges: bytes
<
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
* Connection #0 to host netology.example.com left intact
root@vagrant:/usr/local/share/ca-certificates#
```