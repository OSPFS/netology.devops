FROM centos:7

COPY ./elasticsearch-7.10.0 /srv/elasticsearch
RUN adduser elastic
RUN chown -R elastic: /srv/elasticsearch
RUN mkdir /var/lib/elk; chown -R elastic: /var/lib/elk
CMD ["/srv/elasticsearch/bin/elasticsearch"]
