# Liteflow - Configuration

**Pages:** 25

---

## 📜Apollo配置源

**URL:** https://liteflow.cc/pages/bea809/

**Contents:**
- 📜Apollo配置源
- # 依赖
- # 配置
- # 配置说明
- # 存储数据说明
- # 自动刷新
- # 脚本key的语言配置
- # 规则的启用关闭和脚本启用关闭v2.12.0+

LiteFlow原生支持了Apollo配置中心。你可以在配置中心里配置你的链路和脚本。

如果使用Apollo作为规则配置源，你需要添加以下额外插件依赖：

依赖了插件包之后，你无需再配置liteflow.ruleSource路径。

由于在Apollo中，推荐的做法是把连接信息和环境信息放到服务器的appdatas下的server.properties 文件中的。所以在LiteFlow的配置文件中是不指定连接信息的。这点要注意下。

对于规则来说，你在Apollo中需要为规则单独创建一个Namespace，数据类型选择properties，那么这个Namespace 下的每一对kv都是一个规则

key的格式为：规则ID[:是否启用]，其中方括号内的为可选项，value为单纯的EL（THEN(a,b,c)）

假设你的规则命名空间为:chainConfig，那么配置形式样例如下：

对于脚本命名空间来说，节点的key有固定格式：脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，其中方括号内的为可选项。 value为脚本数据。

假设你的脚本命名空间为：scriptConfig，那么配置形式样例如下：

Apollo支持推送配置数据的变更，凡是在Apollo里的规则和脚本变动，会自动推送到业务系统，进行实时的平滑热刷新，你无需做任何事情。

如果你只依赖了一种脚本语言插件包，那么语言这项是不需要配置的。会自动识别的。如果你配置了多语言脚本，那么脚本语言这一项，是必须要写的。

比如s1:boolean_script:布尔脚本s1:js。

关于脚本的多语言共存，请参考多脚本语言混合共存这一章。

LiteFlow也支持在Etcd节点上保留数据的同时关闭和启动规则/脚本。

之前说到规则的key的固定格式为规则ID[:是否启用]，如果配置chain1:false，那么这个规则就是关闭状态。相当于逻辑删除。

当然如果你只是配置key为chain1，那么等价于chain1:true。

对于脚本key来说，固定格式为脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，如果配置s1:script:脚本s1:groovy:false，那么这个脚本就是关闭状态，相当于逻辑删除。

如果不配置最后一项，比如s1:script:脚本s1:groovy，那么等价于s1:script:脚本s1:groovy:true。

对于规则key或者脚本key来说，一定要以冒号为分隔符对应好位置，如果你想配置是否启动，那么是在第5项，前面4项就必须要写，如果你写成s1:script:脚本s1:false那将会报错。

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-rule-apollo</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (yaml):
```yaml
liteflow:
  rule-source-ext-data-map:
    chainNamespace: chainConfig
    scriptNamespace: scriptConfig
```

Example 3 (properties):
```properties
liteflow.rule-source-ext-data={\
    "chainNamespace":"chainConfig",\
    "scriptNamespace":"scriptConfig"\
}
```

Example 4 (unknown):
```unknown
// Make sure to add code blocks to your code group
```

---

## 🗄Etcd配置源

**URL:** https://liteflow.cc/pages/4bfac2/

**Contents:**
- 🗄Etcd配置源
- # 依赖
- # 配置
- # 配置说明
- # 存储数据说明
- # 自动刷新
- # 脚本key的语言配置
- # 规则的启用关闭和脚本启用关闭v2.12.0+
- # 小例子

LiteFlow原生支持了Etcd的规则配置源。

如果使用Etcd作为规则配置源，你需要添加以下额外插件依赖：

依赖了插件包之后，你无需再配置liteflow.ruleSource路径。

在Etcd中，假设你的chainPath为：/liteflow/chain

那么这个路径下的每一个节点就是一个规则，节点的key的格式为：规则ID[:是否启用]，其中方括号内的为可选项，value为单纯的EL（THEN(a,b,c)），比如：

对于脚本path来说，假设你的scriptPath为：/liteflow/script

那么这个路径下的每一个节点都是一个脚本组件，节点的key有固定格式：脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，其中方括号内的为可选项。 value为脚本数据，比如：

---s2:boolean_script:布尔脚本组件s2

关于脚本类型，可以参照脚本语言介绍这一章节。

使用了此Etcd配置源插件，凡是Etcd节点里面的规则改动，会自动推送到业务系统，进行实时的平滑热刷新。你无需做任何事情。

如果你只依赖了一种脚本语言插件包，那么语言这项是不需要配置的。会自动识别的。如果你配置了多语言脚本，那么脚本语言这一项，是必须要写的。

比如s1:boolean_script:布尔脚本s1:js。

关于脚本的多语言共存，请参考多脚本语言混合共存这一章。

LiteFlow也支持在Etcd节点上保留数据的同时关闭和启动规则/脚本。

之前说到规则的key的固定格式为规则ID[:是否启用]，如果配置chain1:false，那么这个规则就是关闭状态。相当于逻辑删除。

当然如果你只是配置key为chain1，那么等价于chain1:true。

对于脚本key来说，固定格式为脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，如果配置s1:script:脚本s1:groovy:false，那么这个脚本就是关闭状态，相当于逻辑删除。

如果不配置最后一项，比如s1:script:脚本s1:groovy，那么等价于s1:script:脚本s1:groovy:true。

对于规则key或者脚本key来说，一定要以冒号为分隔符对应好位置，如果你想配置是否启动，那么是在第5项，前面4项就必须要写，如果你写成s1:script:脚本s1:false那将会报错。

为了让大家能简单上手Etcd规则文件的配置和运行，这里有一个小demo，大家可以拉到本地来运行，需要你替换Etcd的配置信息。

运行项目前，先读项目里的readme.txt文件。

https://github.com/bryan31/liteflow-ext-rule-demo

← 📋Nacos配置源 📜Apollo配置源→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-rule-etcd</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (yaml):
```yaml
liteflow:
  rule-source-ext-data-map:
    endpoints: http://127.0.0.1:2379
    chainPath: /liteflow/chain
    scriptPath: /liteflow/script
```

Example 3 (properties):
```properties
liteflow.rule-source-ext-data={\
    "endpoints":"http://127.0.0.1:2379",\
    "chainPath":"/liteflow/chain",\
    "scriptPath":"/liteflow/script"\
}
```

Example 4 (unknown):
```unknown
// Make sure to add code blocks to your code group
```

---

## 📋Nacos配置源

**URL:** https://liteflow.cc/pages/09b776/

**Contents:**
- 📋Nacos配置源
- # 依赖
- # 配置
- # 对阿里云MSE的支持v2.11.4+
- # 配置说明
- # 存储数据说明
- # 自动刷新
- # 小例子

LiteFlow原生支持了Nacos的规则配置源。

如果使用Nacos作为规则配置源，你需要添加以下额外插件依赖：

依赖了插件包之后，你无需再配置liteflow.ruleSource路径。

自从v2.11.4开始，LiteFlow对阿里云的MSE也进行了支持，配置如下:

需要说明的是，使用Nacos配置源的时候，Nacos里存的只能是xml形式的配置。并且所有的配置都必须存在一个dataId里。不可以分几个dataId。

使用了此Nacos配置源插件，凡是Nacos节点里面的规则改动，会自动推送到业务系统，进行实时的平滑热刷新。你无需做任何事情。

为了让大家能简单上手Nacos规则文件的配置和运行，这里有一个小demo，大家可以拉到本地来运行，需要你替换Nacos的配置信息。

运行项目前，先读项目里的readme.txt文件。

https://github.com/bryan31/liteflow-ext-rule-demo

← 📗ZK规则文件配置源 🗄Etcd配置源→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-rule-nacos</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (yaml):
```yaml
liteflow:
  rule-source-ext-data-map:
    serverAddr: 127.0.0.1:8848
    dataId: demo_rule
    group: DEFAULT_GROUP
    namespace: your namespace id
    username: nacos
    password: nacos
```

Example 3 (properties):
```properties
liteflow.rule-source-ext-data={\
    "serverAddr":"127.0.0.1:8848",\
    "dataId":"demo_rule",\
    "group":"DEFAULT_GROUP",\
    "namespace":"your namespace id",\
    "username":"nacos",\
    "password":"nacos"\
}
```

Example 4 (unknown):
```unknown
// Make sure to add code blocks to your code group
```

---

## 🍩Solon下的配置项

