# Liteflow - Orchestration

**Pages:** 62

---

## bind语法

**URL:** https://liteflow.cc/pages/934d71/

**Contents:**
- bind语法
- # 绑定静态数据
- # 绑定动态数据
- # bind语法的覆盖用法v2.13.1+

LiteFlow还提供了bind语法关键字，它和data使用场景是一致的，但是它和data关键不同的是，它允许绑定KV键值对，比如

你可以在组件中通过getBindData方法来获取：

当然bind的时候也可以把value设置成json字符串，那么在取值的时候，第二个参数就可以传相应的VO的class，LiteFlow内部可以自动把Json转型成对象。

bind关键字也可以用作于表达式，子变量，chain上，其意义是被赋值的表达式/子变量/chain里所有的组件都绑定了相同的值，比如：

LiteFlow还允许用bind关键字去绑定动态数据，这是tag和data关键字无法做到的。

所谓动态数据就是在编写规则EL的时候无法确定的，你可以bind一个表达式，LiteFlow会根据你bind的表达式去上下文中去搜索所需要的数据。

bind动态数据，value必须为一个表达式，且格式为${表达式}。

那么在b组件中就可以通过this.getBindData("k1", String.class)拿到上下文中orderCode的值。

如果想拿到上面OrderContext中Member对象中的memberName对象，你可以通过点操作符得到：

如果你除了OrderContext还传了其他上下文，以上表达式也是可以得到的具体值的。因为LiteFlow会智能的根据你上下文中去匹配你的表达式。

但是如果有种极端情况，就是假设你传了OrderContext，又传了UserContext，两个上下文都有id属性，那么如果你写以下表达式：

那么bind的到底是哪个上下文里的id呢？

这里如果你不指定，永远是bind第一个上下文的id，那么如果你要指定绑定UserContet里的id怎么办呢？

这时候就需要指定上下文了，你可以这样指定：

这个userContext是UserContext的首字符小写的形式。你也可以通过@ContextBean去改变，比如你这样定义：

其实在多上下文中属性名不冲突的情况，官方建议不要指定上下文，直接智能匹配。

绑定动态数据除了绑定在节点上，同样可以绑定在表达式，子变量，chain上。

bind语法如果同时在节点和表达式上同时使用，是不会相互覆盖的，比如：

上述表达式a拿到的是v2，b拿到的是v1，c拿到的是v2，b并不会被表达式上的bind给覆盖。

那如果想把b也强制覆盖成v2，则可以这么使用：

bind最后一个参数传true的话，那么bind里的所有节点，都会被强制覆盖。以上表达式a,b,c拿到的都是v2了。

**Examples:**

Example 1 (xml):
```xml
<chain id="chain1">
    THEN(a.bind("k1", "test"), b);
</chain>
```

Example 2 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeComponent {
	@Override
	public void process() {
		String bindValue = this.getBindData("k1", String.class);
		...
	}
}
```

Example 3 (xml):
```xml
<chain id="chain1">
    THEN(a,b).bind("k1","test");
</chain>

<chain id="chain2">
    THEN(SWITCH(y).TO(d,c), WHEN(a, b), IF(x, c, d)).bind("k1", "test")
</chain>

<chain id="sub">
    THEN(a,IF(NOT(x), b, c));
</chain>

<chain id="chain3">
    THEN(d, sub.bind("k1", "test2"))
</chain>
```

Example 4 (java):
```java
public class OrderContext {
    private Integer id;
    private String orderCode;
    private Member member;
    //getter setter 省略   
}

// Member对象定义如下：
public class Member {
    private String memberCode;
    private String memberName;
    //getter setter 省略   
}
```

---

## data语法

**URL:** https://liteflow.cc/pages/84538b/

**Contents:**
- data语法

你可以在EL语法中通过data来给组件设置外置参数，建议最好是JSON格式：

上述表达式中，同一个b组件，在不同的chain中被赋予了不同的外置参数，运行中在组件中通过this.getCmpData方法也能拿到相应的参数。

如果上述对象是一个Json的数组，在组件中也可以通过getCmpDataList方法来获取。

这个方法是可以返回对应结构的java对象的，只要传入相对应的class即可。

要注意的是，data关键字也可以用作于表达式，子变量，chain上，其意义是被赋值的表达式/子变量/chain里所有的组件都设置了相同的值，比如：

**Examples:**

Example 1 (xml):
```xml
<flow>
    <chain name="chain1">
        cmpData = '{"name":"jack","age":27,"birth":"1995-10-01"}';
    
        THEN(a, b.data(cmpData), c);
    </chain>
    
    <chain name="chain2">
        cmpData = '{"name":"rose","age":20,"birth":"1997-07-01"}';
    
        WHEN(c, b.data(cmpData));
    </chain>
</flow>
```

Example 2 (java):
```java
@LiteflowComponent("b")
public class BCmp extends NodeComponent {

	@Override
	public void process() {
		User user = this.getCmpData(User.class);
		...
	}

}
```

Example 3 (xml):
```xml
<chain name="chain1">
    THEN(a, b, c).data("123");
</chain>
```

Example 4 (xml):
```xml
<chain name="chain1">
    sub = WHEN(b, c);
    THEN(a, sub.data(""))
</chain>
```

---

## 🪀DEMO案例

**URL:** https://liteflow.cc/pages/0a8188/

**Contents:**
- 🪀DEMO案例
- # DEMO案例1
- # DEMO案例2
- # 外置规则存储案例

如果你想看一个实际的案例，加深对LiteFlow的理解。可以查看：

DEMO案例1 (opens new window)

这个案例为一个短信系统选取供应商的案例。相关配套文章链接如下：

写出个灵活的系统竟然可以如此简单！小白也能写出高级的Java业务！ (opens new window)

DEMO案例2 (opens new window)

这个案例为一个价格计算引擎，其目的是模拟了电商中对订单价格的计算。

这个示例工程提供了一个简单的界面，供大家测试之用

外置规则存储案例 (opens new window)

如果你想把规则放到DB里，或者zk/nacos/etcd里，此案例为一个简单的DEMO，你可以根据此案例的演示来进行接入。

---

## ☕️JDK支持度

**URL:** https://liteflow.cc/pages/7cf080/

**Contents:**
- ☕️JDK支持度

LiteFlow要求的最低的JDK版本为8，支持JDK8~JDK25所有的版本。

--add-opens java.base/sun.reflect.annotation=ALL-UNNAMED

以上JDK版本的支持指的是：均在各个JDK环境中通过了2000多个测试用例的评估而得出的。

而LiteFlow的测试用例覆盖率在90%。

如果你的JDK版本在21和以上版本的话，LiteFlow原生支持虚拟线程特性。具体请参照虚拟线程这章。

← 🍓项目特性 🌿Springboot支持度→

---

## 🎈LiteflowResponse对象

**URL:** https://liteflow.cc/pages/9f653d/

**Contents:**
- 🎈LiteflowResponse对象
- # 流程执行是否成功
- # 获取异常信息
- # 获得执行步骤详细信息
- # 上下文数据
- # 获得步骤字符串信息
- # 获得超时对象v2.12.3+

在执行器返回中，用的最多的就是返回一个LiteFlowResponse对象。

这个对象里面包含了很多结果数据和过程数据。

这个对象并不适合进行序列化返回，应用层如果想返回一些数据，应当自己构建对象。

你可以通过以下方法来判断一个流程是否执行成功：

如果一个流程isSuccess为false，则必然有异常信息，你可以通过以下方法来获得异常：

结果信息中也封装了流程执行每一步的详细信息，你可以通过这个方法来获取：

关于这上面2个方法的区别和步骤信息的详细请参考步骤信息。

流程在执行过程中，会对上下文数据进行读写操作。一个流程的返回数据也应当包含在上下文中。

你获得了LiteFlowResponse对象之后，可以这样获得上下文Bean：

获得一个简单易懂的组件步骤的字符串拼装信息：

这里的表达形式为组件ID[组件别名]<耗时毫秒>。关于如何设置组件别名可以参考组件别名。

同时，response对象里还提供了getExecuteStepStrWithoutTime这个方法，用于返回不带有耗时时间的步骤字符串。

事实上，在每一个流程执行结束后，框架会自动打印这个步骤字符串，所以无需你自己获取打印。

这里只是说明如何获取，如果你要持久化下来，可以这样获取。

你可以调用liteflowResponse.getTimeoutItems()方法来获得超时的对象Id。

**Examples:**

Example 1 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 初始参数, CustomContext.class);
boolean isSuccess = response.isSuccess();
```

Example 2 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 初始参数, CustomContext.class);
if (!response.isSuccess()){
  Exception e = response.getCause();
}
```

Example 3 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 初始参数, CustomContext.class);
Map<String, CmpStep> stepMap = response.getExecuteSteps();
```

Example 4 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 初始参数, CustomContext.class);
Queue<CmpStep> stepQueue = response.getExecuteStepQueue();
```

---

## Slot是一个什么样的概念，在框架中起到什么样的作用？

**URL:** https://liteflow.cc/pages/ad60b4/

**Contents:**
- Slot是一个什么样的概念，在框架中起到什么样的作用？

有使用者肯定发现了，在组件中通过this关键字，可以调用到this.getSlot() 这个方法，返回一个slot。

那这个Slot是什么呢？在框架中起到什么样的作用？

Slot对象是上下文的一个包装类。每一个请求，都会申请一个新的Slot对象，同时一个请求结束的时候，也会回收这个slot对象。

LiteFlow框架声称的对于每个请求，上下文之间是隔离的，准确的来说，是Slot之间是隔离的。因为Slot隔离，所以上下文也隔离。上下文是Slot中的一个子项。

上下文是用来存放组件中产生的业务数据的，而它的包装类Slot里，则存放着一些框架对于这次请求中的元数据。大多数情况下，用户是不需要关心的。

大部分情况下，用户只要直接获得上下文就可以了。

值得一提的是，slot的数量可能有些使用者会以为只有1024个，从而认为并发如果超过1024，slot就会分配不过来了。其实不然，LiteFlow框架从很早开始就加入了slot自动扩容的机制，当slot用完的时候，slot就会自动扩容。扩容因子为0.75，也就是说，每次扩容之后的数量为扩容之前的1.75倍。其实使用者是完全不用担心并发大，slot分配不过来的问题。

---

## 🌿Springboot支持度

**URL:** https://liteflow.cc/pages/891e0f/

**Contents:**
- 🌿Springboot支持度

LiteFlow要求的Springboot的最低的版本是2.0。

支持的范围是Springboot 2.X ~ Springboot 3.X。

当然如果你使用了最新的Springboot 3.X，相应的JDK版本也要切换为JDK17及以上版本。

如果你想使用Springboot快速开始学习，请参考Springboot场景安装运行。

← ☕️JDK支持度 🌱Spring的支持度→

---

## 🌱Spring的支持度

**URL:** https://liteflow.cc/pages/2d12db/

**Contents:**
- 🌱Spring的支持度

如果你不使用Springboot，只使用Spring。

LiteFlow要求的Spring的最低版本为Spring 5.0。

支持的范围是Spring 5.X ~ Spring 6.X。

当然如果你使用了最新的Spring 6.X，相应的JDK版本也要切换为JDK17及以上版本。

如果你想使用Spring快速开始学习，请参考Spring场景安装运行。

← 🌿Springboot支持度 🍄说明→

---

## tag语法

**URL:** https://liteflow.cc/pages/cc24b8/

**Contents:**
- tag语法

关于SWITCH的选择tag标签内容请参考选择编排这一章。

你可以在规则表达式里给每个组件添加运行时的标签值，用tag关键字表示：

这样，你在代码里可以通过this.getTag()获取到当前的标签，这在有些时候非常有用，尤其是当多个相同组件编排时，你可以根据tag来获知到不同的参数。或者根据tag标签来给相同的组件作不同的判断。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    THEN(
        a.tag("tag1"),
        b.tag("tag2"),
        c.tag("tag3")
    );
</chain>
```

Example 2 (java):
```java
@LiteflowComponent("b")
public class BCmp extends NodeComponent {
    @Override
    public void process() {
        String tag = this.getTag();
        ...
    }
}
```

Example 3 (xml):
```xml
<chain name="chain1">
    THEN(
        a.tag("1"), a.tag("2"), a.tag("3"), a.tag("4"), a.tag("5"), a.tag("6")
    );
</chain>
```

