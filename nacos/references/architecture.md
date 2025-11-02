# Nacos - Architecture

**Pages:** 1

---

## Nacos architecture

**URL:** https://nacos.io/en-us/docs/architecture.html

**Contents:**
- Nacos architecture
- Basic Architecture and Concepts
  - Service
  - Service Registry
  - Service Metadata
  - Service Provider
  - Service Consumer
  - Configuration
  - Configuration Management
  - Naming Service

A software function or a set of software functions (such as the retrieval of specified information or the execution of a set of operations) with the purpose that different clients can be reused for different purposes (for example, through a cross-process network call). Nacos supports almost all types of services: Kubernetes Service

gRPC | Dubbo RPC Service

Spring Cloud RESTful Service

The database of services, instances and metadata. Service instances are registered with the service registry on startup and deregistered on shutdown. Clients of the service and/or routers query the service registry to find the available instances of a service. A service registry might invoke a service instances health check API to verify that it is able to handle requests.

Data describing services such as service endpoints, service labels, service version, service instance weights, routing rules, security policies.

A process or application which provides reusable and callable services.

A process or application which initiates a call to a service.

During system development, developers usually extract some parameters or variables that need to be changed from the code and manage them in a separate configuration file. This enables the static system artifacts or deliverables (such as WAR and JAR packages) to fit with the physical operating environment in a better way. Configuration management is generally a part of system deployment, which is executed by the administrator or operation and maintenance personnel. Configuration modification is an effective method to adjust the behavior of a running system.

In the data center, all configuration-related activities such as editing, storage, distribution, change management, history version management, and change audit are collectively referred to as configuration management.

Mapping the "names" of all the objects and entities in the distributed system to the associated metadata, for example, ServiceName -> Endpoints\Version etc..., Distributed Lock Name -> Lock Owner/Status Info, DNS Domain Name -> IP List. Service discovery and DNS are the two major scenarios of naming service.

Providing dynamic configuration, service metadata and configuration management for other services or application.

The Nacos data model Key is uniquely determined by the triplet. The Namespace defaults to an empty string, the public namespace (public), and the group defaults to DEFAULT_GROUP.

Around the configuration, there are mainly two associated entities, one is the configuration change history, and the other is the service tag (used for marking classification, convenient for indexing), which is associated by ID.

// TODO Service part to be continued

Nacos supports both standard Docker images (v0.2.0) and nacos-.zip(tar.gz). You can choose the appropriate build to deploy the Nacos service according to your needs.

Nacos supports two start modes. you can merging the Service Registry and the Config Center in one process or deploying them in separately cluster.

In addition to deploying and launching Nacos services by users themselves, Nacos also supports public cloud. Nacos public cloud service will be free in Alibaba Cloud's commercial service (such as ACM, EDAS). We also welcome other public cloud providers to offer Nacos public cloud services.

---
