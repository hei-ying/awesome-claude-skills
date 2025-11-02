# Nacos - Configuration

**Pages:** 12

---

## Authentication

**URL:** https://nacos.io/en-us/docs/auth.html

**Contents:**
- Authentication
- Use Authentication in Servers
  - Without Docker
    - Custom SecretKey
  - With Docker
    - Official images
    - Custom images
- Authentication in Clients
  - Authentication in Java SDK
    - Example Code

By default, no login is required to start following the official document configuration, which can expose the configuration center directly to the outside world. However, if the authentication is enabled, one can use nacos only after he configures the user name and password.

Before enabling authentication, the configuration in application.properties is as follow:

After enabling authentication, the configuration in application.properties is as follow:

After enabling authentication, you can customize the key used to generate JWT tokens，the configuration in application.properties is as follow：

When customizing the key, it is recommended to set the configuration item to a Base64 encoded string, and the length of the original key must not be less than 32 characters. For example the following example:

Attention: the authentication switch takes effect immediately after the modification, and there is no need to restart the server.

If you choose to use official images, please add the following environment parameter when you start a docker container.

For example, you can run this command to run a docker container with Authentication:

Besides, you can also add the other related enviroment parameters:

If you choose to use custom images, please modify the application.properties before you start nacos, change this line

The user name and password should be set when creating a 'Properties' class.

Firstly, the user name and password should be provided to login.

If the user name and password are correct, the response will be:

Secondly, when using configuration services or naming services, accessToken in the previous response should be provided. To use the accessToken, 'accessToken=${accessToken}' should be appended at the end of request url, e.g.,

After the authentication feature is enabled, requests between servers will also be affected by the authentication system. Considering that the communication between the servers should be credible, during the 1.2~1.4.0 version, Nacos server use whether the User-Agent includes Nacos-Server to determine whether the request comes from other servers.

However, this implementation is too simple and fixed, leading to possible security issues. Therefore, since version 1.4.1, Nacos has added the server identification feature. Users can configure the identity of the server by themselves, and no longer use User-Agent as the judgment standard for server requests.

Way to open server identity

Attention All servers in cluster need to be configured with the same server.identity information, otherwise it may cause data inconsistency between servers or failure to delete instances.

Considering that users of the old version need to upgrade, users can turn on the nacos.core.auth.enable.userAgentAuthWhite=true during upgrading, and turn off it after the cluster is upgraded to 1.4.1 completely and runs stably.

**Examples:**

Example 1 (java):
```java
### If turn on auth system:
nacos.core.auth.enabled=false
```

Example 2 (java):
```java
### If turn on auth system:
nacos.core.auth.system.type=nacos
nacos.core.auth.enabled=true
```

Example 3 (properties):
```properties
### The default token(Base64 String):
nacos.core.auth.default.token.secret.key=SecretKey012345678901234567890123456789012345678901234567890123456789
```

Example 4 (properties):
```properties
### The default token(Base64 String):
nacos.core.auth.default.token.secret.key=VGhpc0lzTXlDdXN0b21TZWNyZXRLZXkwMTIzNDU2Nzg=
```

---

## Console Guide

**URL:** https://nacos.io/en-us/docs/console-guide.html

**Contents:**
- Console Guide
- Features
  - Service management
    - Service list management
    - Service flow weighted support and protection
    - Service metadata management
    - Service elegant line up and down
  - Configuration management
    - More configuration format editor
    - Edit DIFF

Nacos console aims to enhance the console for service list, health management, service management, a distributed configuration management control ability, in order to help users reduce the cost of micro management service application architecture, will provide basic functions include the following:

Developer or operations staff often require after service registry, through friendly interface to view the service registration situation, the current system, including the registration of all of the details of the services and each service.And in a case, with access control service of some of the configuration editor.Nacos in this version of open service found that part of the console, main is to provide users a basic operations page, to view, edit, the current registration services.

Service list to help users with a unified view management of all its service and health status.The overall layout is the upper left corner services and search box to search button, the page is the central service list.Service main display service name list, the cluster number, number of instances, health instance number and details button five columns.

In the service list page click details, you can see details of the service.Can look at the service, the basic information of the cluster and examples.

Nacos flow provides the user with the ability of weight control, open the threshold of service flow protection at the same time, in order to help users better protection service cluster service providers are not accidentally break.The diagram below so, click the edit button instance, modify instance weights.If you want to increase the flow of instance, to turn up the weight, if you don't want to flow method receives the instance, the weight can be set to 0.

Nacos provide multiple dimensions of service metadata exposed, help users to store the information of the custom.This information is based on data storage structure, K - V on the console, as to the k1 = v1, k2 = v2 show such format.Similarly, edit the metadata can be performed by the same format.Such as service metadata editing, first click on the service details in the top right corner of the page "edit service" button, and then in the metadata input: input box version = 1.0, env = prod.

Click on the confirmation, you can in the service details page, see the service metadata has been updated.

Nacos also offers the service instance line operation, up and down in the service details page, you can click on the instance of "on-line" or "off" button, the offline instance, cases of health will not be included in the list.