---

## 🧉XML的DTD

**URL:** https://liteflow.cc/pages/0066ae/

**Contents:**
- 🧉XML的DTD

LiteFlow对XML增加了DTD，方便在XML里作一些检查和提醒约束。

当然不加也是没有关系的，因为LiteFlow xml节点非常简单，并没有很多的节点标签需要记忆。

**Examples:**

Example 1 (xml):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE flow PUBLIC  "liteflow" "https://liteflow.cc/liteflow.dtd">
<flow>
    <chain name="chain1">
        THEN(a,b,WHEN(c,d));
    </chain>
</flow>
```

---

## 🥙上下文参数注入

**URL:** https://liteflow.cc/pages/8777f8/

**Contents:**
- 🥙上下文参数注入

请注意，这个特性只适用于声明式组件。普通的继承式组件并不支持！

以下所有例子采用方法级别式声明。类级别式声明也是可以用此特性的。

我们在组件里面写业务，首先肯定就是要拿到上下文，在声明式组件里通常的写法为：

如果组件一多，那免不了每次都要写这么一句拿context，虽然不影响什么性能，但是非常繁琐。

LiteFlow从2.12.1开始推出了上下文参数注入特性，可以在方法参数中注入你所需的上下文数据，从而直接拿到，无需再每次取一次了。

你在声明式组件中使用@LiteflowFact来定义你的注入型参数：

使用参数注入特性，可以把上下文中已有的值注入到方法参数上，上面这个例子你就可以直接获得上下文中user这个对象。

你可能会有疑惑，如果我这里有多个上下文，我并未指定上下文呀，到底是获取哪个上下文中的user这个对象呢？

LiteFlow会根据你获得的类型去你的上下文中智能的进行搜索匹配，也就是说，你无需关心上下文了。你只需关心组件需要的数据即可。

如果对象比较深，你还可以通过点操作符的方式：

以上这个例子表示address参数取自于上下文中的User对象中的Company对象中的address字段。

你在@LiteflowFact中写的表达式，会自动的从上下文中搜索相应的参数。即使你有多个上下文，也无需去指定上下文。

但是有一种情况，在使用时要注意：假设你有两个上下文，TestContext1和TestContext2，在这两个上下文里都有user这个对象，并且两个user里的信息是不一样的。这时你通过@LiteflowFact("user") User user这样去拿，拿到的是第一个user，在不同环境上可能还不一样。

所以使用上下文参数注入特性时，如果有多个上下文，请确保注入的对象，在多个上下文中只有一份，否则会有错乱情况。

当然在有多个上下文拥有同样的属性的时候，你也可以指定上下文，例如这样：

所以当多个上下文拥有相同的属性id时，这里不指定上下文的话，那么框架只会默认赋值为搜索到的第一个名为id的参数。

← 🥨给上下文设置别名 🪴用表达式获取上下文参数→

**Examples:**

Example 1 (java):
```java
@LiteflowMethod(value = LiteFlowMethodEnum.PROCESS,nodeType = NodeTypeEnum.COMMON, nodeId = "b")
public void processB(NodeComponent bindCmp) {
    YourContext context = bindCmp.getContextBean(YourContext.class);
    //从context中取到业务数据进行处理
    User user = context.getUser();
    ...
}
```

Example 2 (java):
```java
public class TestContext {

    private User user;

    private String data1;
    
    //getter setter 省略   
}
```

Example 3 (java):
```java
@LiteflowComponent
public class CmpConfig {

    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS, nodeType = NodeTypeEnum.COMMON, nodeId = "a")
    public void processA(NodeComponent bindCmp,
                        @LiteflowFact("user") User user) {
        user.setName("jack");
    }
}
```

Example 4 (java):
```java
@LiteflowComponent
public class CmpConfig {

    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS, nodeType = NodeTypeEnum.COMMON, nodeId = "a")
    public void processA(NodeComponent bindCmp,
                        @LiteflowFact("user.company.address") String address) {
        //do biz
    }
}
```

---

## 🌭不同格式规则加载

**URL:** https://liteflow.cc/pages/a7e02e/

**Contents:**
- 🌭不同格式规则加载

有些小伙伴在配置规则时，因为特殊原因，需要同时加载2种不同的配置，甚至是配置源，比如：

这种模式在正常下会解析失败，但是LiteFLow提供了一个参数去支持这个特性，如果出现不同的类型的配置，需要加上这个属性：

**Examples:**

Example 1 (properties):
```properties
liteflow.rule-source=multipleType/flow.xml,multipleType/flow.json
```

Example 2 (properties):
```properties
liteflow.support-multiple-type=true
```

---

## 🍄与或非表达式

**URL:** https://liteflow.cc/pages/a8b344/

**Contents:**
- 🍄与或非表达式
- # 基本用法
- # 可以用的地方
- # 复杂嵌套

LiteFlow提供了与或非表达式，就是AND，OR，NOT表达式。

通过之前的几小章，应该可以知道，有些编排需要返回一个布尔值，比如条件编排：

其中x组件应该为布尔组件，返回的是一个布尔值。

但是如果这个布尔值并不是由一个组件决定的，而是由多个组件决定的呢。这里就可以用与或非表达式了。

假设这里的条件是要由x和y共同决定，利用与或非表达式中的AND:

上述AND的意思是，如果x和y都为true，则为真，会执行组件a，如果x和y有一个为false，则执行b。

AND里面可以有多个布尔组件或者与或非表达式。

上述OR的意思是，只要x和y中的一个为true，则为真，否则为假。

如果x返回true，则经过非运算后，为假，执行b，如果x返回false，则经过非运算后，为真，执行a。

NOT里面只能有一个布尔组件或者与或非表达式。

在LiteFlow所有EL表达式中，返回布尔值的地方都可以用与或非表达式，除了上述的IF外，还可以用在WHILE，BREAK表达式中。

如果你在THEN表达式中用与或非表达式，会报错的，因为普通组件并非是一个布尔值的的返回。

类似于这种，其实概念和java的与或非都一样，无非就是换了种写法。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    IF(x, a, b);
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    IF(AND(x,y), a, b);
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    IF(OR(x,y), a, b);
</chain>
```

Example 4 (xml):
```xml
<chain name="chain1">
    IF(NOT(x), a, b);
</chain>
```

---

## 🌴串行编排

**URL:** https://liteflow.cc/pages/a590ee/

**Contents:**
- 🌴串行编排
- # 基本用法
- # 等价用法v2.11.4+

如果你要依次执行a,b,c,d四个组件，你可以用THEN关键字，需要注意的是，THEN必须大写。

由于THEN关键字用来表示串行在语义上有些不妥，但是为了兼容，又没法完全替换。所以后期版本同时支持了SER关键字，和THEN是完全等价的。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    THEN(a, b, c, d);
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    THEN(a, b, THEN(c, d));
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    SER(a, b, c, d);
</chain>
```

---

## 🍂使用子变量

**URL:** https://liteflow.cc/pages/71ff49/

**Contents:**
- 🍂使用子变量

如果你看过上一章使用子流程后再来看这章，你会觉得其实使用子流程都是多此一举！

因为LiteFlow新的表达式语法可以直接让你在规则里定义子流程变量！

看到这里的你，是不是有种恍然大悟的感觉呢？用这种方式，其实子流程都显得黯然失色了。对于逻辑能力强大的你来说，利用这套表达式是不是任意复杂流程都能写出来了呢。

**Examples:**

Example 1 (xml):
```xml
<chain>
    t1 = THEN(C, WHEN(J, K));
    w1 = WHEN(Q, THEN(P, R)).id("w01");
    t2 = THEN(H, I);
    
    THEN(
        A, B,
        WHEN(t1, D, t2),
        SWITCH(X).to(M, N, w1),
        Z
    );
</chain>
```

---

## 🍁使用子流程

**URL:** https://liteflow.cc/pages/dc5df7/

**Contents:**
- 🍁使用子流程

在某些情况下，可能你用表达式写规则，会嵌套很多层。

比如下面这一个流程，是不是看上去就很复杂？

其实你用规则表达式来写，注意好缩进，也是可以很容易读懂的。上面的图可以写成以下规则表达式：

LiteFlow在新版的表达式里同样也支持子流程的定义，你可以拆分开来分别定义子流程，所以上面的表达式也可以写成以下的形式：

**Examples:**

Example 1 (xml):
```xml
<chain name="chain4">
    THEN(
        A, B,
        WHEN(
            THEN(C, WHEN(J, K)),
            D,
            THEN(H, I)
        ),
        SWITCH(X).to(
            M,
            N,
            WHEN(Q, THEN(P, R)).id("w01")
        ),
        Z
    );
</chain>
```

Example 2 (xml):
```xml
<chain name="mainChain">
    THEN(
    	A, B,
    	WHEN(chain1, D, chain2),
    	SWITCH(X).to(M, N, chain3),
    	z
    );
</chain>

<chain name="chain1">
  	THEN(C, WHEN(J, K));
</chain>

<chain name="chain2">
  	THEN(H, I);
</chain>

<chain name="chain3">
  	WHEN(Q, THEN(P, R)).id("w01");
</chain>
```

---

## 🌻关于分号

**URL:** https://liteflow.cc/pages/af44a6/

**Contents:**
- 🌻关于分号

大家可能注意到了，在EL规则的后面，示例都加上了分号。

但实际你运行的时候，不加分号也是可以正常运行的。

LiteFlow的EL规则依托于底层的表达式语言，进行了扩展和封装。在表示单行语句的时候可以不加。比如：

当然以下形式也认为是单行表达式，只是你人为地换行了而已，其实还是一句表达式

在使用子变量的时候，因为是多行表达式，所以一定得需要加分号，否则解析不通过，会报错，正确的规范是如下所示：

但是官方建议，不管是单行还是多行，尽量在每句表达式后加上分号。

因为LiteFlow的IDEA插件(7月13日上线)会去检查语法，如果每句表达式后面没加分号，会有红波浪线去提示。

当然对于单行表达式，即便忽略了语法检查提示，去运行，也是可以正常运行的，但是在子变量的场景中，一定得加上分号，这个要格外注意下。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    THEN(a, b, WHEN(c, d))
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    THEN(
        a, 
        b, 
        WHEN(c, d)
    )
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    t1 = THEN(a, b);
    w1 = WHEN(c, d);
    
    THEN(t1, w1);
</chain>
```

---

## 🌰关于注释

**URL:** https://liteflow.cc/pages/f3dc09/

**Contents:**
- 🌰关于注释

在LiteFlow的EL规则写法里，你也可以写注释。从2.13.0开始，只支持/** **/这种注释，不支持单行注释//。

要注意，不能在表达式中间夹杂注释，以下是无法编译的：

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    /** 我是注释 **/
    THEN(a, b, WHEN(c, d))
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    THEN(
        /**
        * 我是多行注释
        * 我是多行注释
        **/
        WHEN(c, d)
    )
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    THEN(
        a,b,
        /** 我是注释 **/
        WHEN(c, d)
    )