**URL:** https://liteflow.cc/pages/43178b/

**Contents:**
- 🍩Solon下的配置项

Solon下的配置项同Springboot下的配置项。

← 🌱Spring下的配置项 🌵其他场景代码设置配置项→

---

## 🍩Solon场景安装运行

**URL:** https://liteflow.cc/pages/9c2371/

**Contents:**
- 🍩Solon场景安装运行
- # 依赖
- # 组件的定义
- # 配置文件
- # 规则文件的定义
- # 执行

对于使用solon框架用户。LiteFlow也提供了依赖：

为稳定版本，目前jar包已上传中央仓库，可以直接依赖到

在依赖了以上jar包后，你需要定义并实现一些组件，这里需要注意的是@Component注解应为Solon框架提供的：

import org.noear.solon.annotation.Component;

然后，需要定义application.properties或者application.yml里添加配置(这里以properties为例，yaml也是一样的)

更多配置项请参考Solon下的配置项章节。

同时，你得在resources下的config/flow.xml中定义规则：

然后你就可以在任意被Solon托管的类中拿到flowExecutor，进行执行链路：

这个DefaultContext是默认的上下文，用户可以用最自己的任意Bean当做上下文传入，如果需要传入自己的上下文，则需要传用户Bean的Class属性，具体请看数据上下文这一章节。

← 🌱Spring场景安装运行 🌵其他场景安装运行→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-solon-plugin</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (java):
```java
@Component("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

Example 3 (java):
```java
@Component("b")
public class BCmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

Example 4 (java):
```java
@Component("c")
public class CCmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

---

## 🌿Springboot下的配置项

**URL:** https://liteflow.cc/pages/4594ec/

**Contents:**
- 🌿Springboot下的配置项

只要使用了规则，那么rule-source必须得有。

但是如果你是用代码动态构造规则，那么rule-source配置自动失效。因为代码构造是用代码来装配规则，不需要规则文件。详情请参考用代码动态构造规则。

**Examples:**

Example 1 (properties):
```properties
#规则文件路径
liteflow.rule-source=config/flow.xml
#-----------------以下非必须-----------------
#liteflow是否开启，默认为true
liteflow.enable=true
#liteflow的banner打印是否开启，默认为true
liteflow.print-banner=true
#上下文的初始数量槽，默认值为1024，这个值不用刻意配置，这个值会自动扩容
liteflow.slot-size=1024
#FlowExecutor的execute2Future的线程数，默认为64
liteflow.main-executor-works=64
#FlowExecutor的execute2Future的自定义线程池Builder，LiteFlow提供了默认的Builder
liteflow.main-executor-class=com.yomahub.liteflow.thread.LiteFlowDefaultMainExecutorBuilder
#自定义请求ID的生成类，LiteFlow提供了默认的生成类
liteflow.request-id-generator-class=com.yomahub.liteflow.flow.id.DefaultRequestIdGenerator
#全局异步节点线程池大小，默认为64
liteflow.global-thread-pool-size=64
#全局异步节点线程池队列大小，默认为512
liteflow.global-thread-pool-queue-size=512
#全局异步节点线程池自定义Builder，LiteFlow提供了默认的线程池Builder
liteflow.global-thread-pool-executor-class=com.yomahub.liteflow.thread.LiteFlowDefaultGlobalExecutorBuilder
#异步线程最长的等待时间(只用于when)，默认值为15000
liteflow.when-max-wait-time=15000
#异步线程最长的等待时间(只用于when)，默认值为MILLISECONDS，毫秒
liteflow.when-max-wait-time-unit=MILLISECONDS
#每个WHEN是否用单独的线程池
liteflow.when-thread-pool-isolate=false
#设置解析模式，一共有三种模式，PARSE_ALL_ON_START | PARSE_ALL_ON_FIRST_EXEC | PARSE_ONE_ON_FIRST_EXEC
liteflow.parse-mode=PARSE_ALL_ON_START
#全局重试次数，默认为0
liteflow.retry-count=0
#是否支持不同类型的加载方式混用，默认为false
liteflow.support-multiple-type=false
#全局默认节点执行器
liteflow.node-executor-class=com.yomahub.liteflow.flow.executor.DefaultNodeExecutor
#是否打印执行中过程中的日志，默认为true
liteflow.print-execution-log=true
#是否开启本地文件监听，默认为false
liteflow.enable-monitor-file=false
#是否开启快速解析模式，默认为false
liteflow.fast-load=false
#是否开启Node节点实例ID持久化，默认为false
liteflow.enable-node-instance-id=false
#是否开启虚拟线程(只在JDK21+环境有效)，默认为true
liteflow.enable-virtual-thread=true
#监控是否开启，默认不开启
liteflow.monitor.enable-log=false
#监控队列存储大小，默认值为200
liteflow.monitor.queue-limit=200
#监控一开始延迟多少执行，默认值为300000毫秒，也就是5分钟
liteflow.monitor.delay=300000
#监控日志打印每过多少时间执行一次，默认值为300000毫秒，也就是5分钟
liteflow.monitor.period=300000
```

Example 2 (yaml):
```yaml
liteflow:
  #规则文件路径
  rule-source: config/flow.xml
  #-----------------以下非必须-----------------
  #liteflow是否开启，默认为true
  enable: true
  #liteflow的banner打印是否开启，默认为true
  print-banner: true
  #上下文的初始数量槽，默认值为1024，这个值不用刻意配置，这个值会自动扩容
  slot-size: 1024
  #FlowExecutor的execute2Future的线程数，默认为64
  main-executor-works: 64
  #FlowExecutor的execute2Future的自定义线程池Builder，LiteFlow提供了默认的Builder
  main-executor-class: com.yomahub.liteflow.thread.LiteFlowDefaultMainExecutorBuilder
  #自定义请求ID的生成类，LiteFlow提供了默认的生成类
  request-id-generator-class: com.yomahub.liteflow.flow.id.DefaultRequestIdGenerator
  #全局异步节点线程池大小，默认为64
  global-thread-pool-size: 64
  #全局异步节点线程池队列大小，默认为512
  global-thread-pool-queue-size: 512
  #全局异步节点线程池自定义Builder，LiteFlow提供了默认的线程池Builder
  global-thread-pool-executor-class: com.yomahub.liteflow.thread.LiteFlowDefaultGlobalExecutorBuilder
  #异步线程最长的等待时间(只用于when)，默认值为15000
  when-max-wait-time: 15000
  #异步线程最长的等待时间(只用于when)，默认值为MILLISECONDS，毫秒
  when-max-wait-time-unit: MILLISECONDS
  #每个WHEN是否用单独的线程池
  when-thread-pool-isolate: false
  #设置解析模式，一共有三种模式，PARSE_ALL_ON_START | PARSE_ALL_ON_FIRST_EXEC | PARSE_ONE_ON_FIRST_EXEC
  parse-mode: PARSE_ALL_ON_START
  #全局重试次数，默认为0
  retry-count: 0
  #是否支持不同类型的加载方式混用，默认为false
  support-multiple-type: false
  #全局默认节点执行器
  node-executor-class: com.yomahub.liteflow.flow.executor.DefaultNodeExecutor
  #是否打印执行中过程中的日志，默认为true
  print-execution-log: true
  #是否开启本地文件监听，默认为false
  enable-monitor-file: false
  #是否开启快速解析模式，默认为false
  fast-load: false
  #是否开启Node节点实例ID持久化，默认为false
  enable-node-instance-id: false
  #是否开启虚拟线程(只在JDK21+环境有效)，默认为true
  enable-virtual-thread: true
  #简易监控配置选项
  monitor:
    #监控是否开启，默认不开启
    enable-log: false
    #监控队列存储大小，默认值为200
    queue-limit: 200
    #监控一开始延迟多少执行，默认值为300000毫秒，也就是5分钟
    delay: 300000
    #监控日志打印每过多少时间执行一次，默认值为300000毫秒，也就是5分钟
    period: 300000
