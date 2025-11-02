# Nacos - Service Discovery

**Pages:** 1

---

## Nacos service discovery performance test report

**URL:** https://nacos.io/en-us/docs/nacos-naming-benchmark.html

**Contents:**
- Nacos service discovery performance test report
- Test purposes
- Testing tools
- Test environment
  - 1.environment
  - 2.Set the launch parameters
- Test scenarios
- Test data
  - 1. register instance
  - 2. query instance

Main understanding Nacos service discovery performance load and capacity, to help us better manage Nacos performance quality, help users use of assessment Nacos system load faster.

We use the research of PAS performance evaluation service platform for pressure measurement, the principle is based on the use of JMeter engine, the use of PAS to automatically generate the JMeter scripts, intelligent pressure measurement.

The following test scenarios are service discovery interface:

Nacos service discovery registry instance the performance of the interface, call the HTTP interface test. The measured 3 nodes cluster performance under different pressure:

Nacos service discovery query instance of the performance of the interface, call the HTTP interface test. The measured 3 nodes cluster performance under different pressure:

Nacos service discovery delete instance is given to the performance of the interface, call the HTTP interface test. The measured 3 nodes cluster performance under different pressure:

Nacos service discovery performance test is aimed at a key function, through the pressure test was carried out on the 3 nodes cluster, can see the interface performance load and capacity.

The tests only temporary instance/query/cancellation of registration, no persistent instance (subsequent);

This test provides you as reference, if there are any deficiency or deviation, please correct me! If you have any other requirements on the performance, can you give us the issue.

**Examples:**

Example 1 (unknown):
```unknown
/opt/taobao/java/bin/java	 -server
-Xms20g
-Xmx20g
-Xmn10g	 -XX:MetaspaceSize=128m
-XX:MaxMetaspaceSize=320m
-XX:-OmitStackTraceInFastThrow
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=/home/admin/nacos/logs/java_heapdump.hprof
-XX:-UseLargePages
-Djava.ext.dirs=/opt/taobao/java/jre/lib/ext:/opt/taobao/java/lib/ext:/home/admin/nacos/plugi
ns/cmdb:/home/admin/nacos/plugins/mysql	 -Xloggc:/home/admin/nacos/logs/nacos_gc.log
-verbose:gc	 -XX:+PrintGCDetails	 -XX:+PrintGCDateStamps	 -XX:+PrintGCTimeStamps
-XX:+UseGCLogFileRotation
-XX:NumberOfGCLogFiles=10	 -XX:GCLogFileSize=100M	 -Xdebug
-Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=8000
-Dnacos.home=/home/admin/nacos	 -jar	 /home/admin/nacos/target/nacos-server.jar
--spring.config.location=classpath:/,classpath:/config/,file:./,file:./config/,file:/home/admin/naco
s/conf/	--logging.config=/home/admin/nacos/conf/nacos-logback.xml	nacos.nacos
```

---