</chain>
```

---

## 🍽决策路由用法

**URL:** https://liteflow.cc/pages/b7ed78/

**Contents:**
- 🍽决策路由用法
- # 路由规则体
- # 执行方法
- # 执行指定namespace的决策路由v2.12.1+
- # 决策路由对数据库的支持
- # 要注意的点

在定义规则的时候，新增了一个<route>和<body>标签：

其中<route>标签里的就是决策EL，决策EL里只能用与或非表达式，所配置的组件只能是布尔组件。

而<body>里的内容就是原先的规则EL。

LiteFlow在FlowExecutor里新提供了一系列的方法用于执行带决策路由的规则，最基本的方法：

可以发现，executeRouteChain其实和execute2Resp差不多，当然execute2Resp支持的，executeRouteChain都支持。比如用初始化好的上下文传入，多上下文的传入。其实和原先都一样，只是不用再传chainId了而已。

当传入之后，LiteFlow会去并行的判断决策路由，符合决策的规则也会被并行的进行执行。

如果你的规则里并没有带有决策路由的规则，又或者是匹配决策路由后，没有可用的规则，LiteFlow会报错进行提示。

值得一说的是方法的返回，返回是一个List<LiteflowResponse>，List里面的就是每一个匹配到的规则执行之后生成的response，在LiteflowResponse中新增了chainId字段，用来识别是哪条规则的结果。

决策路由默认会去执行所有带<route>标签的chain。

但是如果你的决策路由很多，想要判断某一组决策路由，这时候可以可以在chain层面加入namespace参数，比如：

FlowExecutor也提供了一个带指定namespace的执行方法：

以上例子只会在n1这个namespace中去进行判断，会依次判断chain1和chain2满不满足决策条件，然后选择满足决策的规则进行执行。

目前决策路由特性仅对xml文件形式以及数据库方式进行了支持。其他存储均不支持这一特性。

1.决策路由体里的节点不能是除了布尔组件之外的任何类型的组件。

2.决策路由体里的表达式不能是除了与或非表达式之外任何其他的主表达式。

3.匹配到的每一个规则的上下文实例都是单独的，并且运行时是并行执行的。互不相干。

4.启动不检查规则特性对决策路由EL是不起作用的，决策体中的EL是启动时一定会检查的，但是决策体中的EL是可以加node关键字的。

5.决策路由体中的EL是可以加tag，data等副表达式的。

6.在JSON和YAML等格式中，也是可以加决策体的，多了一个route的key值，但是没有body，因为在json和yaml中，原先的规则体的key是value，还是会保留的。

**Examples:**

Example 1 (java):
```java
<chain name="chain1">
    <route>
        AND(r1, r2, r3)
    </route>
    <body>
        THEN(a, b, c);
    </body>
</chain>

<chain name="chain2">
    <route>
        AND(OR(r4, r5), NOT(r3))
    </route>
    <body>
        SWITCH(x).TO(d, e, f);
    </body>
</chain>
```

Example 2 (java):
```java
List<LiteflowResponse> responseList = flowExecutor.executeRouteChain(requestData, YourContext.class);
```

Example 3 (xml):
```xml
<chain name="chain1" namespace="n1">
    <route>
        AND(r1, r2, r3)
    </route>
    <body>
        THEN(a, b, c);
    </body>
</chain>

<chain name="chain2" namespace="n1">
    <route>
        AND(OR(r4, r5), NOT(r3))
    </route>
    <body>
        SWITCH(x).TO(d, e, f);
    </body>
</chain>

<chain name="chain3" namespace="n2">
    <route>
        r4
    </route>
    <body>
        WHEN(a,b);
    </body>
</chain>

<chain name="chain4" namespace="n2">
    <route>
        AND(r4,r5)
    </route>
    <body>
        IF(x, m, n);
    </body>
</chain>
```

Example 4 (java):
```java
List<LiteflowResponse> responseList = flowExecutor.executeRouteChain("n1", requestData, YourContext.class);
```

---

## 🍘动态刷新脚本

**URL:** https://liteflow.cc/pages/cbcb14/

**Contents:**
- 🍘动态刷新脚本

其实在平滑热刷新这章所描述的刷新整个规则已经包含了脚本的热刷新。

这里做一个摘用，你可以调用如下的代码进行脚本的热刷新：

**Examples:**

Example 1 (java):
```java
LiteflowMetaOperator.reloadScript(nodeId, script);
```

---

## 🗑卸载脚本

**URL:** https://liteflow.cc/pages/28ad17/

**Contents:**
- 🗑卸载脚本

LiteFlow提供了卸载脚本的接口，你可以这么使用：

此方法不仅会卸载编译好的script，也会在元数据中删除相应的节点。

**Examples:**

Example 1 (java):
```java
FlowBus.unloadScriptNode(String nodeId);
```

---

## 🥨启动不检查脚本

**URL:** https://liteflow.cc/pages/891f37/

**Contents:**
- 🥨启动不检查脚本

同启动时不检查规则一样，也是同样的配置，但要注意这个特性只有2.13.0(含)之后才有。

**Examples:**

Example 1 (properties):
```properties
liteflow.parse-mode=PARSE_ONE_ON_FIRST_EXEC
```

---

## 🐮启动时生命周期

**URL:** https://liteflow.cc/pages/ef098d/

**Contents:**
- 🐮启动时生命周期
- # 规则构造前后
- # 节点构造前后
- # 脚本引擎初始化后

LiteFlow在启动时提供了一些生命周期接口，开发者可以根据需要去实现它们，从而做到在启动的特定时机插入自己的逻辑。

这个生命周期发生在LiteFlow去构造Chain的时候。开发者只要实现如下接口，并注册到spring/solon的上下文中，就可以声明了。

这个生命周期发生在LiteFlow去构造Node的时候，开发者只要实现如下接口，并注册到spring/solon的上下文中，就可以声明了。

这个生命周期发生在脚本引擎初始化后（如果你有引入脚本插件的话），开发者只要实现如下接口，并注册到spring/solon的上下文中，就可以声明了。

请注意，这个engine对象在各个脚本插件下是不同的。需要强转下

对于Groovy / Aviator / JS(JDK) / Kotlin / Lua 这些脚本语言来说，由于都是采用JSR23的实现方式，这里的engine对象为javax.script.ScriptEngine。

对于JS(GraalJs)来说，这里的engine对象为org.graalvm.polyglot.Engine。

对于Python来说，这里的engine对象为org.python.util.PythonInterpreter。

对于QLExpress来说，这里的engine对象为com.ql.util.express.ExpressRunner。

对于Java(Janino) / Java(Liquor) 来说，由于他们都是通过静态类去执行，所以这里的engine对象没有，为null。

同一个生命周期声明多个并不会覆盖，而是会挨个执行。

**Examples:**

Example 1 (java):
```java
@Component
public class TestChainLifeCycle implements PostProcessChainBuildLifeCycle {
    @Override
    public void postProcessBeforeChainBuild(Chain chain) {
        //do something
    }

    @Override
    public void postProcessAfterChainBuild(Chain chain) {
        //do something
    }
}
```

Example 2 (java):
```java
@Component
public class TestNodeLifeCycle implements PostProcessNodeBuildLifeCycle {
    @Override
    public void postProcessBeforeNodeBuild(Node node) {
        //do something
    }

    @Override
    public void postProcessAfterNodeBuild(Node node) {
        //do something
    }
}
```

Example 3 (java):
```java
public class TestScriptInitLifeCycle implements PostProcessScriptEngineInitLifeCycle {
    @Override
    public void postProcessAfterScriptEngineInit(Object engine) {
        //do something
    }
}
```

---

## 💐复杂编排例子

**URL:** https://liteflow.cc/pages/5156b3/

**Contents:**
- 💐复杂编排例子
- # 复杂例子一
- # 复杂例子二
- # 总结

经过上面几小章，你是不是已经大致了解了LiteFlow该如何编排了呢？

这章我们结合以上几个章节，来看下复杂流程编排的例子。

我相信大多数人应该能看懂，但是如果你用子变量再优化的话，会更加清晰，上面的可以优化成：

如果你已经看懂上面这个例子，那我们再来看一个巨复杂的

这个表达式初看，我觉得一部分人会晕，括号都得数半天，当然如果你仔细研读的话，应该能看懂。

对于这种比较难以阅读的表达式来说，官方建议拆子流程或者拆子变量。下面我用拆子变量的方式优化下：

以上2个例子可在源码中的测试用例中找到，你可以运行并测试。

复杂案例一：com.yomahub.liteflow.test.complex.ComplexELSpringbootTest1

复杂案例二：com.yomahub.liteflow.test.complex.ComplexELSpringbootTest2

LiteFlow的规则表达式语法简单，但是却可以描绘出大多数编排场景。努力让你的规则最大程度的简化。

在实际场景中，如果遇到复杂编排，完全可以使用子流程或者子变量来简化你的整个规则。让你的规则优雅且更容易阅读！

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    THEN(
        A,
        WHEN(
            THEN(B, C),
            THEN(D, E, F),
            THEN(
                SWITCH(G).to(
                    THEN(H, I, WHEN(J, K)).id("t1"),
                    THEN(L, M).id("t2")
                ),
                N
            )
        ),
        Z
    );
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    item1 = THEN(B, C);
    item2 = THEN(D, E, F);
    item3_1 = THEN(H, I, WHEN(J, K)).id("t1");
    item3_2 = THEN(L, M).id("t2");
    item3 = THEN(SWITCH(G).to(item3_1, item3_2), N);
    
    THEN(
        A,
        WHEN(item1, item2, item3),
        Z
    );
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    THEN(
        A,
        SWITCH(B).to(
            THEN(D, E, F).id("t1"),
            THEN(
                C,
                WHEN(
                    THEN(
                        SWITCH(G).to(THEN(H, I).id("t2"), J),
                        K
                    ),
                    THEN(L, M)
                )
            ).id("t3")
        ),
        Z
    );
</chain>
```

Example 4 (xml):
```xml
<chain name="chain1">
    item1 = THEN(D, E, F).id("t1");
    
    item2_1 = THEN(
        SWITCH(G).to(
            THEN(H, I).id("t2"),
            J
        ),
        K
    );
    
    item2_2 = THEN(L, M);
    
    item2 = THEN(C, WHEN(item2_1, item2_2)).id("t3");
    
    THEN(
        A,
        SWITCH(B).to(item1, item2),
        Z
    );
</chain>
```

---

## 🍱多脚本语言混合共存

**URL:** https://liteflow.cc/pages/acba2c/

**Contents:**
- 🍱多脚本语言混合共存

LiteFlow支持了多脚本语言混合共存的特性。你完全可以在规则文件内用不同的脚本语言书写不同的逻辑。

当然有个前提：你使用了多个脚本，必须引入多个脚本对应的依赖，依赖选项在脚本语言种类有说过。

以上规则中，其中a,b,c为java组件，s1是groovy组件，s2是javascript组件，s3是python组件。

LiteFlow能非常方便的能进行混合编排，并且实现参数互通。

← 🍣脚本与Java进行交互 🌯文件脚本的定义→

**Examples:**

Example 1 (xml):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<flow>
    <nodes>
        <node id="s1" name="groovy脚本" type="script" language="groovy">
            <![CDATA[
                class Student {
                    int studentID
                    String studentName
                }

                Student student = new Student()
                student.studentID = 100301
                student.studentName = "张三"
                defaultContext.setData("student", student)

                def a = 3
                def b = 2
                defaultContext.setData("s1", a * b)
            ]]>
        </node>

        <node id="s2" name="js脚本" type="script" language="js">
            <![CDATA[
                var student = defaultContext.getData("student");
                student.studentID = 10032;
            ]]>
        </node>

        <node id="s3" name="python脚本" type="script" language="python">
            <![CDATA[
                a = 3
                s1 = defaultContext.getData("s1")
                defaultContext.setData("s1",s1*a)
            ]]>
        </node>
    </nodes>

    <chain name="chain1">
        THEN(a, s1, b, s2, c, s3);
    </chain>
