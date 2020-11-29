#### Домашняя работа к занятию "6.5 Elasticsearch"

* Задача 1

Текст Dockerfile манифеста:
```
FROM centos:7

COPY ./elasticsearch-7.10.0 /srv/elasticsearch
RUN adduser elastic
RUN chown -R elastic: /srv/elasticsearch
RUN mkdir /var/lib/elk; chown -R elastic: /var/lib/elk
CMD ["/srv/elasticsearch/bin/elasticsearch"]
```
образ в репозитории dockerhub https://hub.docker.com/repository/docker/kundulun/elk

docker-compose.yml для выполнения ДЗ:
```
version: '3.1'

services:

  elk:
    image: kundulun/elk
    user: elastic
    restart: unless-stopped
    ports:
      - 9200:9200
    volumes:
      - ./elasticsearch.yml:/srv/elasticsearch/config/elasticsearch.yml
      - ./snapshots/:/srv/elasticsearch/snapshots/
volumes:
  elk_vol:
```
ответ elasticsearch на запрос пути / в json виде:
```
curl -X GET "127.0.0.1:9200/"

{
  "name" : "netology_test",
  "cluster_name" : "CL-1",
  "cluster_uuid" : "-83l0SasROKnJCGtE20KwA",
  "version" : {
    "number" : "7.10.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "51e9d6f22758d0374a0f3f5c6e8f3a7997850f96",
    "build_date" : "2020-11-09T21:30:33.964949Z",
    "build_snapshot" : false,
    "lucene_version" : "8.7.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

* Задача 2

Получите список индексов и их статусов, используя API 
```
curl -X GET "localhost:9200/_aliases?pretty"
{
  "ind-3" : {
    "aliases" : { }
  },
  "ind-1" : {
    "aliases" : { }
  },
  "ind-2" : {
    "aliases" : { }
  }
}

статус приведен в конце файла, а желтый тк нет реплик
```
* Задача 3

запрос API и результат вызова API для создания репозитория:
```
curl -X PUT "localhost:9200/_snapshot/netology_backup" -H 'Content-Type: application/json' -d'{
  "type": "fs",
  "settings": {
    "location": "/srv/elasticsearch/snapshots"
  }
}'

{"acknowledged":true}%
```
список файлов в директории со snapshotами:
```
.
├── index-0
├── index.latest
├── indices
│   └── cXIYF7_UTfC4lPfyEK6UMA
│       ├── 0
│       │   ├── index-FZ1KxLbDQ3aCbdpE3KRCqA
│       │   └── snap-gYPlY2oTTc2bR6h6qPAVtw.dat
│       └── meta-VkeaFHYB11tnRyieZ3Ee.dat
├── meta-gYPlY2oTTc2bR6h6qPAVtw.dat
└── snap-gYPlY2oTTc2bR6h6qPAVtw.dat

3 directories, 7 files
```
запрос к API восстановления:
```
curl -X POST "localhost:9200/_snapshot/netology_backup/snapshot_1/_restore?pretty"
{
  "accepted" : true
}
```
и итоговый список индексов:
```
curl -X GET "localhost:9200/_aliases?pretty"
{
  "test-2" : {
    "aliases" : { }
  },
  "test" : {
    "aliases" : { }
  }
}
```
* Статус индекса 1
```
curl -X GET "localhost:9200/ind-1/_stats?pretty"