```

Example 3 (unknown):
```unknown
// Make sure to add code blocks to your code group
```

---

## 🌿Springboot场景安装运行

**URL:** https://liteflow.cc/pages/9bf6be/

**Contents:**
- 🌿Springboot场景安装运行
- # 依赖
- # 组件的定义
- # SpringBoot配置文件
- # 规则文件的定义
- # 执行

LiteFlow提供了liteflow-spring-boot-starter依赖包，提供自动装配功能

为稳定版本，目前jar包已上传中央仓库，可以直接依赖到

在依赖了以上jar包后，你需要定义并实现一些组件，确保SpringBoot会扫描到这些组件并注册进上下文。

然后，在你的SpringBoot的application.properties或者application.yml里添加配置(这里以properties为例，yaml也是一样的)

同时，你得在resources下的config/flow.xml中定义规则：

SpringBoot在启动时会自动装载规则文件。

然后你就可以在Springboot任意被Spring托管的类中拿到flowExecutor，进行执行链路：

这个DefaultContext是默认的上下文，用户可以用最自己的任意Bean当做上下文传入，如果需要传入自己的上下文，则需要传用户Bean的Class属性，具体请看数据上下文这一章节。

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-spring-boot-starter</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

Example 3 (java):
```java
@LiteflowComponent("b")
public class BCmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

Example 4 (java):
```java
@LiteflowComponent("c")
public class CCmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

---

## 🌱Spring下的配置项

**URL:** https://liteflow.cc/pages/33833a/

**Contents:**
- 🌱Spring下的配置项

只要使用了规则，那么rule-source必须得有。

但是如果你是用代码动态构造规则，那么rule-source配置自动失效。因为代码构造是用代码来装配规则，不需要规则文件。详情请参考用代码动态构造规则。

← 🌿Springboot下的配置项 🍩Solon下的配置项→

**Examples:**

Example 1 (xml):
```xml
<bean id="liteflowConfig" class="com.yomahub.liteflow.property.LiteflowConfig">
    <property name="ruleSource" value="config/flow.xml"/>
    <!-- ***********以下都不是必须的，都有默认值*********** -->
    <!-- liteflow是否开启,默认为true -->
    <property name="enable" value="true"/> 
    <!-- liteflow的banner是否开启，默认为true -->
    <property name="printBanner" value="true"/> 
    <!-- 上下文的初始数量槽，默认值为1024，这个值不用刻意配置，这个值会自动扩容 -->
    <property name="slotSize" value="1024"/> 
    <!-- FlowExecutor的execute2Future的线程数，默认为64 -->
    <property name="mainExecutorWorks" value="64"/> 
    <!-- FlowExecutor的execute2Future的自定义线程池Builder，LiteFlow提供了默认的Builder -->
    <property name="mainExecutorClass" value="com.yomahub.liteflow.thread.LiteFlowDefaultMainExecutorBuilder"/>
    <!-- 自定义请求ID的生成类，LiteFlow提供了默认的生成类 -->
    <property name="requestIdGeneratorClass" value="com.yomahub.liteflow.flow.id.DefaultRequestIdGenerator"/>
    <!-- 全局异步节点线程池大小，默认为64 -->
    <property name="globalThreadPoolSize" value="64"/>
    <!-- 全局异步节点线程池队列大小，默认为512 -->
    <property name="globalThreadPoolQueueSize" value="512"/>
    <!-- 全局异步节点线程池自定义Builder，LiteFlow提供了默认的线程池Builder -->
    <property name="globalThreadPoolExecutorClass" value="com.yomahub.liteflow.thread.LiteFlowDefaultGlobalExecutorBuilder"/>
    <!-- 异步线程最长的等待时间(只用于when)，默认值为15000 -->
    <property name="whenMaxWaitTime" value="15000"/>
    <!-- 异步线程最长的等待时间(只用于when)，默认值为MILLISECONDS，毫秒 -->
    <property name="whenMaxWaitTimeUnit" value="MILLISECONDS"/>
    <!-- 每个WHEN是否用单独的线程池 -->
    <property name="whenThreadPoolIsolate" value="false"/>
    <!-- 设置解析模式，一共有三种模式，PARSE_ALL_ON_START | PARSE_ALL_ON_FIRST_EXEC | PARSE_ONE_ON_FIRST_EXEC -->
    <property name="parseMode" value="PARSE_ALL_ON_START"/>
    <!-- 全局重试次数，默认为0 -->
    <property name="retryCount" value="0"/>
    <!-- 是否支持不同类型的加载方式混用，默认为false -->
    <property name="supportMultipleType" value="false"/>
    <!-- 全局默认节点执行器 -->
    <property name="nodeExecutorClass" value="com.yomahub.liteflow.flow.executor.DefaultNodeExecutor"/>
    <!-- 是否打印执行中过程中的日志，默认为true -->
    <property name="printExecutionLog" value="true"/>
    <!-- 是否开启本地文件监听，默认为false -->
    <property name="enableMonitorFile" value="false"/>
    <!-- 是否开启快速解析模式，默认为false -->
    <property name="fastLoad" value="false"/>
    <!-- 是否开启Node节点实例ID持久化，默认为false -->
    <property name="enableNodeInstanceId" value="false"/>
    <!-- #是否开启虚拟线程(只在JDK21+环境有效)，默认为true -->
    <property name="enableVirtualThread" value="true"/>
    <!-- 监控是否开启，默认不开启 -->
    <property name="enableLog" value="false"/>
    <!-- 监控队列存储大小，默认值为200 -->
    <property name="queueLimit" value="200"/>
    <!-- 监控一开始延迟多少执行，默认值为300000毫秒，也就是5分钟 -->
    <property name="period" value="300000"/>
    <!-- 监控日志打印每过多少时间执行一次，默认值为300000毫秒，也就是5分钟 -->
    <property name="delay" value="300000"/>
</bean>
```

---

## 🌱Spring场景安装运行

**URL:** https://liteflow.cc/pages/7b1eeb/

**Contents:**
- 🌱Spring场景安装运行
- # 依赖
- # 定义你的组件
- # Spring xml中的配置
- # 规则文件的定义
- # 执行

针对于使用了Spring但没有使用SpringBoot的项目

为稳定版本，目前jar包已上传中央仓库，可以直接依赖到

你需要定义并实现一些组件，确保Spring会扫描到这些组件并注册进上下文

同时，你得在resources的config/flow.xml中如下配置：

和SpringBoot的执行方式一样，没有任何区别，你可以在你的任何受Spring托管的类里注入FlowExecutor进行执行：

这个DefaultContext是默认的上下文，用户可以用最自己的任意Bean当做上下文传入，如果需要传入自己的上下文，则需要传用户Bean的Class属性，具体请看数据上下文这一章节。

← 🌿Springboot场景安装运行 🍩Solon场景安装运行→

**Examples:**

Example 1 (xml):
```xml
<dependency>
	<groupId>com.yomahub</groupId>
    <artifactId>liteflow-spring</artifactId>
	<version>2.15.1</version>
</dependency>
```

Example 2 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeComponent {

    @Override
    public void process() {
        //do your business
    }
}
```

Example 3 (java):
```java
@LiteflowComponent("b")
public class BCmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

Example 4 (java):
```java
@LiteflowComponent("c")
public class CCmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

---

## 📘SQL数据库配置源

**URL:** https://liteflow.cc/pages/236b4f/

**Contents:**
- 📘SQL数据库配置源
- # 依赖
- # 配置
- # 配置说明
- # 使用你项目中的dataSource来进行连接v2.10.6+
- # 轮询自动刷新v2.11.1+
- # 自定义规则/脚本表过滤SQLv2.12.4+
- # 支持决策路由v2.12.1+
- # 支持多数据源框架v2.13.0+
- # 小例子

LiteFlow原生支持了标准关系型结构化数据库的配置源，只要你的数据库兼容标准SQL语法，都可以支持。

⭐️SQL插件也是官网推荐的外置配置源插件 ⭐️

如果使用数据库作为规则配置源，你需要添加以下额外插件依赖：

依赖了插件包之后，你无需再配置liteflow.ruleSource路径。

LiteFlow并不约束你的表名和表结构，你只需要把表名和相关的字段名配置在参数里即可。

在数据库中，你至少需要一张表来存储编排规则，这是必须的。

如果你使用到了脚本，那么需要第二张表来存储脚本。

在规则表中，一行数据就是一个规则。在脚本表中，一行数据就是一个脚本组件。

LiteFlow支持了使用项目中已存在的Datasource来进行数据库连接。如果你项目中已有链接配置，比如：

那么你在rule-source-ext-data-map中无需再配置以下几项：

需要注意的是，如果你的系统中声明了多个数据源，那么LiteFlow会自动判断该选用哪个数据源。

如果你的系统中使用了动态数据源，那么请确保默认数据源是含有LiteFlow链路数据的表数据的。

LiteFlow支持SQL数据源轮询模式的自动刷新机制。你可以在配置项中通过pollingEnabled: true来开启自动刷新：

