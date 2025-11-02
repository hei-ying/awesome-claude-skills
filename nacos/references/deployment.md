# Nacos - Deployment

**Pages:** 1

---

## Kubernetes Nacos

**URL:** https://nacos.io/en-us/docs/use-nacos-with-kubernetes.html

**Contents:**
- Kubernetes Nacos
- Quick Start
- Advanced
- Deploy NFS
- Deploy database
- Deploy Nacos
- Scale Testing
- Prerequisites
- Limitations
- Project directory

This project contains a Nacos Docker image meant to facilitate the deployment of Nacos on Kubernetes via StatefulSets.

If you want to start Nacos without NFS, but emptyDirs will possibly result in a loss of data. as follows:

In advanced use, the cluster is automatically scaled and data is persisted, but PersistentVolumeClaims must be deployed. In this example, NFS is used.

If your K8S namespace is not default, execute the following script before creating RBAC

The StatefulSet controller provides each Pod with a unique hostname based on its ordinal index. The hostnames take the form of <statefulset name>-<ordinal index>. Because the replicas field of the nacos StatefulSet is set to 2, In the cluster file only two nacos address

You can find that the new node has joined the cluster

**Examples:**

Example 1 (shell):
```shell
git clone https://github.com/nacos-group/nacos-k8s.git
```

Example 2 (shell):
```shell
cd nacos-k8s
chmod +x quick-startup.sh
./quick-startup.sh
```

Example 3 (powershell):
```powershell
curl -X POST 'http://cluster-ip:8848/nacos/v1/ns/instance?serviceName=nacos.naming.serviceName&ip=20.18.7.10&port=8080'
```

Example 4 (powershell):
```powershell
curl -X GET 'http://cluster-ip:8848/nacos/v1/ns/instance/list?serviceName=nacos.naming.serviceName'
```

---
