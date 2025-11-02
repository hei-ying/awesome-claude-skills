# Nacos - Getting Started

**Pages:** 8

---

## Cluster deployment instructions

**URL:** https://nacos.io/en-us/docs/cluster-mode-quick-start.html

**Contents:**
- Cluster deployment instructions
- Cluster Mode Deployment
  - Cluster Deployment Architecture
- 1. Preparing for the Environment
- 2. Download source code or installation package
  - Download source code from Github
  - Download Compressed Packet after Compilation
- 3. Configuration Cluster Profile
- 4. Determine The DataSource
  - Using built-in data sources

This Quick Start Manual is to help you quickly download, install and use Nacos on your computer to deploy the cluster mode for production use.

Therefore, when it is open source, it is recommended that users put all server lists under a vip and then hang under a domain name.

Http://ip1:port/openAPI Directly connected to ip mode, the machine needs to be modified to use ip.

Http://SLB:port/openAPI Mount the SLB mode(Intranet, do not expose internet to avoid security risks), directly connect to SLB, the following server ip real ip, readability is not good.

Http://nacos.com:port/openAPI Domain name + SLB mode(Intranet, do not expose internet to avoid security risks), good readability, and easy to change ip, recommended mode

Make sure that it is installed and used in the environment:

You can get Nacos in two ways.

In the Nacos decompression directory Nacos / conf directory, there is a configuration file cluster. conf, please configure each line as ip: port.

No configuration is required

production and use recommendations at least backup mode, or high availability database.

sql statement source file

application.properties configuration file

Using built-in data sources

Use an external data source

curl -X PUT 'http://127.0.0.1:8848/nacos/v1/ns/instance?serviceName=nacos.naming.serviceName&ip=20.18.7.10&port=8080'

curl -X GET 'http://127.0.0.1:8848/nacos/v1/ns/instance/list?serviceName=nacos.naming.serviceName'

curl -X POST "http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=nacos.cfg.dataId&group=test&content=helloWorld"

curl -X GET "http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=nacos.cfg.dataId&group=test"

**Examples:**

Example 1 (bash):
```bash
unzip nacos-source.zip
cd nacos/
mvn -Prelease-nacos clean install -U  
cd nacos/distribution/target/nacos-server-1.3.0/nacos/bin
```

Example 2 (bash):
```bash
unzip nacos-server-1.3.0.zip or tar -xvf nacos-server-1.3.0.tar.gz
  cd nacos/bin
```

Example 3 (plain):
```plain
# ip:port
200.8.9.16:8848
200.8.9.17:8848
200.8.9.18:8848
```

Example 4 (bash):
```bash
sh startup.sh -m standalone
```

---

## Quick Start for Nacos

**URL:** https://nacos.io/en-us/docs/v2/quickstart/quick-start.html

**Contents:**
- Quick Start for Nacos
- 0.Choose Version
- 1.Prerequisites
- 2.Download & Build from Release
  - 1)Download source code from Github
  - 2)Download run package
- 3.Setting Configuration
- 4.Start Server
  - Linux/Unix/Mac
  - Windows

This topic is about how to set up and use Nacos.

You can see the introduction of each version at release notes or blog, the current recommended version is 2.1.1.

Before you begin, install the following:

There are two ways to get Nacos.

Select the latest stable version from https://github.com/alibaba/nacos/releases

Must do this setting in 2.2.0.1 and 2.2.1, otherwise fail to start.

Setting configuration file application.properties under conf.

Setting nacos.core.auth.plugin.nacos.token.secret.key parameter，detail see Authentication-Custom SecretKey.

Attention，Default value in Document SecretKey012345678901234567890123456789012345678901234567890123456789 and VGhpc0lzTXlDdXN0b21TZWNyZXRLZXkwMTIzNDU2Nzg= is a public default, only should use in test temporary. Please make sure to replace it with another valid value when you actually deploy.