轮询模式的自动刷新根据预设的时间间隔定时拉取SQL中的数据，与本地保存的数据SHA值进行对比来判断是否需要更新数据。

定时轮询存在些微的性能消耗；受轮询间隔限制，数据更新有一定延迟性。

以上两个属性可以用来自定义你的过滤SQL。这里的配置的是完整的SQL。

配置了自定义过滤SQL，则会完全忽略applicationName和enable属性了，完全根据你的自定义SQL来去查询了，但是返回的字段还是要符合开发者配置的映射字段。

这个特性比较适合想自定义查询规则/脚本表的开发者，突破框架的applicationName和enable的限制。

只需要配置routeField和namespaceFiled字段，并在数据库对应的映射字段存入决策路由的表达式即可开启数据库对决策路由的支持。

LiteFlow支持了常用的两种多数据源框架，分别是：

Baomidou社区的dynamic-datasource和Shardingsphere社区的shardingsphere-jdbc。

为了让大家能简单上手SQL规则文件的配置和运行，这里有一个小demo，大家可以拉到本地来运行，需要你替换数据库的配置信息。

运行项目前，先读项目里的readme.txt文件。

https://github.com/bryan31/liteflow-ext-rule-demo

← 📕本地规则文件配置 📗ZK规则文件配置源→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-rule-sql</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (yaml):
```yaml
liteflow:
  rule-source-ext-data-map:
    url: jdbc:mysql://localhost:3306/poseidon
    driverClassName: com.mysql.cj.jdbc.Driver
    username: root
    password: 123456
    applicationName: demo
    #是否开启SQL日志
    sqlLogEnabled: true
    #是否开启SQL数据轮询自动刷新机制 默认不开启
    pollingEnabled: true
    pollingIntervalSeconds: 60
    pollingStartSeconds: 60
    #以下是chain表的配置，这个一定得有
    chainTableName: chain
    chainApplicationNameField: application_name
    chainNameField: chain_name
    elDataField: el_data
    #以下是决策路由字段的配置，如果你没用到决策路由，可以不配置
    routeField: route
    namespaceField: namespace
    #是否启用这条规则
    chainEnableField: enable
    #规则表自定义过滤SQL
    chainCustomSql: 这里设置自定义规则表SQL
    #以下是script表的配置，如果你没使用到脚本，下面可以不配置
    scriptTableName: script
    scriptApplicationNameField: application_name
    scriptIdField: script_id
    scriptNameField: script_name
    scriptDataField: script_data
    scriptTypeField: script_type
    scriptLanguageField: script_language
    #是否启用这条脚本
    scriptEnableField: enable
    #脚本表自定义过滤SQL
    scriptCustomSql: 这里设置自定义脚本表SQL
```

Example 3 (properties):
```properties
liteflow.rule-source-ext-data={\
  "url":"jdbc:mysql://localhost:3306/poseidon",\
  "driverClassName":"com.mysql.cj.jdbc.Driver",\
  "username":"root",\
  "password":"123456",\
  "applicationName": "demo",\
  "sqlLogEnabled": true,\
  "pollingEnabled": true,\
  "pollingIntervalSeconds": 60,\
  "pollingStartSeconds": 60,\
  "chainTableName": "chain",\
  "chainApplicationNameField": "application_name",\
  "chainNameField": "chain_name",\
  "elDataField": "el_data",\
  "routeField": "route",\
  "namespaceField": "namespace",\
  "chainEnableField": "enable",\
  "chainCustomSql": "这里设置自定义规则表SQL",\
  "scriptTableName": "script",\
  "scriptApplicationNameField": "application_name",\
  "scriptIdField": "script_id",\
  "scriptNameField": "script_name",\
  "scriptDataField": "script_data",\
  "scriptTypeField": "script_type",\
  "scriptLanguageField": "script_language",\
  "scriptEnableField": "enable",\
  "scriptCustomSql": "这里设置自定义脚本表SQL"
  }
```

Example 4 (unknown):
```unknown
// Make sure to add code blocks to your code group
```

---

## 📗ZK规则文件配置源

**URL:** https://liteflow.cc/pages/ffc345/

**Contents:**
- 📗ZK规则文件配置源
- # 依赖
- # 配置
- # 配置说明
- # 存储数据说明
- # 自动刷新
- # 脚本key的语言配置
- # 规则的启用关闭和脚本启用关闭v2.12.0+
- # 小例子

LiteFlow支持把配置放在zk集群中，基于zk的通知机制，LiteFlow支持实时修改流程

如果需要用到zk，需要添加以下额外依赖插件：

依赖了插件包之后，你无需再配置liteflow.ruleSource路径。

在ZK中，假设你的chainPath为：/liteflow/chain

那么这个路径下的每一个节点就是一个规则，节点的key的格式为：规则ID[:是否启用]，其中方括号内的为可选项，value为单纯的EL（THEN(a,b,c)），比如：

对于脚本path来说，假设你的scriptPath为：/liteflow/script

那么这个路径下的每一个节点都是一个脚本组件，节点的key有固定格式：脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，其中方括号内的为可选项。 value为脚本数据，比如：

---s2:boolean_script:布尔脚本组件s2

关于脚本类型，可以参照脚本语言介绍这一章节。

使用了此zk配置源插件，凡是zk节点里面的规则改动，会自动推送到业务系统，进行实时的平滑热刷新。你无需做任何事情。

如果你只依赖了一种脚本语言插件包，那么语言这项是不需要配置的。会自动识别的。如果你配置了多语言脚本，那么脚本语言这一项，是必须要写的。

比如s1:boolean_script:布尔脚本s1:js。

关于脚本的多语言共存，请参考多脚本语言混合共存这一章。

LiteFlow也支持在zk节点上保留数据的同时关闭和启动规则/脚本。

之前说到规则的key的固定格式为规则ID[:是否启用]，如果配置chain1:false，那么这个规则就是关闭状态。相当于逻辑删除。

当然如果你只是配置key为chain1，那么等价于chain1:true。

对于脚本key来说，固定格式为脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，如果配置s1:script:脚本s1:groovy:false，那么这个脚本就是关闭状态，相当于逻辑删除。

如果不配置最后一项，比如s1:script:脚本s1:groovy，那么等价于s1:script:脚本s1:groovy:true。

对于规则key或者脚本key来说，一定要以冒号为分隔符对应好位置，如果你想配置是否启动，那么是在第5项，前面4项就必须要写，如果你写成s1:script:脚本s1:false那将会报错。

为了让大家能简单上手ZK规则文件的配置和运行，这里有一个小demo，大家可以拉到本地来运行，需要你替换zk的配置信息。

运行项目前，先读项目里的readme.txt文件。

https://github.com/bryan31/liteflow-ext-rule-demo

← 📘SQL数据库配置源 📋Nacos配置源→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-rule-zk</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (yaml):
```yaml
liteflow:
  rule-source-ext-data-map:
    connectStr: 127.0.0.1:2181,127.0.0.1:2182,127.0.0.1:2183
    chainPath: /liteflow/chain
    #如果你没有脚本组件，以下可以不配置
    scriptPath: /liteflow/script
```

Example 3 (properties):
```properties
liteflow.rule-source-ext-data={\
    "connectStr":"127.0.0.1:2181,127.0.0.1:2182,127.0.0.1:2183",\
    "chainPath":"/liteflow/chain",\
    "scriptPath":"/liteflow/script"\
}
```

Example 4 (unknown):
```unknown
// Make sure to add code blocks to your code group
```

---

## 🌵其他场景代码设置配置项

**URL:** https://liteflow.cc/pages/b5065a/

**Contents:**
- 🌵其他场景代码设置配置项

只要使用了规则，那么rule-source必须得有。

但是如果你是用代码动态构造规则，那么rule-source配置自动失效。因为代码构造是用代码来装配规则，不需要规则文件。详情请参考用代码动态构造规则。

**Examples:**

