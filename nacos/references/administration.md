# Nacos - Administration

**Pages:** 1

---

## Nacos monitor guide

**URL:** https://nacos.io/en-us/docs/monitor-guide.html

**Contents:**
- Nacos monitor guide
- Deploy Nacos cluster to expose metrics data
- Deploy prometheus to collect Nacos metrics data
  - linux & mac
  - windows
- Deploy grafana to graphically display metrics data
  - mac
  - linux
  - windows
- configure grafana alert

Nacos 0.8.0 improves the monitoring system, supporting Nacos operation status monitoring through exposing metrics data access to third-party monitoring system. Currently, prometheus, elastic search and influxdb are supported. The docs introduce how prometheus and grafana monitor Nacos. Here is Nacos grafana monitoring page. You can find out for yourself how to use elastic search and influxdb.

Deploy the Nacos cluster according to the deploy document

Configure the application. properties file to expose metrics data

Access {ip}:8848/nacos/actuator/prometheus to see if metrics data can be accessed

Download the Prometheus version you want to install at the address of download prometheus

Decompress prometheus compression package

Modify configuration file prometheus.yml to collect Nacos metrics data

Start prometheus service

Download the corresponding version of Windows and decompress it

Modify configuration file prometheus.yml to collect Nacos metrics data

Start prometheus service

By accessing http://{ip}:9090/graph, we can see the data collected by prometheus. By searching nacos_monitor in the search bar, we can find Nacos data to show the success of the data collection.

Install grafana on the same machine as prometheus, and use yum to install grafana

Reference document：http://docs.grafana.org/installation/windows/

Access grafana: http://{ip}:3000

Configuring prometheus data source

Import Nacos grafana monitoring template

Nacos monitoring is divided into three modules:

When Nacos runs out of order, Grafana can alert the person in charge. Grafana supports a variety of police alert. Mail, DingTalk and webhook are commonly used.

Configure DingTalk robots

Configure DingTalk robots url

Modify defaults.ini configuration file to add mail alerts

Configuration notification mailbox

With the release of Nacos 0.9, Nacos-Sync 0.3 supports metrics monitoring. It can observe the running status of Nacos-Sync service through metrics data, and improve the monitoring capability of Nacos-Sync in production environment. Reference for the Construction of the Overall Monitoring System Nacos Monitoring Manual

The same as Nacos monitoring, Nacos-Sync also provides monitoring templates to import monitoring Nacos-Sync templates

Nacos-Sync monitoring is also divided into three modules:

Nacos-Sync metrics is divided into JVM layer and application layer

**Examples:**

Example 1 (unknown):
```unknown
management.endpoints.web.exposure.include=*
```

Example 2 (unknown):
```unknown
tar xvfz prometheus-*.tar.gz
cd prometheus-*
```

Example 3 (unknown):
```unknown
metrics_path: '/nacos/actuator/prometheus'
    static_configs:
      - targets: ['{ip1}:8848','{ip2}:8848','{ip3}:8848']
```

Example 4 (unknown):
```unknown
./prometheus --config.file="prometheus.yml"
```

---