Nacos support Group configuration based on the Namespace and Group management, so that users more flexible according to their own needs in accordance with the environment or application, module, such as grouping management services as well as the configuration of Spring, in the configuration management major provides configuration version history, rollback, subscriber query such as the core management abilities.

Nacos support YAML, Properties, TEXT, JSON, XML, HTML and other common configuration format online editing, syntax highlighting, format check, help users efficiently edit at the same time greatly reduced the risks of format error.

Nacos support configuration tag ability, help users better and more flexible to the configuration of the classification and management based on the tag.Description of configuration and its change is support users at the same time, people or cross team collaboration management configuration.

Nacos supports editing a DIFF ability, help the user to check the changes, and reduce the risks of correction.

Nacos provide sample code ability, can let a novice quickly using client-side programming consumption this configuration, novice slash barriers.

Nacos provide configuration subscriber is the listener query ability, at the same time provide Client MD5 checksum value of the current configuration, in order to help users better check configuration changes pushed to the Client side.

Nacos by providing a key roll back configuration version management and its ability, help users can configure to quick recovery, reduce the micro service system in configuration management will meet the availability of the risk.

Nacos based in Namespace helps users logic isolation based multiple namespaces, this can help users better management testing, service and configure the pretest, production environment, so that the same configuration environment (such as database data sources) can define different values.

Nacos 0.8 version supports simple login function, the default username/password for: nacos/nacos.

As part of its own development console, do not want to be nacos security filter interceptor.Therefore nacos support custom close the login functionFind the configuration file ${nacoshome}/conf/application.properties. The properties, replace the following content.

The default session to keep time for 30 minutes.After 30 minutes need to login authentication.Temporarily does not support to modify the default time.

In Nacos front style, the layout of the discussion, the community vote, finally choose the style of the classic black and white and blue skin, and through our UED Yao Cheng design, layout, make interaction is very natural.

In the development of the console, we recruited through community many front students to participate in the development of the front-end code, in this especially thank Chen Li, Qing Wang, Yanmin Wang Nacos front-end development process in the strong support!

DISS is cheap, show me your hand!

To join Nacos WeChat community discussion Nacos the evolution of the product, you can sweep through xuechaos WeChat QRcode, let "xuechaos" help you pull in "Nacos community communication group".

More Nacos related open source project information:

**Examples:**

Example 1 (unknown):
```unknown
public class PasswordEncoderUtil {

    public static void main(String[] args) {
        System.out.println(new BCryptPasswordEncoder().encode("nacos"));
    }
}
```

Example 2 (unknown):
```unknown
INSERT INTO users (username, password, enabled) VALUES ('nacos', '$2a$10$EuWPZHzz32dJN7jexM34MOeYirDdFAZm2kuWj7VEOJhhZkDrxfvUu', TRUE);
INSERT INTO roles (username, role) VALUES ('nacos', 'ROLE_ADMIN');
```

Example 3 (unknown):
```unknown
## spring security config
### turn off security
spring.security.enabled=false
management.security=false
security.basic.enabled=false
nacos.security.ignore.urls=/**

#nacos.security.ignore.urls=/,/**/*.css,/**/*.js,/**/*.html,/**/*.map,/**/*.svg,/**/*.png,/**/*.ico,/console-fe/public/**,/v1/auth/login,/v1/console/health,/v1/cs/**,/v1/ns/**,/v1/cmdb/**,/actuator/**
```

---

## FAQ

**URL:** https://nacos.io/en-us/docs/faq.html

**Contents:**
- FAQ
- Nacos standard questions
    - What is Nacos
    - Nacos how to support more than the environment
    - Nacos whether production is available
    - Nacos version plan
    - Nacos dependent
    - Nacos using open source licenses
- Nacos operational questions
    - Nacos standalone deployment

Nacos standard questions

Nacos operational questions

Nacos principle questions

Nacos dedicated to help you find, micro configuration and management services. Nacos provides a set of simple and easy to use feature set, help you quickly realize dynamic service discovery, service configuration, service metadata, and traffic management. Details you can refer to Nacos website.

In daily use are often need different environment, such as daily, pretest, online environment, if it is a logical isolation, can use the namespace Nacos support namespace to support more environmental isolation, can create multiple namespaces in Nacos console. If you need physical isolation, will deploy more sets of Nacos environment.

Nacos in January 2019 issued a Pre - GA version, to support the security isolation, monitoring and service migration on the last mile of production, in a more stable support the user's production environment. Details you can refer to Nacos release v0.8.0 Pre - GA version, the safe and stable production.

Nacos 0.8.0 to support production available, version 1.0 to mass production is available, version 2.0 plan and K8s, Spring Cloud, and further integration Service Mesh, Serverless, details you can refer to Nacos roadmap.

In stand-alone mode, Nacos without any rely on, in cluster mode, Nacos rely on Mysql storage, details you can refer to Nacos deployment.

Nacos using Apache 2.0.

You can refer to the manual Nacos website deployment quick start.

Nacos stand-alone mode defaults to using the embedded database as the storage engine, if you want to change your mysql installation, you can refer to website document.