Example 1 (java):
```java
LiteflowConfig config = new LiteflowConfig();
//规则文件路径
config.setRuleSource("config/flow.xml");
//-----------------以下非必须-----------------
//liteflow是否开启，默认为true
config.setEnable(true);
//liteflow的banner打印是否开启，默认为true
config.setPrintBanner(true);
//上下文的初始数量槽，默认值为1024，这个值不用刻意配置，这个值会自动扩容
config.setSlotSize(1024);
//FlowExecutor的execute2Future的线程数，默认为64
config.setMainExecutorWorks(64);
//FlowExecutor的execute2Future的自定义线程池Builder，LiteFlow提供了默认的Builder
config.setMainExecutorClass("com.yomahub.liteflow.thread.LiteFlowDefaultMainExecutorBuilder");
//自定义请求ID的生成类，LiteFlow提供了默认的生成类
config.setRequestIdGeneratorClass("com.yomahub.liteflow.flow.id.DefaultRequestIdGenerator");
//全局异步节点线程池大小，默认为64
config.setGlobalThreadPoolSize(64);
//全局异步节点线程池队列大小，默认为512
config.setGlobalThreadPoolQueueSize(512);
//全局异步节点线程池自定义Builder，LiteFlow提供了默认的线程池Builder
config.setGlobalThreadPoolExecutorClass("com.yomahub.liteflow.thread.LiteFlowDefaultGlobalExecutorBuilder");
//异步线程最长的等待时间(只用于when)，默认值为15000
config.setWhenMaxWaitTime(15000);
//异步线程最长的等待时间(只用于when)，默认值为MILLISECONDS，毫秒
config.setWhenMaxWaitTimeUnit(TimeUnit.MILLISECONDS);
//每个WHEN是否用单独的线程池
config.setWhenThreadPoolIsolate(false);
//设置解析模式，一共有三种模式，PARSE_ALL_ON_START | PARSE_ALL_ON_FIRST_EXEC | PARSE_ONE_ON_FIRST_EXEC
config.setParseMode(ParseModeEnum.PARSE_ALL_ON_START);
//全局重试次数，默认为0
config.setRetryCount(0);
//是否支持不同类型的加载方式混用，默认为false
config.setSupportMultipleType(false);
//全局默认节点执行器
config.setNodeExecutorClass("com.yomahub.liteflow.flow.executor.DefaultNodeExecutor");
//是否打印执行中过程中的日志，默认为true
config.setPrintExecutionLog(true);
//是否开启本地文件监听，默认为false
config.setEnableMonitorFile(false);
//是否开启快速解析模式，默认为false
config.setFastLoad(false);
//是否开启Node节点实例ID持久化，默认为false
config.setEnableNodeInstanceId(false);
//是否开启虚拟线程(只在JDK21+环境有效)，默认为true
config.setEnableVirtualThread(true);
//简易监控配置选项
//监控是否开启，默认不开启
config.setEnableLog(false);
//监控队列存储大小，默认值为200
config.setQueueLimit(200);
//监控一开始延迟多少执行，默认值为300000毫秒，也就是5分钟
config.setDelay(300000L);
//监控日志打印每过多少时间执行一次，默认值为300000毫秒，也就是5分钟
config.setPeriod(300000L);
```

---

## 🌵其他场景安装运行

**URL:** https://liteflow.cc/pages/59e827/

**Contents:**
- 🌵其他场景安装运行
- # 说明
- # 依赖
- # 定义你的组件
- # 规则文件的配置
- # 初始化你的FlowExecutor执行器
- # 用FlowExecutor执行

虽说Springboot/Spring已经成为了Java项目中的标配，但是为了照顾到启用其他框架的小伙伴（其更重要的原因是强耦合Spring我始终觉得是瑕疵，有点代码洁癖），现在在非Spring体系的环境中也能使用LiteFlow框架带来的便捷和高效。

LiteFlow文档中提到的98%以上的特性功能都能在非Spring体系中生效。其中不生效的特性和功能有：

为稳定版本，目前jar包已上传中央仓库，可以直接依赖到

resources的config/flow.xml中如下配置：

通过以下代码你可以轻易的初始化FlowExecutor处理器：

要注意的是，不建议每次执行流程都去初始化FlowExecutor，这个对象的初始化工作相对比较重，全局只需要初始化一次就好了。建议在项目启动时初始化或者第一次执行的时候初始化。

这个DefaultContext是默认的上下文，用户可以用最自己的任意Bean当做上下文传入，如果需要传入自己的上下文，则需要传用户Bean的Class属性，具体请看数据上下文这一章节。

**Examples:**

Example 1 (xml):
```xml
<dependency>
	<groupId>com.yomahub</groupId>
    <artifactId>liteflow-core</artifactId>
	<version>2.15.1</version>
</dependency>
```

Example 2 (java):
```java
public class ACmp extends NodeComponent {

    @Override
    public void process() {
        //do your business
    }
}
```

Example 3 (java):
```java
public class BCmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

Example 4 (java):
```java
public class CCmp extends NodeComponent {

	@Override
	public void process() {
		//do your business
	}
}
```

---

## 🍮启动不检查规则

**URL:** https://liteflow.cc/pages/891f36/

**Contents:**
- 🍮启动不检查规则

LiteFlow默认启动的时候都需要解析规则，但是在协作开发的时候，很可能有些组件还没有，但是规则里却写上了这个组件。这就会导致启动报错。

为此，框架提供了一个新的全局参数供用户配置：

如果设置成PARSE_ONE_ON_FIRST_EXEC那就不会启动时检查规则。

官方建议，如果你希望启动时不检查规则，直接设置PARSE_ONE_ON_FIRST_EXEC就可以了。

**Examples:**

Example 1 (properties):
```properties
liteflow.parse-mode=PARSE_ONE_ON_FIRST_EXEC
```

---

## 🍖平滑热刷新

**URL:** https://liteflow.cc/pages/204d71/

**Contents:**
- 🍖平滑热刷新
- # 自动刷新的场景
- # 主动调用代码全量刷新
- # 单独刷新某一个规则
- # 单独刷新某一个决策规则v2.12.2+
- # 单独刷新某一个脚本

LiteFlow支持了优雅平滑热刷新的特性。

即你可以在不重启服务的情况下，进行规则的重载。并且在高并发下刷新的时候，正在执行流程的线程是完全平滑的，不会因为刷新的过程而出现中断的现象。

在刷新时，正在执行的流程还是走的旧的流程，刷新好。后续request会自动切换到新的流程。

如果你使用LiteFlow原生支持的zookeeper，etcd，nacos，apollo等插件（关于如何集成插件，请参考规则文件这一大章节），不需要你做任何事，只要规则更改之后，会自动热平滑刷新。

如果你是基于本地磁盘规则文件的，并且开启了自动监听设置，那么更改流程后也会自动平滑刷新。关于如何开启自动监听，请参考本地规则文件监听这一章。

如果你使用了LiteFlow原生支持的sql，redis这两个插件，并开启了轮询开关，在你更新了规则或脚本之后，也会自动平滑热刷新。但是受限于轮询间隔时间，会有一定的延时。

关于这个场景，可以参考SQL数据库配置源以及轮询模式配置。

如果你使用了数据库作为规则文件的存储方式，或是你自己实现了自定义配置源，那么LiteFlow还提供了一种基于代码刷新的方式。

这个方法会按照启动时的方式去拉取你最新的所有规则以及组件配置信息，进行平滑热刷新。

1.这样刷新是全量刷新，不过各位同学不用担心其性能，经测试，LiteFlow框架一秒可以刷新1000条规则左右，这都是一些cpu级别的操作，如果你规则没有上大几千，几w条，那么推荐这种方式。

2.如果你的应用是多节点部署的，必须在每个节点上都要刷新，因为规则是存储在jvm内存里的。这就意味着，如果你把刷新规则做成一个rpc接口（诸如dubbo接口之类的），那么rpc接口只会调用到其中一个节点，也就是说，只会有一个节点的规则会刷新。

正确的做法是：利用mq发一个消息，让各个节点去监听到，进行刷新。

如果你的规则比较多，成千上万条，又或者你就是不想全量刷新。希望单独刷新某个改动的规则。

既然是指定刷新，那么必须你要获取到改动的EL内容，然后再利用动态代码构建重新build下就可以了，这种方式会自动替换缓存中已有的规则。这种方式不用在build之前销毁流程。

如果是多服务节点部署的情况下，还是要遵循每个节点要都刷新，上面已经说明具体建议的方式。这里不再赘述。

如果你使用了决策路由，那么可以通过FlowBus连带决策体一起进行刷新：

如果你想要用代码方式来刷新一个指定的脚本，可以这么做：

**Examples:**

Example 1 (java):
```java
LiteflowMetaOperator.reloadAllChain();
```

Example 2 (java):
```java
LiteflowMetaOperator.reloadOneChain("chain1", "THEN(a, b, c)");
```

Example 3 (java):
```java
LiteflowMetaOperator.reloadOneChain("chain1", "THEN(a, b, c)", "AND(r1, r2)");
```

Example 4 (java):
```java
LiteflowMetaOperator.reloadScript(nodeId, script);
```

---

## 🥦异步循环模式

**URL:** https://liteflow.cc/pages/35cc4a/

**Contents:**
- 🥦异步循环模式
- # 使用方法
- # 例子
- # 使用说明

LiteFlow支持循环表达式的异步模式，使得各个循环表达式的循环子项可以异步执行。

对于LiteFlow中的次数循环表达式、条件循环表达式以及迭代循环表达式等循环表达式，可以使用parallel子关键字（默认为false）来配置循环子项的执行方式，使其成为异步模式的循环表达式（所谓异步模式，就是各个循环子项之间并行执行）。

如果parallel子关键字设置为true，表示各循环子项之间并行执行，否则各循环子项之间串行执行。

对于次数循环表达式，可以这样配置，使其各个循环子项并行执行：

如果使用上述配置，每个循环子项本身的执行方式保持不变，只是各个循环子项之间的执行方式变为并行执行，也就是chain1会并行执行两次THEN(a,b,c)。

对于条件循环表达式，可以这样配置，使其各个循环子项并行执行：

对于迭代循环表达式，可以这样配置，使其各个循环子项并行执行：

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
   FOR(2).parallel(true).DO(THEN(a,b,c));
</chain>
```