Run the following command to start(standalone means non-cluster mode):

sh startup.sh -m standalone

If you are using a ubuntu system, or encounter this error message [[symbol not found, try running as follows:

bash startup.sh -m standalone

Run the following command to start(standalone means non-cluster mode):

cmd startup.cmd -m standalone

curl -X POST 'http://127.0.0.1:8848/nacos/v1/ns/instance?serviceName=nacos.naming.serviceName&ip=20.18.7.10&port=8080'

curl -X GET 'http://127.0.0.1:8848/nacos/v1/ns/instance/list?serviceName=nacos.naming.serviceName'

curl -X POST "http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=nacos.cfg.dataId&group=test&content=helloWorld"

curl -X GET "http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=nacos.cfg.dataId&group=test"

Or click the shutdown.cmd file operation.

**Examples:**

Example 1 (bash):
```bash
git clone https://github.com/alibaba/nacos.git
cd nacos/
mvn -Prelease-nacos -Dmaven.test.skip=true clean install -U 
ls -al distribution/target/

// change the $version to your actual path
cd distribution/target/nacos-server-$version/nacos/bin
```

Example 2 (bash):
```bash
unzip nacos-server-$version.zip  OR tar -xvf nacos-server-$version.tar.gz
  cd nacos/bin
```

---

## Quick Start for Nacos

**URL:** https://nacos.io/en-us/docs/quick-start.html

**Contents:**
- Quick Start for Nacos
- 0.Choose Version
- 1.Prerequisites
- 2.Download & Build from Release
  - 1)Download source code from Github
  - 2)Download run package
- 3.Start Server
  - Linux/Unix/Mac
  - Windows
- 4.Service & Configuration Management

This topic is about how to set up and use Nacos.

Nacos 1.X is old version. Recommend you use 2.X version. Please move to document.

You can see the introduction of each version at release notes or blog, the current recommended version is 2.1.1.

Before you begin, install the following:

There are two ways to get Nacos.

Select the latest stable version from https://github.com/alibaba/nacos/releases

Run the following command to start(standalone means non-cluster mode):

sh startup.sh -m standalone