Production environment using Nacos in order to achieve high availability cannot use stand-alone mode, need to build Nacos cluster, specific details can refer to the manual cluster deployment.

In addition to using compressed package deployment Nacos, Nacos also provides a corresponding Docker image, when Nacos release new versions, Nacos will release the corresponding image version supports Docker deployment.Specific details you can refer to Nacos Docker.

In production deployment Nacos cluster, if for Nacos expansion operation, need to manually change the cluster IP file, start a new Nacos service.In order to automate operations, k8s Nacos and combined use of StatefulSets provides automatic operations plan, to dynamic scalability Nacos capacity, specific details reference Kubernetes Nacos.

Nacos0.8 version provides the Metrics data exposed ability, can pass the Metrics data to monitor the running status of Nacos, the content of the details you can refer to Nacos monitor.

The reason may be due to insufficient memory in the Docker environment, causing other services to fail to start normally, and finally causing the service to report an error and keep restarting. You can try to solve it by increasing the Docker memory limit.

Can through the Nacos - Sync moved the Zookeeper service and Nacos, can also be migrated from Nacos Zookeeper, specific details can be used as Nacos Sync reference.

Nacos through Spring Cloud Alibaba Nacos Config support multiple configuration files, configuration can be stored in a separate configuration file.The associated issue, details refer to the document Spring Cloud Alibaba Nacos Config.

Nacos version 0.6 and Dubbo integration, support the use of Nacos as registry, related issue, details refer to the document Nacos and Dubbo fusion become registry.

Nacos perfect supports the Sping technology stack, details refer to the document Nacos Spring、Nacos Spring Boot、Spring Cloud.

Nacos network interaction is implemented based on Http protocol, provides the Open-API can easily achieve Nacos access.

Nacos currently only supports Java, support for other languages are being developed, also need your support to build together.

Nacos version 0.8 when using its and no JAVA_HOME environment variable, Nacos can launch successful, because yum install installed its the Java command to register a beneath /bin directory, and so can cause abnormal SignatureException.This problem has been repair, version 0.9 release, the specific details can refer to the issue.

This problem because Nacos get native IP, don't get to the correct external IP. The need to guarantee the InetAddress.getLocalHost().getHostAddress() or the result of the hostname -i was with the cluster. The conf configuration of IP is the same.

Nacos plan in 1.X version's ability to provide encryption, currently does not support encryption, can only rely on the SDK prepared encryption endures Nacos again.

Nacos server error, check the server logs, refer to the issue.

Nacos console editors weights, at present from SpringCloud client and Dubbo client didn't get through, so can't take effect. For SpringCloud client application can realize the load balancer Ribbon for weighting filter.

Currently supported modify the cluster.conf file in a way that expanding capacity, after the change without restart, the Server will automatically refresh the new content to the file.

Configuration - D parameters com.alibaba.nacos.naming.log.level set naming the client log level, such as setting for the error:-Dcom.alibaba.nacos.naming.log.level=error Similarly, - D parameters com.alibaba.nacos.config.log.level is used to set the config client log level.

Configuration spring-cloud-seluth parameters: spring.zipkin.discovery-client-enabled=false.

If there is still a Service not found error, is recommended to use the open-api will Zipkin-server instance is registered as a permanent Service:

curl -X POST 'http://127.0.0.1:8848/nacos/v1/ns/instance?port=9411&healthy=true&ip=127.0.0.1&weight=1.0&serviceName=zipkin-server&ephemeral=false&namespaceId=public'

Then, went to nacos console, find a service called zipkin-server service, find the cluster configuration, set the health examination mode to TCP, port number of 9411 (zipkin-server port).

This problem appeared in cluster mode, in the use of nacos cluster pattern, ensure that all of the machine time is consistent, can appear otherwise unable to synchronize data.

This package will be auto-generated by protobuf, so if you want to read source code or do some develop, you can use mvn compile to generate them. If you are using IDEA, you can also use IDEA's protobuf plugin.

Service - a service in 192.168.31.114 192.168.31.115, 192.168.31.116 launched three instances. We are thinking of them 192.168.31.114 instance configuration items ". The user password "to change the value of XXX (i.e., Beta release), 192.168.31.115, 192.168.31.116 configuration does not change.

---

## Java SDK

**URL:** https://nacos.io/en-us/docs/sdk.html

**Contents:**
- Java SDK
- Overview
- Configuration Management
  - Get configuration
    - Description
    - Request parameters
    - Return values
    - Request example
    - Exception specification
  - Listen configuration

The latest version of 1.X is 1.4.4

Get configuration from Nacos when a service starts.

A ConfigException is thrown in case of a configuration read time-out or a network error.

Use dynamic configuration listening API to enable Nacos to send configuration change notifications.

Cancel listen configuration. No more notification after cancellation.

Publish Nacos configurations automatically to reduce the operation and maintenance cost.

Note: It uses the same publishing interface to create or modify a configuration. If the specified configuration doesn’t exist, it will create a configuration. If the specified configuration exists, it will update the configuration.

In case of reading configuration timeout or network issues, ConfigException exception is thrown.

It deletes Nacos configurations automatically with program to reduce operation and maintenance costs with automation.