Example 2 (xml):
```xml
<chain name="chain6">
   WHILE(x).parallel(true).DO(THEN(a,b,c));
</chain>
```

Example 3 (xml):
```xml
<chain name="chain7">
   ITERATOR(x).parallel(true).DO(THEN(a,b,c));
</chain>
```

---

## 🧇打印信息详解

**URL:** https://liteflow.cc/pages/4d614c/

**Contents:**
- 🧇打印信息详解
- # 流程执行中打印
- # 打印步骤信息

在执行一条流程时，你在日志中会看到诸如以下的日志：

其中最前面的一串序号，代表这个请求的请求ID，一个请求无论经历了多少个组件，他们的请求ID都是一致的，你可以根据这个ID在日志中进行快速定位进行排查。

在后面会跟着一个[O]或者[X]，[O]代表了执行了这个组件的主要逻辑，[X]代表因为isAccess()返回了false所以没进入这个组件的主要逻辑。

如果你不希望打印这种中间执行信息，LiteFlow提供了配置项，你需要作如下设置：

在执行完一个链路之后，框架会自动打出这一条流程的执行步骤顺序，如下所示：

如果你希望在打印流程链的时候增加别名描述，那你需要在定义组件的时候设置name属性，具体请参照组件别名。

增加了别名之后，执行步骤信息的打印会变成以下样子：

这里的表达形式为：组件ID[组件别名]<耗时毫秒>

**Examples:**

Example 1 (text):
```text
[ea1af4810cc849d58948d091d858b29a]:[O]start component[ACmp] execution
[ea1af4810cc849d58948d091d858b29a]:[O]start component[BCmp] execution
[ea1af4810cc849d58948d091d858b29a]:[X]start component[CCmp] execution
[ea1af4810cc849d58948d091d858b29a]:[O]start component[DCmp] execution
```

Example 2 (properties):
```properties
liteflow.print-execution-log=false
```

Example 3 (text):
```text
a<100>==>c<10>==>m<0>==>q<200>==>p<300>==>p1<0>==>g<305>
```

Example 4 (text):
```text
a[组件A]<100>==>b[组件B]<0>==>m[组件M]<256>
```

---

## 📎普通组件

**URL:** https://liteflow.cc/pages/8486fb/

**Contents:**
- 📎普通组件

普通组件节点需要继承NodeComponent，可用于THEN和WHEN等关键字中。

普通组件的内部可以覆盖的方法和this关键字可调用的方法见组件内方法覆盖和调用这一章。

上述例子中的a即为这个组件的id，对于组件id命名的约束，有以下几个规范：

比如这些都是不行的：88Cmp，cmp-11, user=123，这些组件id在编排时会编译不过。

但是也有方法能打破这个限制，请参考组件名包装这一章。

← 🌵其他场景代码设置配置项 ✂️选择组件→

**Examples:**

Example 1 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		System.out.println("ACmp executed!");
	}
}
```

---

## 🍌本地规则文件监听

**URL:** https://liteflow.cc/pages/f8aa79/

**Contents:**
- 🍌本地规则文件监听
- # 单个文件的监听v2.10.0+
- # 模糊文件路径的监听v2.11.1+

首先，在LiteFlow的配置liteflow.rule-source中，不光可以配置项目内的规则文件，其实还可以配置本地磁盘上的文件的，比如：

但是当你本地规则文件改变了的情况下，你的项目是无法获知的，你只能通过手动刷新规则去实现热刷新(详细请阅读平滑热刷新)。

现在LiteFlow支持对本地文件的监听配置了。

你只需要配置liteflow.enable-monitor-file=true，即可开启自动对文件的监听特性。文件改动，你的项目无需做任何事，立马自动刷新整个规则。非常方便。

如果你用模糊匹配的方式也是可以的，同样也会对匹配的所有文件进行监听。

还是只需要配置liteflow.enable-monitor-file=true即可。

**Examples:**

Example 1 (properties):
```properties
liteflow.rule-source=/Users/bryan31/liteflow/test/flow.xml
```

Example 2 (properties):
```properties
liteflow.rule-source=/Users/bryan31/liteflow/**/flow*.xml
```

---

## 📕本地规则文件配置

**URL:** https://liteflow.cc/pages/51ddd5/

**Contents:**
- 📕本地规则文件配置
- # 规则文件
- # 规则组成部分
- # 常规配置
- # 工程内指定多个路径
- # 绝对路径指定多个路径
- # 绝对路径指定模糊路径v2.11.1+

LiteFlow的规则文件非常轻量，非常容易上手。主要由Node节点和Chain节点组成：

如果是spring体系的应用，那么node的注册是自动完成的，<nodes>标签不是必须的，如果你有脚本节点，那需在这里声明：

如果是非spring体系的应用，node的注册是在<nodes>标签里进行声明：

在LiteFlow框架中，规则文件是驱动/编排整个流程的关键，用户通过指定rule-source来定位规则文件的本地路径。而rule-source也是LiteFlow框架中必须配置的参数，而其他参数都不是必须的（都有默认值）。

以下以Springboot的配置做例子，Spring以及非Spring的环境配置可以详细阅读配置项这章节。

如果想扫描所有其他jar包中的类路径，可以使用classpath*::

你也可以使用Spring EL表达式进行模糊匹配，加载多个配置文件：

以上则表示，在/data/lf/ 这个目录下，以及多级子目录下的所有匹配*Rule这个文件命名并且以xml结尾的所有文件。

**Examples:**

Example 1 (xml):
```xml
<flow>
    <nodes>
        <node id="s1" name="普通脚本1" type="script" language="java">
            这里写脚本
        </node>

        <node id="s2" name="普通脚本1" type="script" language="java">
            这里写脚本
        </node>
    </nodes>

    <chain id="chain1">
        这里写规则
    </chain>
</flow>
```

Example 2 (xml):
```xml
<flow>
    <nodes>
        <node id="a" class="com.yomahub.liteflow.test.parser.cmp.ACmp"/>
        <node id="b" class="com.yomahub.liteflow.test.parser.cmp.BCmp"/>
    </nodes>

    <chain id="chain1">
        这里写规则
    </chain>
</flow>
```

Example 3 (properties):
```properties
liteflow.rule-source=config/flow.xml
```

Example 4 (yaml):
```yaml
liteflow:
  rule-source: config/flow.xml
```

---

## 🥨给上下文设置别名

**URL:** https://liteflow.cc/pages/e71ced/

**Contents:**
- 🥨给上下文设置别名

LiteFlow还支持给上下文设置别名，只需要在上下文中进行标注就可以了：

这个特性，尤其是在你要使用多上下文，并且两个上下文是一个类的时候特别有用，因为用class的方式去取有可能就会取错，而别名的方式就可以很好的规避这点。

如果你的上下文没声明@ContextBean，其实也是可以通过名称取到的，这时的名称就是上下文className，并且首字母小写。比如你的上下文类名为PriceContext，那么你通过this.getContextBean("priceContext");也是可以取到的。

← 🪶用初始化好的上下文传入 🥙上下文参数注入→

**Examples:**

Example 1 (java):
```java
@ContextBean("anyName")
public class YourContext {
    ...
}
```

Example 2 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 流程初始参数, YourContext.class);
```