If you are using a ubuntu system, or encounter this error message [[symbol not found, try running as follows:

bash startup.sh -m standalone

Run the following command to start(standalone means non-cluster mode):

cmd startup.cmd -m standalone

curl -X POST 'http://127.0.0.1:8848/nacos/v1/ns/instance?serviceName=nacos.naming.serviceName&ip=20.18.7.10&port=8080'

curl -X GET 'http://127.0.0.1:8848/nacos/v1/ns/instance/list?serviceName=nacos.naming.serviceName'

curl -X POST "http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=nacos.cfg.dataId&group=test&content=helloWorld"

curl -X GET "http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=nacos.cfg.dataId&group=test"

Or click the shutdown.cmd file operation.

**Examples:**

Example 1 (bash):
```bash
git clone https://github.com/alibaba/nacos.git
cd nacos/
mvn -Prelease-nacos -Dmaven.test.skip=true clean install -U 
ls -al distribution/target/

// change the $version to your actual path
cd distribution/target/nacos-server-$version/nacos/bin
```

Example 2 (bash):
```bash
unzip nacos-server-$version.zip  OR tar -xvf nacos-server-$version.tar.gz
  cd nacos/bin
```

---

## Quick Start for Nacos Docker

**URL:** https://nacos.io/en-us/docs/quick-start-docker.html

**Contents:**
- Quick Start for Nacos Docker
- Steps
- Common property configuration
- Nacos + Grafana + Prometheus
- Related Projects

Run the following command：

To use MySQL 5.7, run

Open the Nacos console in your browser

link：http://127.0.0.1:8848/nacos/

Usage reference：Nacos monitor-guide

Note: When Grafana creates a new data source, the data source address must be http://prometheus:9090

**Examples:**

Example 1 (powershell):
```powershell
git clone https://github.com/nacos-group/nacos-docker.git
cd nacos-docker
```

Example 2 (powershell):
```powershell
docker-compose -f example/standalone-derby.yaml up
```

Example 3 (powershell):
```powershell
docker-compose -f example/standalone-mysql-5.7.yaml up
```

Example 4 (powershell):
```powershell
docker-compose -f example/standalone-mysql-8.yaml up
```

---

## Quick Start for Nacos Spring Boot Projects

**URL:** https://nacos.io/en-us/docs/quick-start-spring-boot.html

**Contents:**
- Quick Start for Nacos Spring Boot Projects
- Prerequisite
- Enable Configuration Service
- Enable Service Discovery
- Related Projects

This quick start introduces how to enable Nacos configuration management and service discovery features for your Spring Boot project.

For more details about Nacos Spring Boot: nacos-spring-boot-project.

The quick start includes two samples:

Follow instructions in Nacos Quick Start to download Nacos and start the Nacos server.

Once you start the Nacos server, you can follow the steps below to enable the Nacos configuration management service for your Spring Boot project.

Sample project: nacos-spring-boot-config-example

Note: Version 0.2.x.RELEASE is compatible with the Spring Boot 2.0.x line. Version 0.1.x.RELEASE is compatible with the Spring Boot 1.x line.

Start NacosConfigApplicationand call curl http://localhost:8080/config/get. You will get a return message of false, as no configuration has been published so far.

Call Nacos Open API to publish a configuration to the Nacos server. Assume the dataId is example, and the content is useLocalCache=true.

Now you would also like to enable the service discovery feature of Nacos in your Spring Boot project.

Sample project: nacos-spring-boot-discovery-example

Note: Version 0.2.x.RELEASE is compatible with the Spring Boot 2.0.x line. Version 0.1.x.RELEASE is compatible with the Spring Boot 1.x line.

Start NacosDiscoveryApplicationand call curl http://localhost:8080/discovery/get?serviceName=example，you will get a return value of an empty JSON array [].

Call Nacos Open API to register a service called example to the Nacos server.

**Examples:**

Example 1 (unknown):
```unknown
<dependency>
    <groupId>com.alibaba.boot</groupId>
    <artifactId>nacos-config-spring-boot-starter</artifactId>
    <version>${latest.version}</version>
</dependency>
```

Example 2 (unknown):
```unknown
nacos.config.server-addr=127.0.0.1:8848
```

Example 3 (plain):
```plain
@SpringBootApplication
@NacosPropertySource(dataId = "example", autoRefreshed = true)
public class NacosConfigApplication {

    public static void main(String[] args) {
        SpringApplication.run(NacosConfigApplication.class, args);
    }
}
```

Example 4 (unknown):
```unknown
@Controller
@RequestMapping("config")
public class ConfigController {

    @NacosValue(value = "${useLocalCache:false}", autoRefreshed = true)
    private boolean useLocalCache;

    @RequestMapping(value = "/get", method = GET)
    @ResponseBody
    public boolean get() {
        return useLocalCache;
    }
}
```

---

## Quick Start for Nacos Spring Cloud Projects

**URL:** https://nacos.io/en-us/docs/quick-start-spring-cloud.html

**Contents:**
- Quick Start for Nacos Spring Cloud Projects
- Prerequisite
- Enable Configuration Service
- Enable Service Discovery
- Related Projects

This quick start introduces how to enable Nacos configuration management and service discovery features for your Spring Cloud project.

For more details about Nacos Spring Cloud: Nacos Config and Nacos Discovery.

The quick start includes two samples:

Follow instructions in Nacos Quick Start to download Nacos and start the Nacos server.

Once you start the Nacos server, you can follow the steps below to enable the Nacos configuration management service for your Spring Cloud project.

Sample project: nacos-spring-cloud-config-example

Note: Version 2.1.x.RELEASE is compatible with the Spring Boot 2.1.x line. Version 2.0.x.RELEASE is compatible with the Spring Boot 2.0.x line. Version 1.5.x.RELEASE is compatible with the Spring Boot 1.5.x line.

Note: The value of spring.application.name will be used to construct part of the dataId in Nacos configuration management.

In Nacos Spring Cloud, the format of dataId is as follows:

Run NacosConfigApplicationand call curl http://localhost:8080/config/get，You will get a returned value of true.

Call Nacos Open API again to publish an updated configuration to the Nacos server. Assume the dataId isexample.properties，and the content is useLocalCache=false.

Now you would also like to enable the service discovery feature of Nacos in your Spring Cloud project.

Sample project: nacos-spring-cloud-discovery-example

Note: Version 2.1.x.RELEASE is compatible with the Spring Boot 2.1.x line. Version 2.0.x.RELEASE is compatible with the Spring Boot 2.0.x line. Version 1.5.x.RELEASE is compatible with the Spring Boot 1.5.x line.

i. Add the Nacos server address in application.properties :

ii. Enable service discovery by adding the Spring Cloud native annotation of @EnableDiscoveryClient:

i. Configure the Nacos server address in application.properties :

ii. Add the Spring Cloud native annotation of @EnableDiscoveryClient to enable service discovery. Add the @LoadBalanced annotation for the RestTemplate instance, and enable the integration of @LoadBalanced and Ribbon:

**Examples:**

Example 1 (unknown):
```unknown
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
    <version>${latest.version}</version>
</dependency>
```

Example 2 (unknown):
```unknown
spring.cloud.nacos.config.server-addr=127.0.0.1:8848

spring.application.name=example
```

Example 3 (plain):
```plain
${prefix}-${spring.profiles.active}.${file-extension}
```

Example 4 (unknown):
```unknown
@RestController
@RequestMapping("/config")
@RefreshScope
public class ConfigController {

    @Value("${useLocalCache:false}")
    private boolean useLocalCache;

    @RequestMapping("/get")
    public boolean get() {
        return useLocalCache;
    }
}
```

---

## Quick Start for Nacos Spring Projects

**URL:** https://nacos.io/en-us/docs/quick-start-spring.html

**Contents:**
- Quick Start for Nacos Spring Projects
- Prerequisite
- Enable Configuration Service
- Enable Service Discovery
- Related Projects

This quick start introduces how to enable Nacos configuration management and service discovery features for your Spring project.

For more details about Nacos Spring Boot: nacos-spring-project.

The quick start includes two samples:

Follow instructions in Nacos Quick Start to download Nacos and start the Nacos server.

Once you start the Nacos server, you can follow the steps below to enable the Nacos configuration management service for your Spring project.

Sample project: nacos-spring-config-example

The the latest version can be available in maven repositories such as "mvnrepository.com".

Start Tomcat and call curl http://localhost:8080/config/get to get configuration information. Because no configuration has been published, a falsemessage is returned.

Now you can call Nacos Open API to publish a configruation to the Nacos server. Assume the dataId is example, and content is useLocalCache=true.

Now you would like to enable the service discovery function of Nacos in your Spring project.

Sampe project: nacos-spring-discovery-example

The the latest version can be available in maven repositories such as "mvnrepository.com".

Start Tomcat and call curl http://localhost:8080/discovery/get?serviceName=example, and the return value is an empty JSON array [].

Call Nacos Open API to register a service called exampleto the Nacos Server.

**Examples:**

Example 1 (unknown):
```unknown
<dependency>
    <groupId>com.alibaba.nacos</groupId>
    <artifactId>nacos-spring-context</artifactId>
    <version>${latest.version}</version>
</dependency>
```

Example 2 (unknown):
```unknown
@Configuration
@EnableNacosConfig(globalProperties = @NacosProperties(serverAddr = "127.0.0.1:8848"))
@NacosPropertySource(dataId = "example", autoRefreshed = true)
public class NacosConfiguration {

}
```

Example 3 (unknown):
```unknown
@Controller
@RequestMapping("config")
public class ConfigController {

    @NacosValue(value = "${useLocalCache:false}", autoRefreshed = true)
    private boolean useLocalCache;

    @RequestMapping(value = "/get", method = GET)
    @ResponseBody
    public boolean get() {
        return useLocalCache;
    }
}
```

Example 4 (unknown):
```unknown
curl -X POST "http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=example&group=DEFAULT_GROUP&content=useLocalCache=true"
```

---

## What is Nacos

**URL:** https://nacos.io/en-us/docs/what-is-nacos.html

**Contents:**
- What is Nacos
- Overview
- What is Nacos？
- Nacos Map
- Nacos landscape
- What’s next

Nacos /nɑ:kəʊs/ is the acronym for 'Dynamic Naming and Configuration Service'，an easy-to-use dynamic service discovery, configuration and service management platform for building cloud native applications。

Nacos is committed to help you discover, configure, and manage your microservices. It provides a set of simple and useful features enabling you to realize dynamic service discovery, service configuration, service metadata and traffic management.

Nacos makes it easier and faster to construct, deliver and manage your microservices platform. It is the infrastructure that supports a service-centered modern application architecture with a microservices or cloud-native approach.

Service is a first-class citizen in Nacos. Nacos supports discovering, configuring, and managing almost all types of services:

gRPC & Dubbo RPC Service

Spring Cloud RESTful Service

Key features of Nacos:

Service Discovery And Service Health Check

Nacos supports both DNS-based and RPC-based (Dubbo/gRPC) service discovery. After a service provider registers a service with native, OpenAPI, or a dedicated agent, a consumer can discover the service with either DNS or HTTP.

Nacos provides real-time health check to prevent services from sending requests to unhealthy hosts or service instances. Nacos supports both transport layer (PING or TCP) health check and application layer (such as HTTP, Redis, MySQL, and user-defined protocol) health check. For the health check of complex clouds and network topologies(such as VPC, Edge Service etc), Nacos provides both agent mode and server mode health check. Nacos also provide a unity service health dashboard to help you manage the availability and traffic of services.

Dynamic configuration management

Dynamic configuration service allows you to manage the configuration of all applications and services in a centralized, externalized and dynamic manner across all environments.

Dynamic configuration eliminates the need to redeploy applications and services when configurations are updated.

Centralized management of configuration makes it more convenient for you to achieve stateless services and elastic expansion of service instances on-demand.

Nacos provides an easy-to-use UI (DEMO) to help you manage all of your application or services's configurations. It provides some out-of-box features including configuration version tracking, canary/beta release, configuration rollback, and client configuration update status tracking to ensure the safety and control the risk of configuration change.

Dynamic DNS service which supports weighted routing makes it easier for you to implement mid-tier load balancing, flexible routing policies, traffic control, and simple DNS resolution services in your production environment within your data center. Dynamic DNS service makes it easier for you to implement DNS-based Service discovery.

Nacos provides some simple DNS APIs TODO for you to manage your DNS domain names and IPs.

Service governance and metadata management

Nacos allows you to manage all of your services and metadata from the perspective of a microservices platform builder. This includes managing service description, life cycle, service static dependencies analysis, service health status, service traffic management，routing and security rules, service SLA, and first line metrics.

Check more features ...

A picture to understand Nacos, the following structure will be described in detail.

// TODO this picture need to translate.

As the figure above shows, Nacos seamlessly supports open source ecologies including Dubbo and Dubbo Mesh, Spring Cloud, and Kubernetes and CNCF.

Use Nacos to simplify your solutions in service discovery, configuration management, and service governance and management. With Nacos, microservices management in open source system is easy.

For more information about how to use Nacos with other open source projects, see the following:

Use Nacos with Kubernetes

Use Nacos with Spring Cloud

Continue with quick start to get started with Nacos.

---