</flow>
```

---

## 如何理解上下文以及请求参数？

**URL:** https://liteflow.cc/pages/e1e61f/

**Contents:**
- 如何理解上下文以及请求参数？
- # 为什么要这么设计呢？
- # 上下文和请求参数有什么区别
- # 上下文中的属性如何保证线程安全
- # 多上下文的使用场景

之前在上下文说明这一小章节已经阐述了上下文在LiteFlow框架中是非常重要的概念。

如果有些新手同学对上下文这一概念还不理解，可以看看这小章的说明。

LiteFlow所有的组件process方法都是无参无返回构造，组件之间的传递参数以及返回的数据都是通过上下文来进行操作的。

我们知道在java中调用方法，都是要通过方法名+参数进行调用的，要调用一个方法就必须提供这个方法所需的参数。A方法里调用B方法，等同于A方法强耦合了B方法。

而LiteFlow的核心特性在于编排，如果每个方法名和参数都不一样，就无法做到可替换，可更换顺序。所以必须把组件都设计成一样的模式，消除每个组件的差异性，才能进行编排。

LiteFlow的做法是设计成无参无返回模式，增加了上下文这一概念，业务组件所需要的参数从上下文取，所产出的结果也放到上下文中。

每一个请求会产生一个上下文对象，不同请求之间的上下文是隔离开来的。而每个请求结束后，当前的上下文会被销毁回收。

在LiteFlow中调用一个流程，经常会这么调用：

LiteFlow中请求初始参数和上下文不是一个东西。

初始请求参数代表这个流程开始调用时，从这个流程外部传入的参数，这个初始参数也是贯穿整个流程的，任何一个组件都可以用this.getRequestData()获取到。

上下文是用来存放组件之间产生的数据的，LiteFlow会去初始化这个上下文的class，形成一个全新的实例，在一开始，这个上下文里面是没有任何数据的，组件把执行完的结果数据放入，然后其他组件需要的时候再进行取出，同时链路的最终结果也应该放在上下文中，在组件中用this.getContextBean()获取。最终流程的response也能通过response.getContextBean()获取到。

前面说到，LiteFlow中请求初始参数和上下文不是一个东西。

所以，这些同学这么写，是把一个实例context单独作为了requestData，而this.getContextBean却是另外一个实例。

其实requestData可以是任何对象，只不过这里传的初始参数恰好是CustomContext类型的而已，如果你想取到这个初始参数的CustomContext对象，依然用this.getRequestData() 来获取。

然而有的同学就是想把初始参数包裹在上下文里面，怎么办，难道还专门在第一个组件里，把初始参数set进context里面吗？

LiteFlow其实在文档中也有提到，可以传入已经初始化好的Context。

其实这就是把初始参数和上下文揉到了一起的体现。

LiteFlow的官方建议还是将初始参数和上下文区分开比较好，理由有以下2点：

1.初始参数是不应该被更改的。而上下文里的数据可以随时被更改的。区分开来比较好

2.初始参数可以是任何结构对象，而上下文只是各个组件运行态时所需要的数据对象。如果初始化参数对象被耦合到上下文对象结构里，则从分层理念上来说，是过于耦合了，不利于扩展。

由于组件编排存在着并发性(WHEN)，那么上下文的某一个对象可能同时会被多个组件访问，那么这时候如何保证线程安全性以及一致性呢。

由于上下文对象是由使用者定义的，所以这个线程安全性需要由使用者来去处理。在问答中也有解释，跳转到相关问答。

LiteFlow支持在调用时传入多个上下文对象。很多小伙伴不明白这在什么场景使用。

有的时候通用组件会被复用到很多流程中去。而每个流程的上下文又是不一样的。那么你可以为这个通用组件单独定义一个上下文，然后每次调用，你都传入2个上下文，一个为业务上下文，一个为通用组件上下文。使上下文之间的结构分离，完成通用编排。

Slot是一个什么样的概念，在框架中起到什么样的作用？→

**Examples:**

Example 1 (java):
```java
flowExecutor.execute2Resp("chain1", requestArg, CustomContext.class);
```

Example 2 (java):
```java
CustomContext context = new CustomContext();
context.setName("xxxx");
LiteflowResponse response = flowExecutor.execute2Resp("chain1", context, CustomContext.class);
```

Example 3 (java):
```java
CustomContext context = this.getContextBean(CustomContext.class);
String name = context.getName();
```

Example 4 (java):
```java
CustomContext context = new CustomContext();
context.setName("xxxx");
LiteflowResponse response = flowExecutor.execute2Resp("chain1", null, context);
```

---

## 🧊异常

**URL:** https://liteflow.cc/pages/dc9bfe/

**Contents:**
- 🧊异常

通常在LiteFlow组件里如果往外抛出异常，流程会中断。除了在并行编排中设置ignoreError关键字以外。

往外抛出的异常会被最外层的执行器捕获，并被包装进LiteflowResponse对象中。

你可以在LiteflowResponse对象中通过以下方法来获取异常

如果你的业务中有获取异常Code的需求，则你自定义的异常需要实现LiteFlow提供的LiteFlowException接口：

如果你的业务抛出了实现了LiteFlowException接口的异常，你则可以在LiteflowResponse中获得message和code信息：

如果你的异常没实现LiteFlowException，code和message字段都为null。

**Examples:**

Example 1 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 初始参数, CustomContext.class);
if (!response.isSuccess()){
  Exception e = response.getCause();
}
```

Example 2 (java):
```java
public class YourException extends LiteFlowException {
	public YourException(String code, String message) {
		super(code, message);
	}
}
```

Example 3 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 初始参数, CustomContext.class);
if (!response.isSuccess()){
  Exception e = response.getCause();
  String code = response.getCode();
  String message = response.getMessage();
}
```

---

## 🪂性能表现

**URL:** https://liteflow.cc/pages/9bf839/

**Contents:**
- 🪂性能表现

LiteFlow绝大部分工作都是在启动时完成，包括解析规则，注册组件，组装元信息。而执行链路时几乎对系统没有额外的消耗。框架在设计之初就是为公司的核心业务量身打造，在性能表现问题上格外注意。所以也对核心代码进行了性能方面的优化。

实际表现中，LiteFlow执行效率很高，在公司级核心业务上面，50多个业务组件组成的链路，在实际压测中单点达到了1500的TPS，集群达到了1W以上的TPS，也经历过双11，明星顶流带货等大流量的考验。

虽然LiteFlow框架本身性能很好，但是整体执行效率却依赖实际业务组件的快慢，如果你的组件有大量的循环数据库请求IO，或者有bad sql，又或者有大量的rpc同步调用。那实际TPS也不会很高。但是这是业务组件的问题，而不是LiteFlow框架本身的性能问题。如果你的业务代码很糟糕，那么任何一个框架都无法提高整体系统的TPS/QPS，一个系统整体吞吐量的快慢，不是仅依靠某一款框架能改善的。这点希望大家能明白。

LiteFlow提供了一个实际业务的测试案例，地址为：

测试案例 (opens new window)

这个业务为一个价格计算引擎，有11个业务节点，业务逻辑丰富，只不过数据为mock，不走数据库IO。

基于这个Demo业务进行了压测，压测机器为mac m3 pro ，压测工具为apache jmeter 5.6，容器为springboot自带的tomcat，压测结果为：

---

## 🎡执行方法

**URL:** https://liteflow.cc/pages/20072e/

**Contents:**
- 🎡执行方法
- # 返回类型为LiteflowResponse
- # 返回类型为Future

你可以在Springboot/Spring体系中的任何被Spring上下文管理的类中进行注入FlowExecutor。

强烈建议先阅读如何理解上下文以及请求参数。

请参考FlowExecutor层面的线程池

**Examples:**

Example 1 (java):
```java
//第一个参数为流程ID，第二个参数为流程入参，后面可以传入多个上下文class
public LiteflowResponse execute2Resp(String chainId, Object param, Class<?>... contextBeanClazzArray)
//第一个参数为流程ID，第二个参数为流程入参，后面可以传入多个上下文的Bean
public LiteflowResponse execute2Resp(String chainId, Object param, Object... contextBeanArray)
```

---

## 🐳执行时生命周期

**URL:** https://liteflow.cc/pages/f6ae9e/

**Contents:**
- 🐳执行时生命周期
- # FlowExecutor执行前后
- # Chain执行前后

LiteFlow在执行时也提供了一些生命周期接口，开发者可以根据需要去实现它们，从而做到在执行的特定时机插入自己的逻辑。

这个生命周期发生在FlowExecutor对象执行规则的时候，每执行一次FlowExecutor就会调用一次。

开发者只要实现如下接口，并注册到spring/solon的上下文中，就可以声明了。

这个生命周期发生在Chain对象执行的时候，每执行一次Chain就会调用一次。

开发者只要实现如下接口，并注册到spring/solon的上下文中，就可以声明了。

这个和FlowExecutor执行生命周期还是有区别的。比如执行以下规则mainChain：

那么每执行一次，FlowExecutor的生命周期只会被触发1次，而Chain的生命周期会被触发2次，分别是mainChain执行前后和subChain执行前后。

通过Slot对象其实可以拿到上下文，错误，Step很多元信息。

← 🐮启动时生命周期 🍌本地规则文件监听→

**Examples:**

Example 1 (java):
```java
@Component
public class TestFlowExecuteLifeCycle implements PostProcessFlowExecuteLifeCycle {
    @Override
    public void postProcessBeforeFlowExecute(String chainId, Slot slot) {
        //do something
    }

    @Override
    public void postProcessAfterFlowExecute(String chainId, Slot slot) {
        //do something
    }
}
```

Example 2 (java):
```java
@Component
public class TestChainExecuteLifeCycle implements PostProcessChainExecuteLifeCycle {
    @Override
    public void postProcessBeforeChainExecute(String chainId, Slot slot) {
        //do something
    }

    @Override
    public void postProcessAfterChainExecute(String chainId, Slot slot) {
        //do something
    }
}
```

Example 3 (xml):
```xml
<chain id="mainChain">
    THEN(a, b, subChain);
</chain>

<chain id="subChain">
    WHEN(c, d);
</chain>
```

---

## 🎃捕获异常表达式

**URL:** https://liteflow.cc/pages/f53b51/

**Contents:**
- 🎃捕获异常表达式
- # 基本用法
- # 搭配循环使用

LiteFlow提供了捕获异常的表达式组合。

上述语法表示，如果a组件出现异常并抛出，则不会执行b组件，会直接执行c组件。

在c组件中，可以通过this.getSlot().getException()来获取异常。

同时，当用了CATCH表达式之后，即便在CATCH包裹的组件有异常抛出，整个流程返回的LiteflowResponse中的isSuccess方法仍然为true，getCause中也没有任何的Exception。如果你写过java程序，应该会对这样的机制很容易理解。因为异常已经被你自己处理掉了。

上面这段表达式不管a,b有没有抛出异常，最终总会执行c。如果a抛出异常，那么最终执行链路就为a==>c

CATCH表达式和循环表达式搭配起来使用，还能做出java中continue的效果，比如：

如果你希望在b组件中达成某一个条件就不执行c，继续循环，那么你可以借助CATCH语法，只要在b组件中往外抛一个异常即可。

我相信这种用法对于写程序的同学来说，应该不用过多解释。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    CATCH(
        THEN(a,b)
    ).DO(c)
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    THEN(
        CATCH(
            THEN(a,b)
        ),
        c
    )
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    FOR(x).DO(
        CATCH(
            THEN(a,b,c)
        )
    )
</chain>
```

---

## 🌯数据上下文的定义和使用

**URL:** https://liteflow.cc/pages/501abf/

**Contents:**
- 🌯数据上下文的定义和使用
- # 默认上下文
- # 自定义上下文
- # 多上下文v2.8.0+
- # 利用超类获取上下文v2.12.2+
- # 利用别名获取上下文v2.12.0+

LiteFlow提供了一个默认的数据上下文的实现：DefaultContext。这个默认的实现其实里面主要存储数据的容器就是一个Map。

你可以通过DefaultContext中的setData方法放入数据，通过getData方法获得数据。

DefaultContext虽然可以用，但是在实际业务中，用这个会存在大量的弱类型，存取数据的时候都要进行强转，颇为不方便。所以官方建议你自己去实现自己的数据上下文。

你可以用你自己的任意的Bean当做上下文进行传入。LiteFlow对上下文的Bean没有任何要求。

自己定义的上下文实质上就是一个最简单的值对象，自己定义的上下文因为是强类型，更加贴合业务。

传入之后， LiteFlow会在调用时进行初始化，给这个上下文分配唯一的实例。你在组件之中可以这样去获得这个上下文实例：

关于组件之中还可以获得哪些默认的参数，请参考普通组件。

LiteFlow在新版本中支持了多上下文，在执行的时候同时初始化你传入的多个上下文。在组件里也可以根据class类型很方便的拿到。

你可以像这样进行传入（看不全的可以往后拉）：

从上面的例子可以得知，获取上下文可以通过对象的class来取到。

但是在有些场景中，尤其是要定义一些通用组件的时候。用特定对象的class来取就有些不合适了。这就显得不是很通用。

为了适配通用组件这个场景。LiteFlow支持了利用超类来获得上下文。

例如，你定义了一个OrderContext:

那么你在某些通用组件里可以通过它的超类BaseContext类型来获取到上下文:

如果在一个链路请求中有多个上下文，并且都是某一个超类的子类，你再用超类去获取，只会获取到第一个上下文。这点请注意。

**Examples:**

Example 1 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 流程初始参数, CustomContext.class);
```

Example 2 (java):
```java
@LiteflowComponent("yourCmpId")
public class YourCmp extends NodeComponent {