Example 3 (java):
```java
YourContext context = new YourContext();
context.setXxxx(yyy);
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 流程初始参数, context);
```

Example 4 (java):
```java
@Component("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		TestContext context = this.getContextBean("anyName");
		...
	}
}
```

---

## 📙自定义配置源

**URL:** https://liteflow.cc/pages/25f2c0/

**Contents:**
- 📙自定义配置源
- # 说明
- # 配置路径

LiteFlow原生只允许一种配置源，比如你使用了数据库配置源，那么就无法使用redis配置源了，你无法一部分规则/脚本从数据库取，另一部分从redis中取。

如果你希望整合两种或以上的配置源，又或者你想从其他框架不支持的地方获取规则/脚本，就需要用到自定义配置源了。

这部分LiteFlow只提供扩展接口，需要开发者自己开发的。

事实上LiteFlow支持的配置源，也是扩展这个接口来实现的。有兴趣的，可以看看源码。

LiteFlow提供扩展继承类ClassXmlFlowELParser

无论你数据存在几个地方，或者是存于哪个存储。中间逻辑需要开发者自己实现，并组装成完成的xml并返回。就是这种形式：

自定义配置源这个类也会自动注入到spring的上下文中，所以在这个类里可以随意注入spring上下文中的bean，可以使用@Autowired和@Resources等标签

以下以Springboot的配置做例子，Spring以及非Spring的环境配置可以详细阅读配置项这章节。

你只需要把rule-source改成你自定义规则配置源的类即可

**Examples:**

Example 1 (java):
```java
public class TestCustomParser extends ClassXmlFlowELParser {

	@Override
	public String parseCustom() {
		System.out.println("进入自定义parser");
		String xmlContent = null;
		//这里需要自己扩展从自定义的地方获取配置
		return xmlContent;
	}
}
```

Example 2 (xml):
```xml
<flow>
    <nodes>
        <node id="脚本id1" name="脚本名称" type="script" language="脚本语言">
            ...
        </node>

        <node id="脚本id2" name="脚本名称" type="script" language="脚本语言">
            ...
        </node>
        
        ...
    </nodes>
    
    <chain name="chain1">
        ...
    </chain>

    <chain name="chain2">
        ...
    </chain>
    
    ...
</flow>
```

Example 3 (properties):
```properties
liteflow.rule-source=el_xml:com.yomahub.liteflow.test.TestCustomParser
```

---

## 订阅模式配置

**URL:** https://liteflow.cc/pages/3f553f/

**Contents:**
- 订阅模式配置
- # 工作原理
- # 配置参数
- # 配置说明
- # 存储数据说明
- # 自动刷新
- # 模式优缺点
- # 脚本key的语言配置
- # 规则的启用关闭和脚本启用关闭v2.12.0+
- # 小例子

在配置参数中添加mode:sub，可将规则刷新机制选为订阅模式。

订阅模式基于Pub/Sub机制，依赖于Redisson中RMapCache结构的监听功能。

考虑到轮询模式无法保证规则刷新的实时性，因此提供订阅模式的刷新机制，即客户端修改数据后发送一个事件，LiteFlow订阅到该事件后进行数据刷新。

基于Pub/Sub机制，若采用Redis原生Hash结构，则修改数据方需要增加额外的开发成本来发送事件。 为降低用户修改规则的开发成本，Redis配置源的订阅模式选择采用Redisson的RMapCache结构。

RMapCache可看作自带监听功能的Redis Hash结构，其底层通过创建额外的Key和Lua脚本，自动使用Pub/Sub来实现监听机制。

需要注意的是，由于Redisson对RMapCache结构中的field和value进行了改动，并非纯文本。故对数据的读取和修改均只能使用Redisson客户端进行。

Redis配置源支持单点和哨兵两种模式。订阅模式下配置参数如下：

在订阅模式中，规则和脚本数据均以Redisson RMapCache结构存储，配置项chainKey和scriptKey即为该RMapCache的名字。

对于规则来说，你需要使用Redisson客户端，为规则单独创建一个RMapCache类型的数据，这个结构内的每个键值对就是一个规则，RMapCache内的key的格式为：规则ID[:是否启用]，其中方括号内的为可选项，value为单纯的EL（THEN(a,b,c)）。

假设你的规则RMapCache数据键名为:chains，那么利用Redisson客户端的数据操作如下：

对于脚本来说，RMapCache中的key有固定格式：脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，其中方括号内的为可选项。 value为脚本数据

假设你的脚本RMapCache数据键名为:scripts，那么利用Redisson客户端的数据操作如下：

关于脚本类型，可以参照定义脚本组件这一章节。

使用了此Redis配置源插件的订阅模式，凡是在配置的RMapCache对象内的数据改动，会自动推送到业务系统，进行实时的平滑热刷新，你无需做任何事情。

根据工作原理，订阅模式有如下优势和局限性：

如果对数据数据延迟容忍度低，希望保证实时性，且接受使用Redisson，推荐采用订阅模式。

如果你只依赖了一种脚本语言插件包，那么语言这项是不需要配置的。会自动识别的。如果你配置了多语言脚本，那么脚本语言这一项，是必须要写的。

比如s1:boolean_script:布尔脚本s1:js。

关于脚本的多语言共存，请参考多脚本语言混合共存这一章。

LiteFlow也支持在Etcd节点上保留数据的同时关闭和启动规则/脚本。

之前说到规则的key的固定格式为规则ID[:是否启用]，如果配置chain1:false，那么这个规则就是关闭状态。相当于逻辑删除。

当然如果你只是配置key为chain1，那么等价于chain1:true。

对于脚本key来说，固定格式为脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，如果配置s1:script:脚本s1:groovy:false，那么这个脚本就是关闭状态，相当于逻辑删除。

如果不配置最后一项，比如s1:script:脚本s1:groovy，那么等价于s1:script:脚本s1:groovy:true。

对于规则key或者脚本key来说，一定要以冒号为分隔符对应好位置，如果你想配置是否启动，那么是在第5项，前面4项就必须要写，如果你写成s1:script:脚本s1:false那将会报错。

为了让大家能简单上手Redis规则文件的配置和运行，这里有一个小demo，大家可以拉到本地来运行，需要你替换Redis的配置信息。

运行项目前，先读项目里的readme.txt文件。

https://github.com/bryan31/liteflow-ext-rule-demo

**Examples:**

Example 1 (yaml):
```yaml
liteflow:
  rule-source-ext-data-map:
    #单点模式配置如下两项
    host: 127.0.0.1
    port: 6379
    #哨兵模式配置如下三项
    redisMode: sentinel
    masterName: mymaster
    sentinelAddress: 127.0.0.1:26389,127.0.0.1:26379
    #集群模式配置以下两项(2.15.0+支持)
    redisMode: cluster
    clusterAddress: 127.0.0.1:26389,127.0.0.1:26379
    #如果你没有用户名或密码可以不配置
    username: root
    password: 123456
    #下面两项可以选配(2.12.2+支持)
    connectionPoolSize: 2
    connectionMinimumIdleSize: 4
    #下面这几项必须得配置
    mode: poll
    pollingInterval: 60
    pollingStartTime: 60
    chainDataBase: 1
    chainKey: chainKey
    #如果你没有脚本组件，以下可以不配置
    scriptDataBase: 1
    scriptKey: scriptKey
```

Example 2 (properties):
```properties
liteflow.rule-source-ext-data={\
      \# 单点模式配置如下两项\
      "host":"127.0.0.1",\
      "port":6379,\
      \# 哨兵模式配置如下三项\
      "redisMode":"sentinel",\
      "masterName":"mymaster",\
      "sentinelAddress":"127.0.0.1:26389,127.0.0.1:26379",\
      \# 集群模式配置以下两项(2.15.0+支持)\
      "redisMode":"cluster",\
      "clusterAddress":"127.0.0.1:26389,127.0.0.1:26379",\
      \# 如果你没有用户名或密码可以不配置\
      "username":"root",\
      "password":"123456",\
      \# 下面两项可以选配(2.12.2+支持)\
      "connectionPoolSize":2,\
      "connectionMinimumIdleSize":4,\
      \# 下面这几项必须得配置\
      "mode":"poll",\
      "pollingInterval":60,\
      "pollingStartTime":60,\
      "chainDataBase":1,\
      "chainKey":"chainKey",\
      \# 如果你没有脚本组件，以下可以不配置\
      "scriptDataBase":1,\
      "scriptKey":"scriptKey"\
}
```