Note: If the specified configuration exists, then it deletes the configuration. If the specified configuration doesn’t exist, then it returns a successful message.

In case of reading configuration timeout or network issues, ConfigException exception is thrown.

Register an instance to service.

Remove instance from service.

Get all instances of service.

Get healthy or unhealthy instances of service.

Get one healthy instance selected by load-balance strategy.

Listen for changes of instances under a service.

Cancel listening service.

**Examples:**

Example 1 (unknown):
```unknown
<dependency>
    <groupId>com.alibaba.nacos</groupId>
    <artifactId>nacos-client</artifactId>
    <version>${version}</version>
</dependency>
```

Example 2 (java):
```java
public String getConfig(String dataId, String group, long timeoutMs) throws NacosException
```

Example 3 (java):
```java
try {
    // Initialize the configuration service, and the console automatically obtains the following parameters through the sample code.
	String serverAddr = "{serverAddr}";
	String dataId = "{dataId}";
	String group = "{group}";
	Properties properties = new Properties();
	properties.put("serverAddr", serverAddr);
	ConfigService configService = NacosFactory.createConfigService(properties);
    // Actively get the configuration.
	String content = configService.getConfig(dataId, group, 5000);
	System.out.println(content);
} catch (NacosException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

Example 4 (java):
```java
public void addListener(String dataId, ConfigChangeListenerAdapter listener)
```

---

## NacosSync migration user guide

**URL:** https://nacos.io/en-us/docs/nacos-sync-use.html

**Contents:**
- NacosSync migration user guide
- Guide purposes
- Preparatory work
- Get the installation package
- Initialize the database
- Database configuration
- Start server
- Check system status
- Console
- Starting migration

Before you start the service, you need to install the following services:

There are two ways to obtain NacosSync installation package:

The path of the target file:

Unpack the installation package, project file directory structure:

The system default configuration database is Mysql, can also support other relational database. 1.The database construction, the default database name for "nacos_Sync". 2.The database table don't need to create separately, using the hibernate automatically by default build table function. 3.If you do not support automatic table, you can use the system's own build table SQL script, the script in the bin directory.

Database configuration file on conf/application.properties:

The path of the log in nacosSync/logs/nacosSync.log, check whether there are abnormal information.

Port is the default system 8081, you can define your own application.properties.

If there is no problem, check NacosSync has begun, normal NacosSync deployment structure:

Dubbo service deployment information:

The migration of services:

1.Click on the "cluster configuration" button in the left navigation bar, a new cluster, first add a Zookeeper cluster, select the cluster type for ZK.

Note: the cluster name can customize, but once confirmed, cannot be modified, otherwise increase task based on the cluster, after NacosSync restart, success will not resume.

2.The same steps, increase NacosSync cluster.

3.After the completion of the add, can inquire on the list:

Add finished, can be in service sync list, view has add synchronization task:

The synchronization is completed, check whether the data synchronization to success Nacos cluster, can query through the Nacos console.

At the moment, the data has been successfully from Zookeeper cluster synchronization to Nacos cluster, the deployment structure is as follows:

Dubbo has supported Nacos registry, support version 2.5 +, need to add a Nacos registry of Dubbo extensions depends on:

Increase Nacos client depends on:

Configuration Dubbo Consumer Dubbo profile Consumer. The yaml, let the client can find Nacos cluster.

Don't need to modify the code, configuration after the update, you can restart your application into law.

Consumer release is completed, the deployment of the structure is as follows:

Before you upgrade the Provider, you need to ensure that the Provider of services, are already configured in NacosSync, synchronous way from Nacos synchronization to Zookeeper, because the Provider connected to Nacos upgrade, you need to make sure that the old Dubbo Consumer client can subscribe to the Provider's address in the Zookeeper, now, we add a sync task:

Note: Nacos synchronization to the Zookeeper service, do not need to fill in the version number, you in choosing the source cluster, the version number of the input box automatically hidden.

Sync task is completed, you can upgrade the Provider, upgrade the Provider method, reference to upgrade the Consumer steps.

Now, the Zookeeper cluster, NacosSync cluster can get offline.

**Examples:**

Example 1 (basic):
```basic
cd nacosSync/
mvn clean package -U
```

Example 2 (basic):
```basic
nacos-sync/nacossync-distribution/target/nacosSync.${version}.zip
```

Example 3 (basic):
```basic
nacosSync
├── LICENSE
├── NOTICE
├── bin
│   ├── nacosSync.sql
│   ├── shutdown.sh
│   └── startup.sh
├── conf
│   ├── application.properties
│   └── logback-spring.xml
├── logs
└── nacosSync-server.${version}.jar
```

Example 4 (basic):
```basic
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/nacos_sync?characterEncoding=utf8
spring.datasource.username=root
spring.datasource.password=root
```

---

## Nacos Concepts

**URL:** https://nacos.io/en-us/docs/concepts.html

**Contents:**
- Nacos Concepts
- Region
- Available Zone
- Endpoint
- Namespace
- Configuration
- Configuration Management
- Configuration Item
- Configuration Set
- Data ID

NOTE: Nacos introduces some basic concepts and systematic understanding of these concepts can help you better understand and correct use Nacos products.

Physical data centers, unalterable after resources are created.

Physical areas with independent power grids and networks in one region. The network latency for instances in the same zone is lower.

The entry domain name of a service in each region.

For configuration isolation by tenants. Different namespaces may have configurations with the same Group or Data ID. One of the common scenarios for namespace is to differentiate and isolate the configurations in different environments, as in development and test environment and production environment.

During system development, developers usually extract some parameters or variables that need to be changed from the code and manage them in a separate configuration file. This enables the static system artifacts or deliverables (such as WAR and JAR packages) to fit with the physical operating environment in a better way. Configuration management is usually a part of system deployment, which is executed by the administrator or operation and maintenance personnel. Configuration modification is an effective way to adjust the behavior of a running system.

Configuration-related activities including editing, storage, distribution, modification management, release version management, and modification audit.

A specific configurable parameter with its value range, generally in the form of param-key=param-value. For example, the log output level (logLevel=INFO|WARN|ERROR) of a system is regarded as a configuration item.

A collection of related or unrelated configuration items.In a system, a configuration file is generally a configuration set which contains all the configurations of the system. For example, a configuration set may contain configuration items such as data sources, thread pools, and log levels.

The ID of a configuration set in Nacos. It is one of the dimensions according to which configurations are organized. Data ID is generally used to organize the system configuration sets. A system or application can contain multiple configuration sets, each of which can be identified by a meaningful name. The Data ID usually uses the naming rule similar to Java packages (for example, com.taobao.tc.refund.log.level) to ensure global uniqueness. This naming rule is not mandatory.

The group of configuration sets in Nacos. It is one of the dimensions according to which configurations are organized. The configuration sets are always grouped by a meaningful string such as Buy or Trade to differentiate the configuration sets with the same Data ID. When you create a configuration on Nacos, the group name is replaced by DEFAULT_GROUP by default if not specified. A typical scenario of Group is when the same configuration type is used for different applications or components, such as database_url configuration and MQ_topic configuration.

The Nacos client SDK can generate snapshots of configurations on local machines. Snapshots can be used to indicate the overall disaster recovery capabilities of the system when the client cannot connect to the Nacos server. Configuration snapshot is similar to local commit in Git, or cache, which is updated at the appropriate time, but does not have the notion of expiration as in cache.

Software functions which are provided to the client via the network through a predefined interface.

Identifier provided by the service, by which the service it refers to can be uniquely determined.

Database which stores the instances of services and the load balancing policies for services.

On a computer network, the address and metadata of an instance under the service are probed (usually using a service name) and provided to the client for querying with a predefined interface.

Custom configuration information, such as a disaster recovery policy, a load balancing policy, an authentication configuration, and various tags. From the scope of action, it is divided into meta-information of service level, meta-information of virtual cluster, and meta-information of instance.

Property of service which can be used to identify the service provider.

Different services can be categorized into the same service group.

Service instances under the same service can be further classified. One possible unit of this classification is Virtual Cluster.

A process with an accessible network address (IP:Port) that provides one or more services.

Instance-level configuration. Weight is a floating-point number. The greater the weight, the greater the traffic that the instance expects to be allocated.

Health check of the instances under a service in a specified manner to ensure that the instances can work properly. Instances are judged to be healthy or unhealthy according to the inspection results. Unhealthy instances are not returned to the client when initiating a resolution request to the service.

To prevent traffic from flowing to healthy instances because of some unhealthy instances, which causes traffic pressure, healthy instance collapse, and finally an avalanche, the health protection threshold should be defined as a floating point number between 0 and 1. When the proportion of the domain name healthy instance to the total instance is smaller than this value, the instance is returned to the client regardless of the health of the instance. Although this can result in a loss of some of the traffic, we ensure that the remaining healthy instances can work normally.

---

## Nacos deployment environment

**URL:** https://nacos.io/en-us/docs/deployment.html

**Contents:**
- Nacos deployment environment
- Nacos supports three types of deployment modes
- Environment preparation
- Running Nacos in Standalone Mode
  - Linux/Unix/Mac
  - Windows
  - Running Nacos with mysql in Standalone Mode
    - Initialize MySQL database
    - application.properties configuration
- Running Nacos in Multi-Node Cluster Mode

Nacos is defined as an IDC internal application component, not a product for the public network environment. It is not recommended expose it to the public network environment directly.

All network related concepts such as VIP and network interface mentioned in the following documents are in the internal network environment.

sql statement source file

application.properties configuration file

add mysql datasource and configure url, user and password

Nacos in Multi-Node Cluster Mode

Nacos support a NameServer route request mode， by which you can design a useful mapping rule to control the request forward to the corresponding cluster, in the mapping rule you can sharding the request by namespace or by tenant etc...

to setup a NameServer:

When the local environment is complex, the Nacos service needs to choose IP or network card to use at runtime when it starts up. Nacos Gets IP Reference Spring Cloud Design from Multiple Network Cards. With the nacos.inetutils parameter, you can specify the network card and IP address used by Nacos. The configuration parameters currently supported are:

**Examples:**

Example 1 (unknown):
```unknown
spring.datasource.platform=mysql