	@Override
	public void process() {
		CustomContext context = this.getContextBean(CustomContext.class);
		//或者你也可以用这个方法去获取上下文实例，如果你只有一个上下文，那么和上面是等价的
		//CustomContext context = this.getFirstContextBean();
		...
	}
}
```

Example 3 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", 流程初始参数, OrderContext.class, UserContext.class, SignContext.class);
```

Example 4 (java):
```java
@LiteflowComponent("yourCmpId")
public class YourCmp extends NodeComponent {

	@Override
	public void process() {
		OrderContext orderContext = this.getContextBean(OrderContext.class);
		UserContext userContext = this.getContextBean(UserContext.class);
		SignContext signContext = this.getContextBean(SignContext.class);
		
		//如果你只想获取第一个上下文，第一个上下文是OrderContext，那么也可以用这个方法
		//OrderContext orderContext = this.getFirstContextBean();
		...
	}
}
```

---

## 🌯文件脚本的定义

**URL:** https://liteflow.cc/pages/f7acfd/

**Contents:**
- 🌯文件脚本的定义
- # 相对位置的文件脚本v2.6.4+
- # 绝对位置的文件脚本v2.9.7+

LiteFlow支持脚本文件的定义。你除了可以把脚本内容写在配置文件中，也可以写在文件中。如果大的脚本就推荐写在文件中。毕竟IDE对文件的语法高亮和代码提示做的也相对友好。编写脚本会更加方便。

你可以这样定义（这里以xml文件格式举例）:

LiteFlow支持脚本文件的绝对路径，你可以这样定义（这里以xml文件格式举例）:

← 🍱多脚本语言混合共存 🍘动态刷新脚本→

**Examples:**

Example 1 (xml):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<flow>
    <nodes>
        <node id="s1" name="普通脚本" type="script" file="xml-script-file/s1.groovy"/>
        <node id="s2" name="选择脚本" type="switch_script" file="xml-script-file/s2.groovy"/>
        <node id="s3" name="条件脚本" type="switch_script" file="xml-script-file/s3.groovy"/>
    </nodes>

    <chain name="chain1">
        THEN(a, b, c, s1)
    </chain>

    <chain name="chain2">
        THEN(d, IF(s3, b, c));
    </chain>
</flow>
```

Example 2 (xml):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<flow>
    <nodes>
        <node id="s1" name="普通脚本" type="script" file="/data/liteflow/s1.groovy"/>
        <node id="s2" name="选择脚本" type="switch_script" file="/data/liteflow/s2.groovy"/>
        <node id="s3" name="条件脚本" type="switch_script" file="/data/liteflow/s3.groovy"/>
    </nodes>

    <chain name="chain1">
        THEN(a, b, c, s1)
    </chain>

    <chain name="chain2">
        THEN(d, IF(s3, b, c));
    </chain>
</flow>
```

---

## 🍞构造Chain

**URL:** https://liteflow.cc/pages/cd0445/

**Contents:**
- 🍞构造Chain
- # 构建一个Chain
- # 使用动态组装EL表达式构建Chain

你可以像以下那样构造一个chain，由于和规则定义的没冲突。你也可以和规则文件结合起来用。当build的时候，如果没有则添加，如果有则修改。

值得提一下的是，由于用构造模式是一个链路一个链路的添加，如果你用了子流程，如果chain1依赖chain2，那么chain2要先构建。否则会报错。

但是经过上面几章的学习，其实一个EL表达式完全可以表示一个复杂的流程，即便不能也可以用子变量来优化流程。

从2.11.1版本开始，您可以根据实际需求动态地构建EL表达式，而不仅仅限于使用固定的字符串。如下例所示：

请注意，上述示例仅用于演示目的，实际使用时，您需要根据具体的业务逻辑和数据结构来组装EL表达式，并将其应用于相应的Chain。

如果使用动态组装的EL表达式，需要引入额外依赖。具体请参考构造EL。

**Examples:**

Example 1 (java):
```java
LiteFlowChainELBuilder.createChain().setChainName("chain2").setEL(
  "THEN(a, b, WHEN(c, d))"
).build();
```

Example 2 (java):
```java
// 动态组装el表达式
ELWrapper el = ELBus.then("a", "b", ELBus.when("c", "d"));
LiteFlowChainELBuilder.createChain().setChainName("chain2").setEL(
	// 输出el表达式
    el.toEL()
).build();
```

---

## 🏖概念以及介绍

**URL:** https://liteflow.cc/pages/ec1ac4/

**Contents:**
- 🏖概念以及介绍

在之前的介绍中，LiteFlow执行一个规则主要是依赖FlowExecutor来执行，需要指定一个规则Id。

但是在有些场景中，使用者定义若干个规则，具体执行哪个规则事先并不知道。需要依靠入参去动态判断执行某一个或多个规则。

在之前的介绍中，除非你定义一个主规则。通过SWITCH去判断，来执行哪个子规则。其实也不是不可以。但是本质上还是执行一个规则。只不过通过这个主规则把子规则给串起来而已。并且想要同时执行多个规则，也是需要刻意去编排的。初学者并不知道如何去比编排这样的规则场景。

为此，LiteFlow推出了决策路由特性，也就是说，现在LiteFlow支持不指定规则，在所有规则中通过对决策表达式的判断来动态执行规则。符合决策表达式的规则则执行，不符合的不予以执行。

---

## 🍡步骤信息

**URL:** https://liteflow.cc/pages/e5ed0d/

**Contents:**
- 🍡步骤信息
- # 基本应用
- # 设置自定义步骤信息v2.13.0+

LiteFlow为执行的过程提供了详细的步骤信息。

获取一条流程执行的步骤信息是通过LiteflowResponse对象来获取的：

获得Map返回值的那个方法，如果有多个相同的组件，那么以上这个方法获得的Map中这个组件id的value是最终的那个步骤信息。

而获得Queue<CmpStep>这个返回值的方法，返回值里包含了所有的步骤信息，相同的组件在规则里定义n次，那么这里也有n个步骤。

在CmpStep这个对象里，你可以通过以下方法获得你要的数据：

如果你的某一个组件抛出了异常，在默认配置情况下，流程会中断。那么response.getCause()和相应组件步骤里的exception都是一致的。且没执行的组件不会有相应步骤信息。

这样你就可以在LiteflowResponse对象中拿到每个step对象中拿到stepData信息：

这个特性的意义在于，你可以监控上下文中的某一个数据在经过每个组件时的变化数据。比如上下文中一个count属性，每经过一个组件+1。

那么你最终拿到的step队列中，你可以清楚的看到当时这个step中的count属性数据是多少。

**Examples:**

Example 1 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("chain1", "初始参数", CustomContext.class);
Map<String, CmpStep> stepMap = response.getExecuteSteps();
//或者你也可以通过以下的语句来获得一个步骤队列
Queue<CmpStep> stepQueue = response.getExecuteStepQueue();
```

Example 2 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		this.setStepData("step_a");
	}
}
```

Example 3 (java):
```java
response.getExecuteStepQueue().forEach(
        cmpStep -> System.out.println(cmpStep.getStepData())
);
```

---

## 🫐活跃规则保活策略

**URL:** https://liteflow.cc/pages/57a1fd/

**Contents:**
- 🫐活跃规则保活策略

如果你的系统有非常庞大的规则数目(上万条乃至数十万条规则)，推荐开启活动规则保活策略。

这个策略会在过多的规则下只维持前N条最活跃的规则缓存，而不活跃的规则会被暂时的从系统中卸载掉。被卸载掉的规则，再次被调用时的第一次会重新编译加入活跃的队列。

整个策略使用者无感，默认这个策略的开关在框架中是关闭的，这个策略的打开方式为：

**Examples:**

Example 1 (properties):
```properties
# 是否开启保活策略
liteflow.chain-cache.enabled=true
# 保持活跃chain的数目，默认为10000
liteflow.chain-cache.capacity=10000
# 模式一定得为PARSE_ONE_ON_FIRST_EXEC
liteflow.parse-mode=PARSE_ONE_ON_FIRST_EXEC
```

---

## 🎢流程入参

**URL:** https://liteflow.cc/pages/563b67/

**Contents:**
- 🎢流程入参

在实际使用中，很多同学会对流程入参这一概念有所疑惑。

在一个流程中，总会有一些初始的参数，比如订单号，用户Id等等一些的初始参数。这时候需要通过以下方法的第二个参数传入：

请注意，这个流程入参，可以是任何对象，一般生产业务场景下，你可以把自己封装好的Bean传入。

在这里，流程入参可以是任何对象，如果你把数据上下文的实例传入了，并不意味着你拿到的相同类型的数据上下文中就是有值的。因为这2个对象根本就是2个实例。 流程入参只能通过this.getRequestData()去拿。

如果你真实目的是想提前传入初始化好的上下文对象，可以参考用初始化好的上下文传入这一章节。

← 🎡执行方法 🎈LiteflowResponse对象→

**Examples:**

Example 1 (java):
```java
public LiteflowResponse execute2Resp(String chainId, Object param, Class<?>... contextBeanClazzArray)
```