Example 3 (unknown):
```unknown
// Make sure to add code blocks to your code group
```

Example 4 (java):
```java
RMapCache<String, String> chains = redissonClient.getMapCache("chains");
chains.put("chain1", "THEN(a, b, c);");
chains.put("chain2", "IF(x, b).ELIF(y, c).ELSE(d);");
```

---

## 轮询模式配置

**URL:** https://liteflow.cc/pages/186747/

**Contents:**
- 轮询模式配置
- # 工作原理
- # 配置参数
- # 配置说明
- # 存储数据说明
- # 自动刷新
- # 模式优缺点
- # 脚本key的语言配置
- # 规则的启用关闭和脚本启用关闭v2.12.0+
- # 小例子

Redis配置源的规则刷新机制默认为轮询模式。

轮询模式以 定时拉取 的方式进行规则数据刷新。

在拉取方式的具体设计上主要考虑到两个因素。其一，若每次去Redis中拉取规则数据，需要再次解析和编译，会对框架性能造成很大影响； 其二，大部分时间拉取的数据并无变化，无用功较多。

考虑到如上两个问题，轮询模式数据拉取的工作方式设定为：

1、首次在Redis中获取数据后，将数据以KV结构缓存到本地，key为chainId/scriptId (以下简称数据Id)，value为数据的指纹值 (SHA-1值)。相较于原始数据，指纹值数据量小，缓存占用空间可忽略不计。

2、此后的每次轮询中，无需拉取全部数据，而是在Redis端调用脚本计算当前数据的指纹值，仅传输数据Id及对应指纹值。

3、将拉取获得的最新指纹值与本地缓存的指纹值对比，对于发生变化的数据，针对性地根据数据Id从Redis中获取最新数据值，更新规则元数据，同时更新本地缓存指纹值。

以上设定中，首次轮询起始时间、轮询时间间隔均可自由配置。

Redis配置源支持单点和哨兵两种模式。轮询模式下配置参数如下：

在轮询模式中，规则和脚本数据均以Redis Hash结构存储，配置项chainKey和scriptKey即为该Hash的名字。

你可以在redis UI客户端直接存入数据，如果使用redis client框架以代码的方式存入时，一定要注意编码，比如以Redisson存储规则时，一定要设置Codec为StringCodec。

对于规则来说，你在Redis中需要为规则单独创建一个Hash类型的数据，这个Hash内的每个键值对就是一个规则，Hash内的每一个键的格式为：规则ID[:是否启用]，其中方括号内的为可选项，值为单纯的EL（THEN(a,b,c)）。

假设你的规则Hash数据键名为:chains，那么配置形式样例如下：

对于脚本来说，Hash中的field有固定格式：脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，其中方括号内的为可选项。 value为脚本数据

假设你的脚本Hash数据键名为:scripts，那么配置形式样例如下：

关于脚本类型，可以参照定义脚本组件这一章节。

使用了此Redis配置源插件的轮询模式，凡是在配置的Redis键内的数据改动，会依据设定的轮询参数定期拉取并更新数据，你无需做任何事情。

根据工作原理，轮询模式在性能方面做出了权衡：

如果对数据数据延迟容忍度高，且希望Redis客户端不受限的情况下，推荐采用轮询模式。

如果你只依赖了一种脚本语言插件包，那么语言这项是不需要配置的。会自动识别的。如果你配置了多语言脚本，那么脚本语言这一项，是必须要写的。

比如s1:boolean_script:布尔脚本s1:js。

关于脚本的多语言共存，请参考多脚本语言混合共存这一章。

LiteFlow也支持在Etcd节点上保留数据的同时关闭和启动规则/脚本。

之前说到规则的key的固定格式为规则ID[:是否启用]，如果配置chain1:false，那么这个规则就是关闭状态。相当于逻辑删除。

当然如果你只是配置key为chain1，那么等价于chain1:true。

对于脚本key来说，固定格式为脚本组件ID:脚本类型[:脚本名称:脚本语言:是否启用]，如果配置s1:script:脚本s1:groovy:false，那么这个脚本就是关闭状态，相当于逻辑删除。

如果不配置最后一项，比如s1:script:脚本s1:groovy，那么等价于s1:script:脚本s1:groovy:true。

对于规则key或者脚本key来说，一定要以冒号为分隔符对应好位置，如果你想配置是否启动，那么是在第5项，前面4项就必须要写，如果你写成s1:script:脚本s1:false那将会报错。

为了让大家能简单上手Redis规则文件的配置和运行，这里有一个小demo，大家可以拉到本地来运行，需要你替换Redis的配置信息。

运行项目前，先读项目里的readme.txt文件。

https://github.com/bryan31/liteflow-ext-rule-demo

**Examples:**

Example 1 (yaml):
```yaml
liteflow:
  rule-source-ext-data-map:
    #单点模式配置如下两项
    host: 127.0.0.1
    port: 6379
    #哨兵模式配置如下三项
    redisMode: sentinel
    masterName: mymaster
    sentinelAddress: 127.0.0.1:26389,127.0.0.1:26379
    #集群模式配置以下两项(2.15.0+支持)
    redisMode: cluster
    clusterAddress: 127.0.0.1:26389,127.0.0.1:26379
    #如果你没有用户名或密码可以不配置
    username: root
    password: 123456
    #下面两项可以选配(2.12.2+支持)
    connectionPoolSize: 2
    connectionMinimumIdleSize: 4
    #下面这几项必须得配置
    mode: poll
    pollingInterval: 60
    pollingStartTime: 60
    chainDataBase: 1
    chainKey: chainKey
    #如果你没有脚本组件，以下可以不配置
    scriptDataBase: 1
    scriptKey: scriptKey
```

Example 2 (properties):
```properties
liteflow.rule-source-ext-data={\
      \# 单点模式配置如下两项\
      "host":"127.0.0.1",\
      "port":6379,\
      \# 哨兵模式配置如下三项\
      "redisMode":"sentinel",\
      "masterName":"mymaster",\
      "sentinelAddress":"127.0.0.1:26389,127.0.0.1:26379",\
      \# 集群模式配置以下两项(2.15.0+支持)\
      "redisMode":"cluster",\
      "clusterAddress":"127.0.0.1:26389,127.0.0.1:26379",\
      \# 如果你没有用户名或密码可以不配置\
      "username":"root",\
      "password":"123456",\
      \# 下面两项可以选配(2.12.2+支持)\
      "connectionPoolSize":2,\
      "connectionMinimumIdleSize":4,\
      \# 下面这几项必须得配置\
      "mode":"poll",\
      "pollingInterval":60,\
      "pollingStartTime":60,\
      "chainDataBase":1,\
      "chainKey":"chainKey",\
      \# 如果你没有脚本组件，以下可以不配置\
      "scriptDataBase":1,\
      "scriptKey":"scriptKey"\
}
```

Example 3 (unknown):
```unknown
// Make sure to add code blocks to your code group
```

---

## 配置说明

**URL:** https://liteflow.cc/pages/38dcf8/

**Contents:**
- 配置说明
- # 依赖
- # 配置模式
- # 配置模式选择

LiteFlow原生支持了Redis的规则配置源。

如果使用Redis作为规则配置源，你需要添加以下额外插件依赖：

依赖了插件包之后，你无需再配置liteflow.ruleSource路径。

Redis配置源支持平滑热刷新，在刷新机制上实现了【轮询】和【订阅】两种模式，可通过配置自由选择。

【轮询模式】：基于Redis的Hash结构，通过定时轮询的方式进行规则刷新，轮询频率可配置，轮询间隔内有一定刷新延迟。

【订阅模式】：基于Redisson客户端的RMapCache存储结构，只支持使用Redisson客户端，可实现规则的实时平滑刷新。

两种模式的插件依赖相同，仅通过配置参数加以区分。 如果没有配置模式选择，默认为轮询模式。

两种模式的工作原理及具体配置方式详见对应子菜单：

基于两种工作模式的特点，推荐根据实际需要进行选择。

如果你需要采用其他Redis客户端 (如Jedis等)，且接受轮询间隔内的数据刷新延迟，推荐你配置为【轮询模式】

如果你需要确保规则刷新的实时性，不容忍轮询间隔内的延迟，且接受使用Redisson，推荐你配置为【订阅模式】

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-rule-redis</artifactId>
    <version>2.15.1</version>
</dependency>
```

---