db.num=1
db.url.0=jdbc:mysql://11.162.196.16:3306/nacos_devtest?characterEncoding=utf8&connectTimeout=1000&socketTimeout=3000&autoReconnect=true
db.user=nacos_devtest
db.password=youdontknow
```

Example 2 (unknown):
```unknown
nacos.inetutils.ip-address=10.11.105.155
```

Example 3 (unknown):
```unknown
nacos.inetutils.use-only-site-local-interfaces=true
```

Example 4 (unknown):
```unknown
nacos.inetutils.ignored-interfaces[0]=eth0
nacos.inetutils.ignored-interfaces[1]=eth1
```

---

## Nacos service configuration performance test report

**URL:** https://nacos.io/en-us/docs/nacos-config-benchmark.html

**Contents:**
- Nacos service configuration performance test report
- Test purposes
- Test tools
- Test environment
  - 1.environment
  - 2.Set the launch parameters
- Test scenarios
- Test data
  - 1. Release configuration
  - 2. Access configuration

Let everybody understand the Nacos main performance load and capacity, to help us better manage Nacos performance quality, help users use of assessment Nacos system load faster.

We use the research of PAS performance evaluation service platform for pressure measurement, the principle is based on the use of JMeter engine, the use of PAS to automatically generate the JMeter scripts, intelligent pressure measurement.

The following test scenarios are service discovery interface:

The performance of the main test launch configuration Nacos publishConfig interface. In the performance of each scale clusters:

We look at three nodes specific services cluster configuration ability. The following for each concurrency (press the machine number * concurrency), the configuration of the TPS, the average RT.

Access to configuration for Nacos getConfig interface for testing. The measured performance in each cluster size:

We also look at the three nodes specific services cluster acquire configuration, the following for each concurrency (pressure machine is used for * concurrency), access to configuration of TPS, the average RT.

Perform Nacos addListeners the performance of the interface to monitor configuration mainly adopts increase more configuration monitoring, and issued several configuration method, statistics released time and listening to receive configuration time interval. We pick a few points, and lists the publish and listening time, the basic within 100 ms can listen to the configuration changes.

Nacos listener configuration with the client to establish long connection, long service connection consumes memory, thereby cluster increased load.Build up capability of the capacity of long connection, mainly examines configuration monitor bottlenecks. Cluster connectivity test methods are increasing stand-alone connection to reach 9000, CPU: 13.9% memory: 18.8%, load: 4.7, are in normal state, the number of connections increases, the load will increase exponentially number level. In each cluster scale test basically conform to test and verify.

Nacos performance test is aimed at a key function, through the study of the pressure measurement of the cluster size, you can see the interface of each cluster capacity. This test provides you as reference, if there are any deficiency or deviation, please correct me! If you have any other requirements on the performance, can you give us the issue.

**Examples:**

Example 1 (unknown):
```unknown
/opt/taobao/java/bin/java -server -Xms4g -Xmx4g -Xmn2g 
-XX:MetaspaceSize=128m 
-XX:MaxMetaspaceSize=320m 
-Xdebug 
-Xrunjdwp:transport=dt_socket,address=9555,server=y,suspend=n 
-XX:+UseConcMarkSweepGC 
-XX:+UseCMSCompactAtFullCollection 
-XX:CMSInitiatingOccupancyFraction=70 
-XX:+CMSParallelRemarkEnabled -XX:SoftRefLRUPolicyMSPerMB=0 
-XX:+CMSClassUnloadingEnabled -XX:SurvivorRatio=8 
-XX:-UseParNewGC -verbose:gc -Xloggc:/home/admin/nacos/logs/nacos_gc.log 
-XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCApplicationStoppedTime 
-XX:+PrintAdaptiveSizePolicy -Dnacos.home=/home/admin/nacos -XX:-OmitStackTraceInFastThrow 
-XX:-UseLargePages -jar /home/admin/nacos/target/nacos-server.jar 
--spring.config.location=classpath:/,classpath:/config/,file:./,file:./config/,file:/home/admin/nacos/conf/
```

---

## Nacos Spring

**URL:** https://nacos.io/en-us/docs/nacos-spring.html

**Contents:**
- Nacos Spring
- 1. Annotation-Driven
  - 1.1. Enable Nacos
  - 1.2. Configure Change Listener method
    - 1.2.1. Type Conversion
    - 1.2.2. Timeout of Execution
  - 1.3. Global and Special Nacos Properties
  - 1.4. @NacosProperties
- 2. Dependency Injection
- 3. Externalized Configuration

This section provides a detailed description of the key features of nacos-spring-context:

@EnableNacos is a modular-driven annotation that enables all features of Nacos Spring, including Service Discovery and Distributed Configuration. It equals to @EnableNacosDiscovery and @EnableNacosConfig, which can be configured separately and used in different scenarios.

Suppose there was a config in Nacos Server whose dataId is "testDataId" and groupId is default group("DEFAULT_GROUP"). Now you would like to change its content by using the ConfigService#publishConfig method:

Then you would like to add a listener, which will be listening for the config changes. You can do this by adding a config change listener method into your Spring Beans:

The code below has the same effect:

Note: @NacosConfigListener supports richer type conversions.

The type conversion of @NacosConfigListener includes both build-in and customized implementations. By default, build-in type conversion is based on Spring DefaultFormattingConversionService, which means it covers most of the general cases as well as the rich features of the higher Spring framework.

For example, the content "9527" in the preceding example can also be listened by a method with integer or the Integer argument:

Of course, nacos-spring-context provides elastic extension for developers. If you define a named nacosConfigConversionService Spring Bean whose type is ConversionService , the DefaultFormattingConversionService will be ignored. In addition, you can customize the implementation of the NacosConfigConverter interface to specify a listener method for type conversion:

The UserNacosConfigConverter class binds the @NacosConfigListener.converter() attribute:

As it might cost some time to run customized NacosConfigConverter, you can set max execution time in the @NacosConfigListener.timeout() attribute to prevent it from blocking other listeners:

The integerValue of Listeners Bean is always null and will not be changed. Therefore, those asserts will be true:

The globalProperties is a required attribute in any @EnableNacos, @EnableNacosDiscovery or @EnableNacosConfig, and its type is @NacosProperties. globalProperties initializes "Global Nacos Properties" that will be used by other annotations and components, e,g @NacosInjected. In other words, Global Nacos Properties" defines the global and default properties. It is set with the lowest priority and can be overridden if needed. The precedence of overiding rules is shown in the following table:

*.properties() defines special Nacos properties which come from one of the following:

Special Nacos properties are also configured by @NacosProperties. However, they are optional and are used to override Global Nacos Properties in special scenarios. If not defined, the Nacos Properties will try to retrieve properities from @EnableNacosConfig.globalProperties() or @EnableNacosDiscovery.globalProperties(), or @EnableNacos.globalProperties().

@NacosProperties is a uniform annotation for global and special Nacos properties. It serves as a mediator between Java Properties and NacosFactory class. NacosFactory is responsible for creating ConfigService or NamingService instances.

The attributes of @NacosProperties completely support placeholders whose source is all kinds of PropertySource in Spring Environment abstraction, typically Java System Properties and OS environment variables. The prefix of all placeholders are nacos.. The mapping between the attributes of @NacosProperties and Nacos properties are shown below:

Note that there are some differences in the placeholders of globalProperties() between @EnableNacosDiscovery and @EnableNacosConfig:

These placeholders of @EnableNacosDiscovery and @EnableNacosConfig are designed to isolate different Nacos servers, and are unnecessary in most scenarios. By default, general placeholders will be reused.

@NacosInjected is a core annotation which is used to inject ConfigService or NamingService instance in your Spring Beans and make these instances cacheable. This means the instances will be the same if their @NacosProperties are equal, regargless of whether the properties come from global or special Nacos properties:

The property configService uses @EnableNacos#globalProperties() or @EnableNacosConfig#globalProperties(), and because the default value of the encode attribute is "UTF-8", therefore the configService instance and the configService2 instance which is annotated by @NacosProperties(encode = "UTF-8") are the same. The same is true for namingService and namingService2.

More importantly, unlike the ConfigService instances created by the NacosFactory.createConfigService() method, the ConfigService instances created by the @NacosInjected annotation support Nacos Spring events. For instance, there will be an NacosConfigPublishedEvent after an enhanced ConfigService invokes the publishConfig() method. Refer to the Event/Listener Driven section for more details.

Externalized configuration is a concept introduced by Spring Boot, which allows applications to receive external property sources to control runtime behavior. Nacos Server runs an isolation process outside the application to maintain the application configurations. nacos-spring-context provides properties features including object binding, dynamic configuration(auto-refreshed) and so on, and dependence on Spring Boot or Spring Cloud framework is required.

Here is a simple comparison between nacos-spring-context and Spring stack:

See Auto-Refreshed Sample of @NacosConfigurationProperties

See Sample of @NacosPropertySources and @NacosPropertySource

Nacos Event/Listener Driven is based on the standard Spring Event/Listener mechanism. The ApplicationEvent of Spring is an abstract super class for all Nacos Spring events:

**Examples:**

Example 1 (java):
```java
@NacosInjected
private ConfigService configService;