Example 2 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		YourBean requestBean = this.getRequestData();
	}
}
```

---

## 🪁测试用例

**URL:** https://liteflow.cc/pages/81cdce/

**Contents:**
- 🪁测试用例

项目提供了丰富的测试用例，截止到目前版本，项目内一共有1800多个测试用例。几乎涵盖了文档内所有提到的功能点和场景。

强烈建议想了解LiteFlow的同学可以去看看测试用例来学会如何在细节点上的配置和使用

---

## 🪶用初始化好的上下文传入

**URL:** https://liteflow.cc/pages/f05ed6/

**Contents:**
- 🪶用初始化好的上下文传入

你可能注意到了，在执行器执行流程的时候，需要传入流程入参和上下文class定义(一个或多个)两种参数。

对于数据上下文而言，初始化动作是由框架来处理的。也就是说，在你执行第一个组件时，上下文对象里面是没有用户数据的。而你的流程入参是用this.getRequestData()获取的，这部分不包含在上下文里面。

如果你需要将流程入参放入上下文，那这一动作是需要你自己来完成的。

LiteFlow允许用户传入一个或多个已经初始化好的bean作为上下文，而不是传入class对象。

在拿到FlowExecutor之后，你可以像如下一样，传入已经初始化好的bean作为上下文（当然也支持多上下文，这里只演示单上下文）：

如果你这样调用，等于你的上下文中已经初始化好了一个一些数据。从某种意义上来说，这已经等同于流程入参了，所以使用这个的时候，你完全可以不传流程入参了。

框架并不支持上下文bean和class混传，你要么都传bean，要么都传class。

← 🌯数据上下文的定义和使用 🥨给上下文设置别名→

**Examples:**

Example 1 (java):
```java
OrderContext orderContext = new OrderContext();
orderContext.setOrderNo("SO11223344");
LiteflowResponse response = flowExecutor.execute2Resp("chain1", null, orderContext);
```

---

## 🪴用表达式获取上下文参数

**URL:** https://liteflow.cc/pages/57e00b/

**Contents:**
- 🪴用表达式获取上下文参数
- # 介绍
- # 用表达式获取参数
- # 用表达式设置参数

如果你看过上下文参数注入，一定注意到了，使用上下文参数注入的方式可以让组件和上下文解耦。

但是上下文参数注入只限于声明式组件使用。有没有通用一点的类似机制呢，使得普通继承式组件也能用？

这就是这个章节带来的表达式取参的功能，这个功能，无论在继承式还是声明式的组件里都可以使用，甚至于在脚本组件里都可以使用。这是真正意义上的通用特性。

我们在组件里面写业务，首先肯定就是要拿到上下文，在声明式组件里通常的写法为：

以上代码，我们从上下文中拿到了上下文，并且从上下文中拿到了userCode这个参数。

这样写的好处是直观，但是缺点是，如果这是一个公用的组件，那么这个组件就强绑定YourContext这个对象了。虽然在LiteFlow中，你也可以通过上下文继承的方式或者多上下文的方式来解决。但是都是曲线救国。

现在这个组件就和你的上下文彻底解耦了，你的上下文中只要有userCode这个属性的，那都可以被取出来。

上述表达式，意思是取出上下文中member这个对象中的code字段的值。

如果有多个上下文，表达式也会匹配最合适的那个进行取出，你无需关心有多少个上下文，上下文是什么。

但是，你需要注意有一种特例，那就是你在多个上下文中拥有相同的字段，比如现在这个流程中传入了3个上下文：

这时候的this.getContextValue("code");取出的到底是哪一个呢？

LiteFlow框架在这种情况下 ，只会返回第一个匹配到的字段的值。如果你需要精确指定是某个Context下的code。则需要在表达式中加上上下文的前缀：

这个前缀默认是你的上下文的类名的首字母小写。但是你也可以改变它，它受@ContextBean这个注解的影响：

那么你就不能用authContext这个前缀来取了，而是通过authCtx来取：

你除了可以用点操作符，对于常用的List，Map，数组形式也有支持：

除了可以用表达式取出上下文中的参数，在设置参数时，同样可以用表达式：

以上代码就是从上下文中拿到name这个值，并且调用上下文中的setDesc方法，把值设置进去。

同样的，如果有多个上下文的时候，完全不用关心name是从哪个上下文中来，setDesc是哪个上下文中的方法。

值得注意的是，this.setContextValue的定义是：

所以当你的方法有多个参数的时候，也是可以支持的。

同样的，你也可以用点操作符给更深次的对象进行赋值，比如：

同样的，你想调用指定上下文中的方法，也可以用上下文的前缀加以指定：

**Examples:**

Example 1 (java):
```java
@Component("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		YourContext context = this.getContextBean(YourContext.class);
        String userCode = context.getUserCode();
		...
	}
}
```

Example 2 (java):
```java
@Component("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		String userCode = this.getContextValue("userCode");
		...
	}
}
```

Example 3 (java):
```java
@Component("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		String code = this.getContextValue("member.code");
		...
	}
}
```

Example 4 (java):
```java
public class OrderContext{
    private String code;
    ...
}
```

---

## 🪃直接执行EL规则

**URL:** https://liteflow.cc/pages/55f4bc/

**Contents:**
- 🪃直接执行EL规则

LiteFlow的规则是定义在配置文件里，在本地它以xml的形式存在。

但是如果是很简单的表达式，你也可以不定义在本地文件中，直接传入规则也是可以的：

execute2RespWithEL这个方法和execute2Resp类似，只不过把第一个参数从chainId换成了规则EL。这里对其他的重载方法不再赘述。

值得注意的是，LiteFlow内部实现上，并没有每次请求去创建一个chain。如果多次请求的表达式MD5指纹是同一个时，只会创建一个chain，并且这个chain会由LiteFlow来托管，开发者完全不用关心。

但是如果出现每次请求的传入的表达式都不一样这种极端的情况，会引起托管chain的数量的暴增。所以要尽量避免这种情况，或者也可以考虑结合活跃规则保活策略这个特性来做。

← 🎈LiteflowResponse对象 🌭脚本语言介绍→

**Examples:**

Example 1 (java):
```java
LiteflowResponse response = flowExecutor.execute2RespWithEL("THEN(a, b, c)", requestData, CustomContext.class);
```

---

## 🍥简单监控

**URL:** https://liteflow.cc/pages/e59f3a/

**Contents:**
- 🍥简单监控

LiteFlow提供了简单的监控，目前只统计一个指标：每个组件的平均耗时

默认每5分钟会打印一次(可以自己调整)，并且是根据耗时时长倒序排的。

← 🍿自定义组件执行器 🧉XML的DTD→

**Examples:**

Example 1 (properties):
```properties
#是否启用监控
liteflow.monitor.enable-log=false
#监控队列的大小
liteflow.monitor.queue-limit=200
#监控延迟多少毫秒打印
liteflow.monitor.delay=300000
#监控每隔多少毫秒打印
liteflow.monitor.period=300000
```

---

## 🍣脚本与Java进行交互

**URL:** https://liteflow.cc/pages/d861c8/

**Contents:**
- 🍣脚本与Java进行交互
- # 和上下文进行交互
- # 自定义上下文引用名称
- # 元数据获取方式之一
- # 元数据获取方式之二
- # 和自定义的JavaBean进行交互
- # 直接注入方法

这章只适用于groovy,js,python,qlexpress,lua,aviator这6种脚本语言。

v2.11.0新增的Java脚本语言和Java类的交互方式在Java脚本引擎中已做了详细说明。

因为LiteFlow组件与组件之间的数据交互都在上下文中，所以在脚本语言中，你可以通过你定义数据上下文的className的驼峰形式来获取数据。

比如你的上下文类叫OrderContext，那么脚本中的就用orderContext这个关键字来获取数据或调用方法。

如果你是多上下文，同样的，你也可以在脚本中用多个上下文来获取数据或调用context内部的逻辑方法。

比如，你想获取UserContext中的userName对象。你可以这样写（以下以groovy作例子）：

上文提到，在脚本中默认的上下文引用规则为上下文类的simpleClassName，比如你的上下文为UserContext，那么脚本就用userContext去引用。

可以。LiteFlow从2.10.0版本开始支持这个功能，如果你不想用userContext来引用，那么只需加一个@ContextBean的注解即可完成：

这样定义后，那么脚本中，你就可以用userCtx关键字去引用上下文了。

在脚本中可以用通过_meta关键字获取元数据，可以通过_meta.xxx获取元数据，元数据里包括：

你也可以通过_meta.cmp来获取当前的组件对象。

你可以理解_meta.cmp为this关键字，那既然如此，那this可以获取的资源，在脚本里也可以，比如想获取tag就是_meta.cmp.getTag()，想通过别名获取上下文就是_meta.cmp.getContextBean("xxx")。

LiteFlow从v2.9.0开始支持在脚本中注入你自己定义的任何java对象。

在spring体系中，你只需要在你需要注入的java对象上使用@ScriptBean标注，即可完成注入。

以上例子中，脚本里就可以直接使用demo关键字来调用getDemoStr1()和getDemoStr2()方法了。

我们在LiteFlow 2.9.5版本支持了@ScriptBean的指定方法和排除方法功能。

如果你想指定这个类中的某2个方法可以被脚本访问到，你可以这样写：

这样你在脚本中只能访问test1和test2方法。

如果你想指定这个类中的某些访问无法被脚本访问到，你可以这样写：

这样你在脚本中只能访问到test1方法了。

需要注意的是，java对象在spring体系中一定要注册进上下文，如果不注册进上下文，光加@ScriptBean注解也是没用的。

在非spring体系下面，如果你要把自己的定义的java对象注入脚本，则需要手动写代码（最好在启动应用的时候）：

如果你有一个java类，里面有100个方法，而我只想暴露其1个给脚本使用，用@ScriptBean可能会把整个bean都暴露出去，有没有方法呢？

有。LiteFlow从2.9.5开始加入了@ScriptMethod注解，在方法上进行标注：

这样，你就可以在脚本中用demo.getDemoStr1()来调用到相应的java方法了。

当然这里的前提同样是：java对象在spring体系中一定要注册进上下文，如果不注册进上下文，光加@ScriptMethod注解也是没用的。

← 🥠Kotlin脚本引擎 🍱多脚本语言混合共存→

**Examples:**

Example 1 (xml):
```xml
<node id="s1" name="普通脚本" type="script">
    <![CDATA[
        //你可以这样定义
        def name = userContext.userName;
        //也可以这样定义，如果你对userName有getter方法的话
        def name = userContext.getUserName();
        //同理，你可以调用数据上下文中的任意方法
        userContext.doYourMethod();
    ]]>
</node>
```

Example 2 (java):
```java
@ContextBean("userCtx")
public class UserContext {
    ...
}
```

Example 3 (java):
```java
@Component
@ScriptBean("demo")
public class DemoBean1 {

    @Resource
    private DemoBean2 demoBean2;

    public String getDemoStr1(){
        return "hello";
    }

    public String getDemoStr2(String name){
        return demoBean2.getDemoStr2(name);
    }
}
```

Example 4 (java):
```java
@Component
@ScriptBean(name = "demo", includeMethodName = {"test1","test2"})
public class DemoBean3 {

    public String test1(String name){
        ...
    }

    public String test2(String name){
        ...
    }

    public String test3(String name){
        ...
    }
}
```

---

## 🌭脚本语言介绍

**URL:** https://liteflow.cc/pages/38c781/

**Contents:**
- 🌭脚本语言介绍

在前面几个章节中，我们介绍了LiteFlow是用EL表达式来驱动组件执行顺序的。

可见组件是LiteFlow的最小逻辑执行单元。

而组件在前面几章的介绍中，都是需要你自己去定义类的。而定义类通常用于相对固定的逻辑，EL表达式能够即时调整，但是定义成类的组件中的逻辑还是要重启系统才能调整。

但是在实际业务场景中，有的场景需要实时的去调整小部分逻辑，那怎么办呢。

这就需要LiteFlow提供的脚本组件特性了。

脚本组件，顾名思义就是不再需要你去用类去定义组件了，而是用脚本来定义组件。而脚本也是可以被即时调整的。

脚本组件也是LiteFlow框架中非常重要且极具有特色的一个特性，利用EL+脚本组件，你可以做出一套极其灵活的系统。无论是执行顺序，还是关键逻辑，均可进行热刷新。

LiteFlow在启动时就对脚本进行了预编译，虽然脚本的执行性能肯定比不过原生java，但是性能不会差太多，因为脚本方便且灵活可以热刷，这是java类所做不到的。

LiteFlow中目前支持的脚本语言多达8种。下面一小章会大致说下每一种脚本语言该如何运用。

虽然脚本组件拥有可热刷新的特性，但是依旧不推荐把一个系统里所有的逻辑都写成脚本组件，因为并不是所有的逻辑都需要热修改。

推荐把需要灵活经常变的逻辑写成脚本组件，固定不变的逻辑还是用java类来写。java类+脚本组件+EL的组合是官方最为推荐的方式。

← 🪃直接执行EL规则 ☕️Java脚本引擎→

---

## 🧁自定义请求Id

**URL:** https://liteflow.cc/pages/47e8f5/

**Contents:**
- 🧁自定义请求Id
- # 按照自己的规则生成
- # 传入已有的requestId/traceId
- # 给组件中的日志也加上请求ID前缀

LiteFlow支持让你自定义你的请求Id。

大家在执行一条流程的时候，往往可以在日志信息中看到以下类似的信息：

其中日志主体中最前面的就是RequestId，一个请求中的requestId都是相同的，方便你进行日志查找。

这个requestId的形式也是可以自定义的。你可以按照自己的规则生成，也可以传入本来已有的TraceId来和系统做集成。

你只需要要声明一个类，然后实现RequestIdGenerator接口即可：

然后在LiteFlow的配置文件里声明下你这个类即可：

一般情况下，LiteFlow有自己默认的Id生成规则。所以大多数情况下你并不需要去特别自定义这个Id生成器。

LiteFlow在v2.10.5版本中对于这个特性给予了支持。在FlowExecutor进行调用的时候，你可以调用如下方法来传入一个已有的requestId。

如果有小伙伴用了TraceId的框架，可以把TraceId通过以下这种方式进行传入：

那么，这个链路中所有的框架日志前，都会带有[T001234]这个传入的ID了。

值得一提的是，LiteFlow还提供了一个日志包装类。只要你在组件中把slf4j的日志声明换成如下形式，那么你在组件中自己打出的日志也会带有请求ID前缀。

其中LFLog这个类是继承自slf4j的Logger类的，所以它的使用方式和Logger是完全一致的。

如果在一个链路中相同请求的日志都拥有同一个请求ID，那么对于定位问题来说，会很方便。推荐大家使用此特性。

**Examples:**

Example 1 (text):
```text
2022-07-03 11:15:00.196  INFO 71275 --- [           main] com.yomahub.liteflow.flow.element.Node   : [067a0baa6d434de3a8ccafa4b1506562]:[O]start component[a] execution
2022-07-03 11:15:00.204  INFO 71275 --- [           main] com.yomahub.liteflow.flow.element.Node   : [067a0baa6d434de3a8ccafa4b1506562]:[O]start component[b] execution
2022-07-03 11:15:00.218  INFO 71275 --- [lf-when-thead-0] com.yomahub.liteflow.flow.element.Node   : [067a0baa6d434de3a8ccafa4b1506562]:[O]start component[c] execution
2022-07-03 11:15:00.220  INFO 71275 --- [lf-when-thead-1] com.yomahub.liteflow.flow.element.Node   : [067a0baa6d434de3a8ccafa4b1506562]:[O]start component[d] execution
2022-07-03 11:15:00.220  INFO 71275 --- [           main] com.yomahub.liteflow.slot.Slot           : [067a0baa6d434de3a8ccafa4b1506562]:CHAIN_NAME[chain1]
a<1>==>b<0>==>c<0>==>d<0>
2022-07-03 11:15:00.221  INFO 71275 --- [           main] com.yomahub.liteflow.slot.DataBus        : [067a0baa6d434de3a8ccafa4b1506562]:slot[0] released
```

Example 2 (java):
```java
public class CustomRequestIdGenerator implements RequestIdGenerator {

