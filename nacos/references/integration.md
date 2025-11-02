# Nacos - Integration

**Pages:** 2

---

## NacosSync introduce

**URL:** https://nacos.io/en-us/docs/nacos-sync.html

**Contents:**
- NacosSync introduce
- Introduce
- System module architecture:
  - Synchronization task management page
  - Registry management page
- Usage scenarios:

The consoleProvides concise Web console operation, support for internationalization.

---

## Nacos with Dubbo fusion become registry

**URL:** https://nacos.io/en-us/docs/use-nacos-with-dubbo.html

**Contents:**
- Nacos with Dubbo fusion become registry
- Preparatory work
- Quick Start
  - Increasing Maven dependency
  - Configuration registry
  - Dubbo Spring externalized configuration
  - Spring XML configuration files
- Complete sample
  - Sample interface and implementation
  - Spring annotations driver sample

Nacos as Dubbo ecosystems important registry implementation, including dubbo-registry-nacos is Dubbo fusion Nacos registry implementation.

When you put dubbo-registry-nacos integrated into your dubbo project before, please make sure the background nacos service has started. If you are still not familiar with the basic use of Nacos, reference Quick Start for Nacos.

Nacos Dubbo fusion become registry procedure is very simple, general steps can be divided into "increasing Maven dependency" and "the registry".

First, you need to dubbo-registry-nacosMaven dependent on added to your project pom.xml file, and strongly recommend that you use the dubbo 2.6.5:

When a project to adddubbo-registry-nacos, you don't need to explicitly logic programming to realize service discovery and registration, actual implementation is provided by the third party and then configure Naocs registry.

Suppose you Dubbo application using the Spring Framework assembly, there will be two kinds of optional configuration method, respectively: Dubbo Spring externalized configuration, and the Spring XML configuration files, and, I strongly recommend the former.

Dubbo Spring externalized configuration consists of Dubbo 2.5.8 introduced new features, through the Spring Environment attribute automatically generate and bind the Dubbo configuration Bean, implement configuration to simplify, and lower the threshold of service development.

Suppose you Dubbo applications using Nacos as registry, and the server IP address is:10.20.153.10 at the same time, the registered address as Dubbo externalized configuration properties are stored in dubbo-config.properties file, as shown below:

Then, restart your application Dubbo, Dubbo information services and consumption in Nacos console can show:

As shown, the service name prefix for providers: metainfo for the service provider's information, consumers: represents the service consumer metainfo. Click"details" can check the service status details:

If you are using a Spring XML configuration file assembly Dubbo registry, please refer to the next section.

Similarly, suppose you Dubbo applications using Nacos as registry, and the server IP address is:10.20.153.10, and assembling Spring Bean in the XML file, as shown below:

After restart the Dubbo application, you can also find the provider and consumer registered metainfo is presented in Nacos console:

Whether you absolute configuration or switch Nacos registry super Easy? If you are still wanting more or less understand, may refer to the following the complete example.

Above pictures of metadata from Dubbo Spring annotations driver sample and Dubbo Spring XML configuration driven example, the following will introduce both, you can choose your preference programming model.Before the formal discussion, first to introduce the preparation work, because they are dependent on the Java service interface and implementation.At the same time, please make sure that the local (127.0.0.1) environment has launched Nacos service.

First define the sample interface, as shown below:

Provide the above interface implementation class:

Interface and implementation after ready, the following will be driven by annotations and XML configuration driven their implementation.

https://github.com/nacos-group/nacos-examples/tree/master/nacos-dubbo-example

Dubbo 2.5.7 reconstructed the Spring annotations driver programming model.

The annotation @EnableDubbo activation Dubbo annotation driven and externalized configuration, its scanBasePackages properties scanning to specify the Java package, all marked @Service Service interface implementation class exposure for Spring Bean, then be exported Dubbo Service.

@PropertySource is Spring Framework 3.1 introduced the standard import properties annotation configuration resources, it will provide Dubbo externalized configuration.

Similarly, dubbo.registry.address attribute points to Nacos registry, other dubbo service relevant meta information through Nacos registry access.

Similarly, @EnableDubbo annotations to activate Dubbo annotation driven and externalized configuration, but the current belong to the Service consumers, without having to specify the Java package name scan label @Service Service implementation.

@Reference is Dubbo remote service dependency injection annotations, need service providers and consumers agreed interface (interface), version (version) and group (group) information.Example, in the current service consumption DemoService service version from the configuration properties file consumer-config.properties.

@PostConstruct code shows when DemoServiceConsumerBootstrap Bean initialization, execution Dubbo ten times remote method invocation.

Twice in the local boot DemoServiceProviderBootstrap, the registry will appear two health services:

Run again DemoServiceConsumerBootstrap, run results as follows:

Operate, and service consumer using the load balancing strategy, RPC calls ten times the average contribution to two Dubbo provider instance.

The Spring XML configuration driven programming model is a traditional Spring assembly components.

Similarly, to start the first two DemoServiceProviderXmlBootstrap bootstrap class, observe Nacos registry service provider changes:

XML configuration driven service version for 2.0.0, therefore the registration service and correct.

Again run service consumers leading class DemoServiceConsumerXmlBootstrap, watch the console output:

Results also runs and load balancing is normal, but because the current sample has yet to add attributes demo.service.name of therefore, "name" part of the information output null.

If your attention or love Dubbo and Nacos open source project, as well as for their points of "star", related links:

**Examples:**

Example 1 (xml):
```xml
<dependencies>

    ...
    
    <!-- Dubbo dependency -->
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>dubbo</artifactId>
        <version>3.0.5</version>
    </dependency>

    <!-- Dubbo Nacos registry dependency -->
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>dubbo-registry-nacos</artifactId>
        <version>3.0.5</version>
    </dependency>

    <!-- Alibaba Spring Context extension -->
    <dependency>
        <groupId>com.alibaba.spring</groupId>
        <artifactId>spring-context-support</artifactId>
        <version>1.0.11</version>
    </dependency>

    ...
    
</dependencies>
```

Example 2 (properties):
```properties
## application
dubbo.application.name = your-dubbo-application

## Nacos registry address
dubbo.registry.address = nacos://10.20.153.10:8848
##If you want to use your own namespace, you can use the following two methods:
#dubbo.registry.address = nacos://10.20.153.10:8848?namespace=5cbb70a5-xxx-xxx-xxx-d43479ae0932
#dubbo.registry.parameters.namespace=5cbb70a5-xxx-xxx-xxx-d43479ae0932
...
```

Example 3 (xml):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:dubbo="http://dubbo.apache.org/schema/dubbo"
    xsi:schemaLocation="http://www.springframework.org/schema/beans        http://www.springframework.org/schema/beans/spring-beans-4.3.xsd        http://dubbo.apache.org/schema/dubbo        http://dubbo.apache.org/schema/dubbo/dubbo.xsd">
 
    <!-- 提供方应用信息，用于计算依赖关系 -->
    <dubbo:application name="dubbo-provider-xml-demo"  />
 
    <!-- 使用 Nacos 注册中心 -->
    <dubbo:registry address="nacos://10.20.153.10:8848" />
     <!-- If you want to use your own namespace, you can use the following configuration -->
    <!-- <dubbo:registry address="nacos://10.20.153.10:8848?namespace=5cbb70a5-xxx-xxx-xxx-d43479ae0932" /> -->
 	...
</beans>
```

Example 4 (java):
```java
package com.alibaba.nacos.example.dubbo.service;

public interface DemoService {
    String sayName(String name);
}
```

---