@Test
public void testPublishConfig() throws NacosException {
    configService.publishConfig(DATA_ID, DEFAULT_GROUP, "9527");
}
```

Example 2 (java):
```java
@NacosConfigListener(dataId = DATA_ID)
public void onMessage(String config) {
    assertEquals("mercyblitz", config); // asserts true
}
```

Example 3 (java):
```java
configService.addListener(DATA_ID, DEFAULT_GROUP, new AbstractListener() {
    @Override
    public void receiveConfigInfo(String config) {
        assertEquals("9527", config); // asserts true
    }
});
```

Example 4 (java):
```java
@NacosConfigListener(dataId = DATA_ID)
public void onInteger(Integer value) {
    assertEquals(Integer.valueOf(9527), value); // asserts true
}

@NacosConfigListener(dataId = DATA_ID)
public void onInt(int value) {
    assertEquals(9527, value); // asserts true
}
```

---

## Nacos system parameters introduce

**URL:** https://nacos.io/en-us/docs/system-configurations.html

**Contents:**
- Nacos system parameters introduce
- Nacos Server
  - Global parameters
  - Naming module
  - Config module
  - CMDB module
- Nacos Java Client
  - General parameters
  - Naming client
  - Config client

For Server side, usually set in {nacos.home}/conf/application.properties, if the parameter name after mark (-D), says is the JVM parameter, need in {nacos.home}/bin/startup.sh accordingly set up. Such as setting nacos. The value of the home, can be in {nacos.home}/bin/startup.sh the following Settings:

In addition to the above listed to in application.propertiesconfiguration properties, And some can be adjusted call interface at runtime, These parameters are in the Open APIexamine system current data indexthe API in a statement.

Now the db config support multi data source. It can set data source num by db.num, and db.url.index as the corresponding connection's url. When db.user and db.password are set without index, all db connection use db.user and db.password to auth. If the username or password is different with different data source, can split by symbol ,, or use db.user.index,db.user.password to set corresponding db connection's username or password. It is important to note that, when db.user or db.password are set without index, and the mechanism which split db.user,db.password by , exist, so if username or password contains ,, it will split the value by ,, and use split[0] to auth, failed to auth finally.

Nacos started to use HikariCP connection pool from version 1.3, but before version 1.4.1, the connection pool configuration is system default value, and the configuration could not be customized. After 1.4.1, Nacos provide a method to configure the HikariCP connection pool. db.pool.config is the configuration prefix, xxx is the actual hikariCP configuration, such as db.pool.config.connectionTimeout or db.pool.config.maximumPoolSize and so on. For more configuration of hikariCP, please check HikariCP It should be noted that url, user, password will be rewrite by db.url.n, db.user, db.password, and driverClassName is the default MySQL8 driver which supports mysql5.x.

Client parameters are divided into two kinds, one kind is through the -D parameter to specify the configuration of the client is a kind of structure, through Properties objects specified in the configuration, the following without -D marked by Properties injection configuration.

**Examples:**

Example 1 (unknown):
```unknown
JAVA_OPT="${JAVA_OPT} -Dnacos.home=${BASE_DIR}"
```

---

## Open API Guide

**URL:** https://nacos.io/en-us/docs/open-api.html

**Contents:**
- Open API Guide
- Configuration Management
- Get configurations
  - Description
  - Request type
  - Request URL
  - Request parameters
  - Return parameters
  - Error codes
  - Example

Configuration Management

This API is used to get configurations in Nacos.

This API is used to listen for configurations in Nacos to capture configuration changes. In case of any configuration changes, you can use the Get Configurations API to obtain the latest value of the configuration and dynamically refresh the local cache.

A listener is registered using an asynchronous servlet. The nature of registering a listener is to compare the configuration value and the MD5 value of it with that of the backend. If the values differ, the inconsistent configuration is returned immediately. Otherwise, an empty string is returned after 30 seconds.

/nacos/v1/cs/configs/listener

It publishes configurations in Nacos.

It deletes configurations in Nacos.

Query list of history configuration.

Query the history details of the configuration

Note: From version 2.0.3, this interface need add three parameter, include tenant, dataId and group, tenant can not be provided.

Query the previous version of the configuration.(Since 1.4.0)

/nacos/v1/cs/history/previous

Note: From version 2.0.3, this interface need add three parameter, include tenant, dataId and group, tenant can not be provided.

Register an instance to service.

Delete instance from service.

Modify an instance of service.

Attension：After Nacos2.0 version, the metadata updated through this interface has a higher priority and has the ability to remember. After the instance removed, it will still exist for a period of time. If the instance is re-registered during this period, the metadata will still be Effective. You can modify the memory time through nacos.naming.clean.expired-metadata.expired-time and nacos.naming.clean.expired-metadata.interval

Query instance list of service.

Query instance details of service.

Delete a service, only permitted when instance count is 0.

Query system switches

Query the leader of current cluster

Update instance health status, only works when the cluster health checker is set to NONE.

Batch update instance metadata(Since 1.4)

Note: This API is a Beta API, later versions maybe modify or even delete. Please use it with caution.

Batch delete instance metadata(Since 1.4)

Note: This API is a Beta API, later versions maybe modify or even delete. Please use it with caution.

This API is used to get namespaces in Nacos.

It deletes namespace in Nacos.

**Examples:**

Example 1 (unknown):
```unknown
curl -X GET 'http://127.0.0.1:8848/nacos/v1/cs/configs?dataId=nacos.example&group=com.alibaba.nacos'
```

Example 2 (unknown):
```unknown
contentTest
```

Example 3 (unknown):
```unknown
http://serverIp:8848/nacos/v1/cs/configs/listener

POST request body data:

Listening-Configs=dataId%02group%02contentMD5%02tenant%01
```

Example 4 (unknown):
```unknown
In case of any configuration changes,

dataId%02group%02tenant%01

Otherwise, an empty string is returned.
```

---

## 

**URL:** https://nacos.io/en-us/docs/management-api.html

IN PLAN with Nacos 1.x.x

---