    @Override
    public String generate() {
        return System.nanoTime();
    }
}
```

Example 3 (properties):
```properties
liteflow.request-id-generator-class=com.yomahub.liteflow.test.requestId.config.CustomRequestIdGenerator
```

Example 4 (java):
```java
LiteflowResponse response = flowExecutor.execute2RespWithRid("chain1", arg, "T001234", YourContext.class);
```

---

## 🪶虚拟线程

**URL:** https://liteflow.cc/pages/f23d3d/

**Contents:**
- 🪶虚拟线程

当你的JDK为21及以上时。框架内所有的异步线程将转化为虚拟线程。虚拟线程在处理高IO场景时，有着超高的优势。

如果JDK21以上你还想使用普通线程，框架也提供了一个开关，只需要把以下值设为false即可。

**Examples:**

Example 1 (properties):
```properties
# 默认为true
liteflow.enable-virtual-thread=false
```

---

## 💧说明

**URL:** https://liteflow.cc/pages/3a3b69/

**Contents:**
- 💧说明

在LiteFlow中，所有和异步运行有关的，都和线程池有关。

框架提供了多个线程池有关的参数，关键字以及自定义策略。本章将阐述线程池在所有的异步场景中的用法。

从2.13.0开始，框架中的线程池模型设计和之前的版本有较大的差异性，所以此章只适用于2.13.0之后的版本。

← 🥨启动不检查脚本 🐋FlowExecutor层面的线程池→

---

## 🍄说明

**URL:** https://liteflow.cc/pages/16eca9/

**Contents:**
- 🍄说明

LiteFlow在2.8.X版本中设计了非常强大的规则表达式。一切复杂的流程在LiteFlow表达式的加持下，都异常丝滑简便。

你只需要很短的时间即可学会如何写一个很复杂流程的表达式。

---

## 说明

**URL:** https://liteflow.cc/pages/6e4d15/

**Contents:**
- 说明

组件参数是指给组件编排中设置特定的参数。这些参数能在组件中能被轻易取出来参与逻辑运算。

LiteFlow能给组件设置参数的关键有三个，分别为tag,data和bind，它们做的事都是设置参数，但是在各自的场景上又略微有不同。以下篇幅会分别介绍。

---

## 🍄说明

**URL:** https://liteflow.cc/pages/631fa1/

**Contents:**
- 🍄说明

这章是一个快速入门的指引，帮助你用最快的时间去立马体验LiteFlow。

大家可以根据自己的实际环境从下面的Hello World里选择一种。

建议跟着文档操作一遍。你会初步感受到LiteFlow的优雅之处。

← 🌱Spring的支持度 🌿Springboot场景安装运行→

---

## 🍄说明

**URL:** https://liteflow.cc/pages/b70ec8/

**Contents:**
- 🍄说明

LiteFlow有诸多配置项，但在大多数情况下，你都不是必须得配置，因为系统有默认值。

如果你不明白此配置项是干什么用的，那么希望不要改变其默认值。

你也可以跳过此大章节，继续看下面的，如果碰到某个配置项的意义时，再来查阅此大章节。

以下三章所涵盖的配置项完全一样，只是在不同的架构环境下表现形式不同，为了方便你查看，可以选择你所熟悉的章节进行查看。

← 🌵其他场景安装运行 🌿Springboot下的配置项→

---

## 🍄说明

**URL:** https://liteflow.cc/pages/90b2a5/

**Contents:**
- 🍄说明

上面的几章节说明了，规则文件如何配置，如何定义组件，如何撰写规则。

相信你已经结合Hello World章节做了初步的尝试。

执行器是一个流程的触发点，你可以在代码的任意地方用执行器进行执行流程。

← 🪴用表达式获取上下文参数 🎡执行方法→

---

## 🍄说明

**URL:** https://liteflow.cc/pages/9aa85a/

**Contents:**
- 🍄说明

之前的章节讲述的是通过规则文件去构造流程。

LiteFlow也支持用代码去构造流程，你可以不用写xml/json/yaml的规则文件，ruleSource不用去定义。完全用代码去构建。

事实上，LiteFlow的规则无论是什么格式的，最终底层也是由构造链去构造的。

有些规则并不是在项目启动时就确定的。你可以通过构造模式，以代码形式的方式去动态构造一条链路，也可以去替换一条链路。

LiteFlow设计了非常简单的构造方法链式API，让你可以很轻松的构造一条链路。

并且，这一切同规则文件一样，都是支持平滑热刷新的，你完全不必担心在高并发时更换流程会造成链路错乱的问题。关于平滑热刷新，可以参考平滑热刷新。

---

## ⏱️超时控制语法

**URL:** https://liteflow.cc/pages/fd5984/

**Contents:**
- ⏱️超时控制语法
- # 使用方法
- # 注意事项

LiteFlow支持使用关键字对流程进行超时控制。

使用 maxWaitSeconds,maxWaitMilliseconds 关键字可对任意的组件、表达式、流程进行超时控制。

maxWaitSeconds后面传的是秒数，maxWaitMilliseconds后面传的是毫秒数。使用方式都一样。

maxWaitSeconds和maxWaitMilliseconds 传入一个 int 类型的整数表示最大等待秒数/毫秒数，使用如下方法设置最大超时等待时间。

如果 THEN 使用了超时控制，其内部直属的 FINALLY 不受超时控制。

组件 b 是不受超时控制的。但如果 FINALLY 不是设置超时的 THEN 所直属的，则仍受超时控制。

除WHEN外，若某个关键字后续存在多个连续操作，则maxWaitSeconds必须放在完整语义的最后。。

必须得到完整语义后再设置超时。但使用 WHEN 关键字时可以不放在最后，以下写法是被允许的：

**Examples:**

Example 1 (xml):
```xml
<flow>
    <!-- 串行编排超时控制 -->
    <chain name="then">
        THEN(a,b).maxWaitSeconds(5);
    </chain>

    <!-- 并行编排超时控制 -->
    <chain name="when">
        WHEN(a,b).maxWaitSeconds(3);
    </chain>

    <!-- 循环编排超时控制 -->
    <chain name="for">
        FOR(2).DO(a).maxWaitSeconds(3);
    </chain>
    <chain name="while">
        WHILE(w).DO(a).maxWaitSeconds(3);
    </chain>
    <chain name="iterator">
        ITERATOR(x).DO(a).maxWaitSeconds(3);
    </chain>

    <!-- 选择编排超时控制 -->
    <chain name="switch">
        SWITCH(s).TO(a, b).maxWaitSeconds(3);
    </chain>

    <!-- 条件编排超时控制 -->
    <chain name="if">
        IF(f, b, c).maxWaitSeconds(3);
    </chain>

    <!-- 组件超时控制 -->
    <chain name="component">
        WHEN(
            a.maxWaitSeconds(2),
            b.maxWaitSeconds(3)
        );
    </chain>

    <!-- 流程超时控制 -->
    <chain name="testChain">
        THEN(b)
    </chain>
    <chain name="chain">
        testChain.maxWaitSeconds(3);
    </chain>
</flow>
```

Example 2 (text):
```text
THEN(a, FINALLY(b).maxWaitSeconds(3))
```

Example 3 (text):
```text
THEN(a, FINALLY(b)).maxWaitSeconds(5);
```

Example 4 (text):
```text
THEN(a, THEN(b, FINALLY(c))).maxWaitSeconds(5);
```

---

## 🌾选择编排

**URL:** https://liteflow.cc/pages/d90483/

**Contents:**
- 🌾选择编排
- # 最基本的例子
- # DEFAULT关键字v2.9.5+
- # 和THEN,WHEN嵌套起来
- # 选择编排中的id语法
- # 选择编排中的tag语法

我们在写业务逻辑的时候，通常会碰到选择性问题，即，如果返回结果1，则进入A流程，如果返回结果2，则进入B流程，如果返回结果3，则进入C流程。在有些流程定义中也被定义为排他网关。

这个通过LiteFLow的表达式也非常容易实现，你可以用SWITCH...TO的组合关键字，注意的是SWITCH必须大写，to大小写均可。

如果，根据组件a，来选择执行b,c,d中的一个，你可以如下声明：

LiteFlow对选择编排新增了一个DEFAULT关键字。用法为SWITCH...TO...DEFAULT。

如上表达式的x如果返回非a,b,c中的一个，则默认选择到y。当然DEFAULT里面也可以是一个表达式。

我们结合之前两章，把三种表达式嵌套起来看一些例子

接下来展示一个SWITCH中套THEN和WHEN的例子。

如果你阅读过选择组件这一章，就应该知道，LiteFlow通过选择组件的返回来确定该选择什么。

那么如果SWITCH中套一个THEN，那么选择组件如果要选择这个THEN应该返回什么呢？

LiteFlow中规定，每个表达式都可以有一个id值，你可以设置id值来设置一个表达式的id值。然后在选择组件里返回这个id即可。用法如下：

如果你想选择THEN这个表达式，那么你可以在选择节点里返回t1:

事实上，除了给表达式赋值id属性之外，你还可以给表达式赋值tag属性。用法如下：

如果你想选择THEN这个表达式，那么你可以在选择节点里返回:

选择组件还有其他返回形式，详情请见选择组件这一章。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    SWITCH(a).to(b, c, d);
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    SWITCH(x).TO(a, b, c).DEFAULT(y);
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    THEN(
        a,
        WHEN(
            b,
            SWITCH(c).to(d,e)
        ),
        f
    );
</chain>
```

Example 4 (xml):
```xml
<chain name="chain1">
    THEN(
        a,
        SWITCH(b).to(
            c, 
            THEN(d, e).id("t1")
        ),
        f
    );
</chain>
```

---

## 🫐重试语法

**URL:** https://liteflow.cc/pages/b44233/

**Contents:**
- 🫐重试语法
- # 单个组件的重试
- # 表达式的重试
- # 整个Chain的重试
- # 带指定异常的重试
- # 特例

LiteFlow支持在EL层面进行重试次数的设置。用来满足一些失败了需要重试的场景。

以上EL表示，当b这个组件出现任何异常时，会最多自动重试3次。

3次重试中如果有任意一次成功，则正常往下走。如果3次均不成功，则会中断规则，最后LiteflowResponse结果中的isSuccess为false，并且结果中带有具体异常信息。

retry关键字不仅可以作用于组件上，还可以作用于任意表达式上，或者作用于表达式变量上，以下仅为举例：

retry关键字默认情况下，只要碰到任何异常，都会进行重试。

这里我们也可以指定异常，来完成特定情况下的重试：

上述表达式表示只有抛出NullPointerException异常的情况下才进行重试，其余的异常都不进行重试，直接中断失败。

那么只有抛出上述两个异常中的任意一个都会进行重试。

如果你的组件中设置了this.setIsEnd(true)，虽然会抛出一个ChainEndException，但是这个错无论如何不会导致重试。

因为这个Exception就是要强制中止。不应该被重试。

**Examples:**

Example 1 (xml):
```xml
<chain id="chain1">
    THEN(a, b.retry(3));
</chain>
```

Example 2 (xml):
```xml
<chain id="chain1">
    THEN(a, b).retry(3);
</chain>

<chain id="chain2">
    FOR(c).DO(a).retry(3);
</chain>

<chain id="chain3">
    exp = SWITCH(x).to(m,n,p);
    IF(f, exp.retry(3), b);
</chain>
```

Example 3 (xml):
```xml
<chain id="sub">
    THEN(a, b);
</chain>

<chain id="main">
    WHEN(x, y, sub.retry(3));
</chain>
```

Example 4 (xml):
```xml
<chain id="chain1">
    THEN(a, b).retry(3, "java.lang.NullPointerException");
</chain>
```

---

## 🥯链路继承🧪 Beta

**URL:** https://liteflow.cc/pages/524c43/