{
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "_all" : {
    "primaries" : {
      "docs" : {
        "count" : 0,
        "deleted" : 0
      },
      "store" : {
        "size_in_bytes" : 416,
        "reserved_in_bytes" : 0
      },
      "indexing" : {
        "index_total" : 0,
        "index_time_in_millis" : 0,
        "index_current" : 0,
        "index_failed" : 0,
        "delete_total" : 0,
        "delete_time_in_millis" : 0,
        "delete_current" : 0,
        "noop_update_total" : 0,
        "is_throttled" : false,
        "throttle_time_in_millis" : 0
      },
      "get" : {
        "total" : 0,
        "time_in_millis" : 0,
        "exists_total" : 0,
        "exists_time_in_millis" : 0,
        "missing_total" : 0,
        "missing_time_in_millis" : 0,
        "current" : 0
      },
      "search" : {
        "open_contexts" : 0,
        "query_total" : 0,
        "query_time_in_millis" : 0,
        "query_current" : 0,
        "fetch_total" : 0,
        "fetch_time_in_millis" : 0,
        "fetch_current" : 0,
        "scroll_total" : 0,
        "scroll_time_in_millis" : 0,
        "scroll_current" : 0,
        "suggest_total" : 0,
        "suggest_time_in_millis" : 0,
        "suggest_current" : 0
      },
      "merges" : {
        "current" : 0,
        "current_docs" : 0,
        "current_size_in_bytes" : 0,
        "total" : 0,
        "total_time_in_millis" : 0,
        "total_docs" : 0,
        "total_size_in_bytes" : 0,
        "total_stopped_time_in_millis" : 0,
        "total_throttled_time_in_millis" : 0,
        "total_auto_throttle_in_bytes" : 41943040
      },
      "refresh" : {
        "total" : 4,
        "total_time_in_millis" : 0,
        "external_total" : 4,
        "external_total_time_in_millis" : 1,
        "listeners" : 0
      },
      "flush" : {
        "total" : 2,
        "periodic" : 0,
        "total_time_in_millis" : 0
      },
      "warmer" : {
        "current" : 0,
        "total" : 2,
        "total_time_in_millis" : 0
      },
      "query_cache" : {
        "memory_size_in_bytes" : 0,
        "total_count" : 0,
        "hit_count" : 0,
        "miss_count" : 0,
        "cache_size" : 0,
        "cache_count" : 0,
        "evictions" : 0
      },
      "fielddata" : {
        "memory_size_in_bytes" : 0,
        "evictions" : 0
      },
      "completion" : {
        "size_in_bytes" : 0
      },
      "segments" : {
        "count" : 0,
        "memory_in_bytes" : 0,
        "terms_memory_in_bytes" : 0,
        "stored_fields_memory_in_bytes" : 0,
        "term_vectors_memory_in_bytes" : 0,
        "norms_memory_in_bytes" : 0,
        "points_memory_in_bytes" : 0,
        "doc_values_memory_in_bytes" : 0,
        "index_writer_memory_in_bytes" : 0,
        "version_map_memory_in_bytes" : 0,
        "fixed_bit_set_memory_in_bytes" : 0,
        "max_unsafe_auto_id_timestamp" : -1,
        "file_sizes" : { }
      },
      "translog" : {
        "operations" : 0,
        "size_in_bytes" : 110,
        "uncommitted_operations" : 0,
        "uncommitted_size_in_bytes" : 110,
        "earliest_last_modified_age" : 0
      },
      "request_cache" : {
        "memory_size_in_bytes" : 0,
        "evictions" : 0,
        "hit_count" : 0,
        "miss_count" : 0
      },
      "recovery" : {
        "current_as_source" : 0,
        "current_as_target" : 0,
        "throttle_time_in_millis" : 0
      }
    },
    "total" : {
      "docs" : {
        "count" : 0,
        "deleted" : 0
      },
      "store" : {
        "size_in_bytes" : 416,
        "reserved_in_bytes" : 0
      },
      "indexing" : {
        "index_total" : 0,
        "index_time_in_millis" : 0,
        "index_current" : 0,
        "index_failed" : 0,
        "delete_total" : 0,
        "delete_time_in_millis" : 0,
        "delete_current" : 0,
        "noop_update_total" : 0,
        "is_throttled" : false,
        "throttle_time_in_millis" : 0
      },
      "get" : {
        "total" : 0,
        "time_in_millis" : 0,
        "exists_total" : 0,
        "exists_time_in_millis" : 0,
        "missing_total" : 0,
        "missing_time_in_millis" : 0,
        "current" : 0
      },
      "search" : {
        "open_contexts" : 0,
        "query_total" : 0,
        "query_time_in_millis" : 0,
        "query_current" : 0,
        "fetch_total" : 0,
        "fetch_time_in_millis" : 0,
        "fetch_current" : 0,
        "scroll_total" : 0,
        "scroll_time_in_millis" : 0,
        "scroll_current" : 0,
        "suggest_total" : 0,
        "suggest_time_in_millis" : 0,
        "suggest_current" : 0
      },
      "merges" : {
        "current" : 0,
        "current_docs" : 0,
        "current_size_in_bytes" : 0,
        "total" : 0,
        "total_time_in_millis" : 0,
        "total_docs" : 0,
        "total_size_in_bytes" : 0,
        "total_stopped_time_in_millis" : 0,
        "total_throttled_time_in_millis" : 0,
        "total_auto_throttle_in_bytes" : 41943040
      },
      "refresh" : {
        "total" : 4,
        "total_time_in_millis" : 0,
        "external_total" : 4,
        "external_total_time_in_millis" : 1,
        "listeners" : 0
      },
      "flush" : {
        "total" : 2,
        "periodic" : 0,
        "total_time_in_millis" : 0
      },
      "warmer" : {
        "current" : 0,
        "total" : 2,
        "total_time_in_millis" : 0
      },
      "query_cache" : {
        "memory_size_in_bytes" : 0,
        "total_count" : 0,
        "hit_count" : 0,
        "miss_count" : 0,
        "cache_size" : 0,
        "cache_count" : 0,
        "evictions" : 0
      },
      "fielddata" : {
        "memory_size_in_bytes" : 0,
        "evictions" : 0
      },
      "completion" : {
        "size_in_bytes" : 0
      },
      "segments" : {
        "count" : 0,
        "memory_in_bytes" : 0,
        "terms_memory_in_bytes" : 0,
        "stored_fields_memory_in_bytes" : 0,
        "term_vectors_memory_in_bytes" : 0,
        "norms_memory_in_bytes" : 0,
        "points_memory_in_bytes" : 0,
        "doc_values_memory_in_bytes" : 0,
        "index_writer_memory_in_bytes" : 0,
        "version_map_memory_in_bytes" : 0,
        "fixed_bit_set_memory_in_bytes" : 0,
        "max_unsafe_auto_id_timestamp" : -1,
        "file_sizes" : { }
      },
      "translog" : {
        "operations" : 0,
        "size_in_bytes" : 110,
        "uncommitted_operations" : 0,
        "uncommitted_size_in_bytes" : 110,
        "earliest_last_modified_age" : 0
      },
      "request_cache" : {
        "memory_size_in_bytes" : 0,
        "evictions" : 0,
        "hit_count" : 0,
        "miss_count" : 0
      },
      "recovery" : {
        "current_as_source" : 0,
        "current_as_target" : 0,
        "throttle_time_in_millis" : 0
      }
    }
  },
  "indices" : {
    "ind-1" : {
      "uuid" : "h7hJH5zvSeCR1jkXYelLrg",
      "primaries" : {
        "docs" : {
          "count" : 0,
          "deleted" : 0
        },
        "store" : {
          "size_in_bytes" : 416,
          "reserved_in_bytes" : 0
        },
        "indexing" : {
          "index_total" : 0,
          "index_time_in_millis" : 0,
          "index_current" : 0,
          "index_failed" : 0,
          "delete_total" : 0,
          "delete_time_in_millis" : 0,
          "delete_current" : 0,
          "noop_update_total" : 0,
          "is_throttled" : false,
          "throttle_time_in_millis" : 0
        },
        "get" : {
          "total" : 0,
          "time_in_millis" : 0,
          "exists_total" : 0,
          "exists_time_in_millis" : 0,
          "missing_total" : 0,
          "missing_time_in_millis" : 0,
          "current" : 0
        },
        "search" : {
          "open_contexts" : 0,
          "query_total" : 0,
          "query_time_in_millis" : 0,
          "query_current" : 0,
          "fetch_total" : 0,
          "fetch_time_in_millis" : 0,
          "fetch_current" : 0,
          "scroll_total" : 0,
          "scroll_time_in_millis" : 0,
          "scroll_current" : 0,
          "suggest_total" : 0,
          "suggest_time_in_millis" : 0,
          "suggest_current" : 0
        },
        "merges" : {
          "current" : 0,
          "current_docs" : 0,
          "current_size_in_bytes" : 0,
          "total" : 0,
          "total_time_in_millis" : 0,
          "total_docs" : 0,
          "total_size_in_bytes" : 0,
          "total_stopped_time_in_millis" : 0,
          "total_throttled_time_in_millis" : 0,
          "total_auto_throttle_in_bytes" : 41943040
        },
        "refresh" : {
          "total" : 4,
          "total_time_in_millis" : 0,
          "external_total" : 4,
          "external_total_time_in_millis" : 1,
          "listeners" : 0
        },
        "flush" : {
          "total" : 2,
          "periodic" : 0,
          "total_time_in_millis" : 0
        },
        "warmer" : {
          "current" : 0,
          "total" : 2,
          "total_time_in_millis" : 0
        },
        "query_cache" : {
          "memory_size_in_bytes" : 0,
          "total_count" : 0,
          "hit_count" : 0,
          "miss_count" : 0,
          "cache_size" : 0,
          "cache_count" : 0,
          "evictions" : 0
        },
        "fielddata" : {
          "memory_size_in_bytes" : 0,
          "evictions" : 0
        },
        "completion" : {
          "size_in_bytes" : 0
        },
        "segments" : {
          "count" : 0,
          "memory_in_bytes" : 0,
          "terms_memory_in_bytes" : 0,
          "stored_fields_memory_in_bytes" : 0,
          "term_vectors_memory_in_bytes" : 0,
          "norms_memory_in_bytes" : 0,
          "points_memory_in_bytes" : 0,
          "doc_values_memory_in_bytes" : 0,
          "index_writer_memory_in_bytes" : 0,
          "version_map_memory_in_bytes" : 0,
          "fixed_bit_set_memory_in_bytes" : 0,
          "max_unsafe_auto_id_timestamp" : -1,
          "file_sizes" : { }
        },
        "translog" : {
          "operations" : 0,
          "size_in_bytes" : 110,
          "uncommitted_operations" : 0,
          "uncommitted_size_in_bytes" : 110,
          "earliest_last_modified_age" : 0
        },
        "request_cache" : {
          "memory_size_in_bytes" : 0,
          "evictions" : 0,
          "hit_count" : 0,
          "miss_count" : 0
        },
        "recovery" : {
          "current_as_source" : 0,
          "current_as_target" : 0,
          "throttle_time_in_millis" : 0
        }
      },
      "total" : {
        "docs" : {
          "count" : 0,
          "deleted" : 0
        },
        "store" : {
          "size_in_bytes" : 416,
          "reserved_in_bytes" : 0
        },
        "indexing" : {
          "index_total" : 0,
          "index_time_in_millis" : 0,
          "index_current" : 0,
          "index_failed" : 0,
          "delete_total" : 0,
          "delete_time_in_millis" : 0,
          "delete_current" : 0,
          "noop_update_total" : 0,
          "is_throttled" : false,
          "throttle_time_in_millis" : 0
        },
        "get" : {
          "total" : 0,
          "time_in_millis" : 0,
          "exists_total" : 0,
          "exists_time_in_millis" : 0,
          "missing_total" : 0,
          "missing_time_in_millis" : 0,
          "current" : 0
        },
        "search" : {
          "open_contexts" : 0,
          "query_total" : 0,
          "query_time_in_millis" : 0,
          "query_current" : 0,
          "fetch_total" : 0,
          "fetch_time_in_millis" : 0,
          "fetch_current" : 0,
          "scroll_total" : 0,
          "scroll_time_in_millis" : 0,
          "scroll_current" : 0,
          "suggest_total" : 0,
          "suggest_time_in_millis" : 0,
          "suggest_current" : 0
        },
        "merges" : {
          "current" : 0,
          "current_docs" : 0,
          "current_size_in_bytes" : 0,
          "total" : 0,
          "total_time_in_millis" : 0,
          "total_docs" : 0,
          "total_size_in_bytes" : 0,
          "total_stopped_time_in_millis" : 0,
          "total_throttled_time_in_millis" : 0,
          "total_auto_throttle_in_bytes" : 41943040
        },
        "refresh" : {
          "total" : 4,
          "total_time_in_millis" : 0,
          "external_total" : 4,
          "external_total_time_in_millis" : 1,
          "listeners" : 0
        },
        "flush" : {
          "total" : 2,
          "periodic" : 0,
          "total_time_in_millis" : 0
        },
        "warmer" : {
          "current" : 0,
          "total" : 2,
          "total_time_in_millis" : 0
        },
        "query_cache" : {
          "memory_size_in_bytes" : 0,
          "total_count" : 0,
          "hit_count" : 0,
          "miss_count" : 0,
          "cache_size" : 0,
          "cache_count" : 0,
          "evictions" : 0
        },
        "fielddata" : {
          "memory_size_in_bytes" : 0,
          "evictions" : 0
        },
        "completion" : {
          "size_in_bytes" : 0
        },
        "segments" : {
          "count" : 0,
          "memory_in_bytes" : 0,
          "terms_memory_in_bytes" : 0,
          "stored_fields_memory_in_bytes" : 0,
          "term_vectors_memory_in_bytes" : 0,
          "norms_memory_in_bytes" : 0,
          "points_memory_in_bytes" : 0,
          "doc_values_memory_in_bytes" : 0,
          "index_writer_memory_in_bytes" : 0,
          "version_map_memory_in_bytes" : 0,
          "fixed_bit_set_memory_in_bytes" : 0,
          "max_unsafe_auto_id_timestamp" : -1,
          "file_sizes" : { }
        },
        "translog" : {
          "operations" : 0,
          "size_in_bytes" : 110,
          "uncommitted_operations" : 0,
          "uncommitted_size_in_bytes" : 110,
          "earliest_last_modified_age" : 0
        },
        "request_cache" : {
          "memory_size_in_bytes" : 0,
          "evictions" : 0,
          "hit_count" : 0,
          "miss_count" : 0
        },
        "recovery" : {
          "current_as_source" : 0,
          "current_as_target" : 0,
          "throttle_time_in_millis" : 0
        }
      }
    }
  }
}
```