**Contents:**
- 🥯链路继承🧪 Beta
- # 使用方法
- # 例子
- # 注意事项

LiteFlow从以上版本起，支持chain之间的继承关系，使得chain之间可以进行继承和扩展。

可以在某个chain中使用extends属性来指明该chain继承自哪个chain。在被继承的chain中，需要预留出一个或多个占位符，以便于子chain可以对其进行扩展；而在子chain中，需要对被继承的父chain中的所有占位符进行实现。

子chain中的实现可以是组件，可以是表达式，可以是其他chain的id。但是需要注意的是，最终实现的chain必须是一个合法的EL规则，否则会解析失败。子chain的实现中同样可以包含占位符，从而实现多级继承。

通过上述定义，实现了一个继承自base的implA,最终实现的implA流程如下

在上面的定义中,implB继承自base2,base2又继承自base,最终实现的implB流程如下：

**Examples:**

Example 1 (xml):
```xml
<chain id="base">
    THEN(a, b, {{0}}, {{1}});
</chain>

<chain id="implA" extends="base">
    {{0}}=IF(c, d, e);
    {{1}}=SWITCH(f).to(j,k);
</chain>
```

Example 2 (xml):
```xml
<chain id="implA">
    THEN(a, b, IF(c, d, e), SWITCH(f).to(j,k));
</chain>
```

Example 3 (xml):
```xml
<chain id="base">
        THEN(a, b, {{0}}, {{1}});
    </chain>

    <chain id="base2" extends="base">
        {{0}}=THEN(a,b,{{3}});
        {{1}}=SWITCH(f).to({{4}},k);
    </chain>

    <chain id="implB" extends="base2">
        {{3}}=THEN(a,b);
        {{4}}=j;
    </chain>
```

Example 4 (xml):
```xml
<chain id="implB" extends="base2">
        THEN(
            a, b,
            THEN(a, b,
                THEN(a,b)
            ),
            SWITCH(f).to(j,k) 
        );
    </chain>
```

---

## 问答

**URL:** https://liteflow.cc/pages/845dff/

**Contents:**
- 问答
- # Q：LiteFlow支持事务么？
- # Q：LiteFlow适用于什么场景？
- # Q：是否可以做审批流或者角色轮转的流程？
- # Q：是否可以运行到一半手动停止，然后下次继续运行链路？
- # Q：为什么规则存储Nacos不支持拆分规则和脚本，而是需要保存整个XML？
- # Q：对于通用组件进行复用编排，上下文类型该如何设置？
- # Q：上下文里的数据是线程安全的吗？
- # Q：LiteFlow性能如何？
- # Q：是否支持逆向执行，来实现回滚等操作？

A：不能说支持或者说不支持，因为LiteFlow和事务没有本质上的关系。LiteFlow只不过在本地帮你把代码进行组件化和可编排化，事务还是按照原先的方式去做。例如，你完全可以加@Transactional来开启spring事务：

那么，这个链路中的所有组件，只要有一个组件发生异常，那么执行过的本地事务就会回滚，同理，你可以在任意地点加编程式事务。

同理，如果涉及到分布式事务，你也可以采用任意一种分布式事务的解决方案来做，这本质上已经脱离了LiteFlow的讨论范畴。

A：LiteFlow适用于具有复杂逻辑，逻辑复用性比较强的业务系统，可以利用LiteFlow框架对业务进行解耦，编排，复用，动态更新，使代码更加优雅。

LiteFlow使用场景不限业务，只要你的业务系统可以根据业务边界来划分出来一个个独立的组件逻辑。既可以使用LiteFlow框架来优化你的代码。

A：其实在开篇LiteFLow简介已经有提到过，LiteFlow不做基于角色流转的流程，只做逻辑流程。并且LiteFlow在以后，也不会做基于角色流转的流程，因为LiteFlow要保持轻量和易用性，是一个无状态的流程编排工具。如果你的业务是基于角色流转的，推荐使用Flowable。

A：不可以。LiteFlow是一个无状态的规则引擎。不对中间状态进行存储。LiteFlow更希望业务一次性运行完，并且自己保证其幂等性。如果你确实有业务场景，需要运行到一半手动停止。那么建议你去使用Flowable等一些有状态的流程引擎框架。

因为Nacos没法对一个group进行监听，如果拆分了，那就会导致新增规则，删除规则没法被监听到。

而现在这种单个节点的形式，虽然没拆分，但是功能是齐全的。这也是无奈的选择。我们也想拆分的，但是我们搞不定。

Nacos官方也有类似的issue，官方表示考虑在3.0的时候加入对group的监听特性。

如果你有一个通用组件，要定义在不同的链路中。那你就给这个组件一个单独的上下文，LiteFlow是支持多上下文传入的，你调用链路的时候，代入这个上下文。那这个通用组件就可以在不同的链路中使用了。

还有种方法，就是你自己定义一个弱类型的上下文类型，比如Map。但是使用的时候需要你自己去强转类型。

A：LiteFlow虽然提供了默认的上下文实现，但是更建议用户自己去实现自己的上下文。Slot本质上是一个普通的值对象，虽然LiteFlow能保证上下文本身的线程安全（指在多线程情况下，多个请求上下文不会串），但是上下文内数据的线程安全性是无法保障的，这需要用户自己去定义其线程安全的属性。比如你在上下文里定义了一个int的变量，多个异步节点对其进行增加，那当然会有线程安全的问题。你需要在你自己定义的上下文内部去声明一个AtomicInteger对象，从而保证线程安全。

A：LiteFlow本身性能优秀，几乎没有什么额外的损耗，在压测过程中，基于复杂的价格逻辑引擎的业务系统，三十多个组件，在实测中可以跑到单机1500多的TPS。当然，这是基于良好的组件实现逻辑的前提下。如果你的组件里有一个bad sql，或者大量的IO操作，RPC调用操作，那么任何框架也无法提升你业务的TPS。这里只能说LiteFlow框架本身对系统几乎无额外损耗，如果你的系统使用了LiteFlow但是TPS/QPS很低的话，那么请从你的组件实现逻辑入手排查。

A：不支持，如果要实现本地回滚，请用事务来控制，如果涉及分布式事务的回滚，也有分布式事务的解决方案可以用。

但是之后的版本可能会出一个特性，在执行的过程中，如果遇到某个Exception去执行额外的链路，如果真的想逆向执行，可以把回滚组件放到这个里面。

A：已经有无数人说的界面编排特性，我想说几句：

界面编排已经不算作特性了，应该算作LiteFlow这个开源框架的一个形态升级，形态延伸。

这个形态升级我一定会做。不仅会做，还会出一整套集编排，管理，监控，追踪于一体的后端界面。

这也是LiteFlow这个框架的愿景：做最轻量，最好用的，能快速赋予生产力的国产优秀的规则编排框架。

LiteFlow才刚刚起步，核心的很多地方还在快速迭代中。后面不做好，无法马上开始做前端编排。加上作者也有本职工作，也是打工人。只能日常挤出时间来做。所以这点望大家理解。目前LiteFlow的迭代还是很频繁的。我打算之后每个月出2个迭代更新版本。

相信这天的到来，不会太久。请支持LiteFlow框架的小伙伴继续关注它。

A：LiteFlow是轻量级的单服务编排，你可以把它理解为一个工具包。和高可用，分布式没有关系。

你一个业务系统里面有50个组件，liteflow可以编排，复杂一点的也可以。但是你多个业务系统，想要用一个链路，去编排不同服务里的组件。先去调用A服务的组件a，再去调用B服务的组件b，再去调用C服务的组件c，这种LiteFlow并不支持。

变相的实现，只有你独立出来一个服务X，然后服务X写3个组件(x1,x2,x3)分别用rpc去调用a,b,c，然后把x1,x2,x3编排成一个链路。

但是对LiteFlow来说，它运行的组件也只是X服务中的3个组件，至于组件里面是rpc调用还是其他网络IO操作，这和LiteFlow本身没有关系，因为已经涉及到业务实现层了。

为什么我在组件或者脚本中取到的name参数为null？

其中第二个参数为流程入参，流程入参其实和上下文没什么关系，在组件中通过this.getRequestData()来获得。在脚本中通过requestData变量获得。

第三个参数为上下文，如果你传入了class，那么liteflow会帮你初始化一个空的对象。当然也支持传入已经初始化好的bean。在组件里通过this.getContextBean来获得，在脚本里直接通过xxxContext来引用。

回到上述问题，如果把初始化好的bean作为流程入参传入，而上下文传入UserContext.class，那么其实this.getRequestData出来的是这个bean，而this.getContextBean出来是一个空的UserContext对象，所以你拿到的name为null。

在很多情况下，流程入参是可以包装到上下文里去的。所以流程入参这里给个null即可。所以上下文和流程入参是2个完全不相干的概念，这点别弄混淆。

其中c发送结果到第三方，d要等待第三方回调才可以处理，这种要如何做？

A：LiteFlow是无状态的规则引擎，即时不用LiteFlow，这种模式也应该考虑如何更优雅的设计

一般都是分成2段式，第一段发出去后，保存其中间状态，然后回调回来再进行第二段。

A：确保LF的版本在2.11.4+以上，如果版本没问题，还出现栈溢出，大概率就是jvm参数Xss配置太少了。

解析EL本质上是一个递归调用，如果你层数很多很深，用到的栈空间就会增加。如果Xss太少就会报栈溢出的错误。

在LiteFlow中启动时出现这个错，大概率都可能是以下3个依赖包的冲突而导致。

transmittable-thread-local 要求版本 2.12.3+

byte-buddy 要求版本 1.14.10+

所谓依赖冲突就是你本地的其他jar包传递依赖的包覆盖了LiteFlow传递依赖的版本。如果你的这个错是以上jar包的某一个，只需要重新定义其版本号即可。

**Examples:**

Example 1 (java):
```java
@Transactional
public void testIsAccess() {
  LiteflowResponse response = flowExecutor.execute2Resp("chain1", 101);
  if (!response.isSuccess()){
    throw response.getCause();
  }
}
```

Example 2 (java):
```java
UserContext context = new UserContext();
context.setName("jack");
LiteflowResponse response = flowExecutor.extcute2Resp("chain1", context, UserContext.class);
```

Example 3 (java):
```java
//第一个参数为流程ID，第二个参数为流程入参，后面可以传入多个上下文class
public LiteflowResponse execute2Resp(String chainId, Object param, Class<?>... contextBeanClazzArray)
//第一个参数为流程ID，第二个参数为流程入参，后面可以传入多个上下文的Bean
public LiteflowResponse execute2Resp(String chainId, Object param, Object... contextBeanArray)
```

Example 4 (java):
```java
UserContext context = new UserContext();
context.setName("jack");
LiteflowResponse response = flowExecutor.extcute2Resp("chain1", null, context);
```

---

## 🍓项目特性

**URL:** https://liteflow.cc/pages/724bc3/

**Contents:**
- 🍓项目特性

← 🍤LiteFlow简介 ☕️JDK支持度→

---

## 🍦验证脚本

**URL:** https://liteflow.cc/pages/a5f7d9/

**Contents:**
- 🍦验证脚本

LiteFlow提供了验证脚本的接口，你可以这么使用，去验证一个脚本是否规范：

返回布尔值，true为通过检查，反之亦然。

多增加了带验证结果的接口，可以方便使用者拿到验证的错误信息

**Examples:**

Example 1 (java):
```java
boolean isValid = ScriptValidator.validate(script);
```

Example 2 (java):
```java
ValidationResp resp = ScriptValidator.validateWithEx(script);
boolean isSuccess = resp.isSuccess();
Exception e = resp.getCause();
```

---

## 🔆验证规则

**URL:** https://liteflow.cc/pages/395fd0/

**Contents:**
- 🔆验证规则

LiteFlow为规则EL提供了一个验证的方法接口，用于验证EL是不是能被正确解析。

**Examples:**

Example 1 (java):
```java
public void yourMethod() {
    boolean isValid = LiteFlowChainELBuilder.validate("THEN(a, b, h)");
    ...
}
```

Example 2 (java):
```java
public void yourMethod() {
    ValidationResp resp = LiteFlowChainELBuilder.validateWithEx("THEN(a, b, h)");
    if (!resp.isSuccess()){
        log.error(resp.getCause());
    }
}
```

---
