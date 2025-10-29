# Liteflow - Components

**Pages:** 36

---

## 🥐Aviator脚本引擎

**URL:** https://liteflow.cc/pages/bad4b0/

**Contents:**
- 🥐Aviator脚本引擎
- # 依赖
- # 使用
- # 脚本类型
- # 如何取到上下文以及和Java类进行交互

使用aviator脚本语言，你需要额外依赖LiteFlow提供的脚本插件：

你需要在你的xml中去定义node节点，以下是一个示例：

在aviator中，你同样可以导入java的包名，直接调用java的方法。

在aviator中，调用java方式和其他不一样，比如我们上下文是UserContext，在其他脚本语言中调用是用userContext.setName("jack")，而在aviator脚本中，调用方式是setName(userContext, "jack")，也就是method(bean, args)这种形式，有点类似java反射的invoke形式。这点要注意下。

script：普通脚本节点，脚本里无需返回。

switch_script：选择脚本节点，脚本里需要返回选择的节点Id。

boolean_script：条件脚本节点，脚本里需要返回true/false。

for_script：数量循环节点，脚本里需要返回数值类型，表示循环次数。

关于这部分，请详细参考脚本与Java进行交互这一章节。

← 🍝Lua脚本引擎 🥠Kotlin脚本引擎→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-aviator</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (xml):
```xml
<node id="s1" name="普通脚本1" type="script" language="aviator">
    <![CDATA[
        use java.util.Date;
        use cn.hutool.core.date.DateUtil;
        let d = DateUtil.formatDateTime(new Date());
        println(d);

        a = 2;
        b = 3;

        setData(defaultContext, "s1", a*b);
    ]]>
</node>
```

---

## 🐋FlowExecutor层面的线程池

**URL:** https://liteflow.cc/pages/82cb24/

**Contents:**
- 🐋FlowExecutor层面的线程池

LiteFlow执行一个流程是要用FlowExecutor来驱动的。

最常用的就是flowExecutor.execute2Resp方法，这也是官方推荐使用的方法。这个方法无论当中的节点是串行还是并行，最终当返回的时候LiteflowResponse对象的时候，这条链路是全部执行完毕的。

但是如果业务中的组件需要处理很多业务，你的主程序不想阻塞的在execute2Resp这个方法上的时候，你可以使用flowExecutor.execute2Future方法。

这时候，方法不再返回LiteflowResponse对象，而是返回Future<LiteflowResponse>对象，且不会阻塞。这样主线程就可以后续需要使用的地方拿到future中的LiteflowResponse对象，从而实现主线程无阻塞的效果。

当然，有Future对象，就一定会有线程池。这个线程池在LiteFlow是单独配置的。框架给了默认值：

当然也支持自定义线程池，你需新建一个类，然后实现ExecutorBuilder接口：

**Examples:**

Example 1 (properties):
```properties
liteflow.main-executor-works=64
liteflow.main-executor-class=com.yomahub.liteflow.thread.LiteFlowDefaultMainExecutorBuilder
```

Example 2 (java):
```java
public class CustomThreadBuilder implements ExecutorBuilder {
    @Override
    public ExecutorService buildExecutor() {
        return Executors.newCachedThreadPool();
    }
}
```

---

## 🥏Groovy脚本引擎

**URL:** https://liteflow.cc/pages/36877b/

**Contents:**
- 🥏Groovy脚本引擎
- # 依赖
- # 使用
- # 脚本类型
- # 如何取到上下文以及和Java类进行交互

使用groovy脚本语言，你需要额外依赖LiteFlow提供的脚本插件：

你需要在你的xml中去定义node节点，以下是一个示例：

以上是一个普通脚本组件的示例，可以看到，groovy的脚本语言还是非常类似于java的。甚至还可以在脚本里定义类。

script：普通脚本节点，脚本里无需返回。

switch_script：选择脚本节点，脚本里需要返回选择的节点Id。

boolean_script：条件脚本节点，脚本里需要返回true/false。

for_script：数量循环节点，脚本里需要返回数值类型，表示循环次数。

关于这部分，请详细参考脚本与Java进行交互这一章节。

← ☕️Java脚本引擎 🧀Javascript脚本引擎→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-groovy</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (xml):
```xml
<node id="s1" name="普通脚本1" type="script" language="groovy">
    <![CDATA[
    import cn.hutool.core.collection.ListUtil
    import cn.hutool.core.date.DateUtil

    import java.util.function.Consumer
    import java.util.function.Function
    import java.util.stream.Collectors

    def date = DateUtil.parse("2022-10-17 13:31:43")
    println(date)
    defaultContext.setData("demoDate", date)

    List<String> list = ListUtil.toList("a", "b", "c")

    List<String> resultList = list.stream().map(s -> "hello," + s).collect(Collectors.toList())

    defaultContext.setData("resultList", resultList)

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
```

---

## 🧀Javascript脚本引擎

**URL:** https://liteflow.cc/pages/07f433/

**Contents:**
- 🧀Javascript脚本引擎
- # 依赖
- # 使用
- # 脚本类型
- # 如何取到上下文以及和Java类进行交互

对于Javascript脚本，你有两种引擎可以选择，一种是基于jdk的js引擎实现，只支持ES5。另一种是基于GraalJs引擎实现，支持ES6。

如果你使用jdk8，你可以选用下面任意一种脚本引擎，而jdk11和jdk17，你只能选用graaljs引擎，因为jdk8之后的jdk已经移除了jdk自带的Nashorn JavaScript引擎。

你需要在你的xml中去定义node节点，以下是一个示例

以上是一个普通脚本组件的示例，你可以用js的绝大部分语法特性，甚至还可以在脚本里定义Function。

script：普通脚本节点，脚本里无需返回。

switch_script：选择脚本节点，脚本里需要返回选择的节点Id。

boolean_script：条件脚本节点，脚本里需要返回true/false。

for_script：数量循环节点，脚本里需要返回数值类型，表示循环次数。

关于这部分，请详细参考脚本与Java进行交互这一章节。

← 🥏Groovy脚本引擎 🥞QLExpress脚本引擎→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-javascript</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-graaljs</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 3 (xml):
```xml
<node id="s1" name="普通脚本1" type="script" language="js">
    <![CDATA[
        var a=3;
        var b=2;
        var c=1;
        var d=5;

        function addByArray(values) {
            var sum = 0;
            for (var i = 0; i < values.length; i++) {
                sum += values[i];
            }
            return sum;
        }

        var result = addByArray([a,b,c,d]);

        defaultContext.setData("s1",parseInt(result));
    ]]>
</node>
```

---

## ☕️Java脚本引擎

**URL:** https://liteflow.cc/pages/2b8afb/

**Contents:**
- ☕️Java脚本引擎
- # 介绍
- # 使用liteflow-script-javax
- # 使用liteflow-script-javax-pro
- # 如何取Spring上下文中的数据

LiteFlow支持了用Java本身作为脚本语言的特性。用Java作为脚本语言也是LiteFlow首推的脚本语言。

也就是说，在写组件脚本时，你可以完全用Java自身的语法来写脚本。同样这部分的脚本，也是可以进行热刷新的。

LiteFlow提供了三种Java脚本的插件，分别为：

以下针对于liteflow-script-javax和liteflow-script-javax-pro这2个插件进行说明。

如果你使用2.13.X系列版本，推荐使用liteflow-script-javax-pro。

如果你使用2.12.X系列版本，推荐使用liteflow-script-javax。

你需要额外依赖LiteFlow提供的脚本插件：

使用以Liquor为核心的javax插件，部署运行的时候必须为JDK，而不能是JRE，这点要注意下。

使用liteflow-script-javax插件，需要像如下去定义，以下是个例子：

如果你要实现其他种类的组件，请替换实现的接口：

script：普通脚本节点，需要实现CommonScriptBody接口，脚本里返回null即可。

switch_script：选择脚本节点，需要实现SwitchScriptBody接口，脚本里需要返回选择的节点Id。

boolean_script：布尔脚本节点，需要实现BooleanScriptBody接口，脚本里需要返回true/false。

for_script：数量循环节点，需要实现ForScriptBody接口，脚本里需要返回数值类型，表示循环次数。

之前类方法通过this调用的，现在都用wrap.getCmp()来替换。

但是在这个插件中，你无法覆盖其他方法，比如说isAccess或者onSuccess等方法。

你需要额外依赖LiteFlow提供的脚本插件：

使用以Liquor为核心的javax插件，部署运行的时候必须为JDK，而不能是JRE，这点要注意下。

这个为上一个插件的升级版本，在这个插件中，定义java完全是按照静态java类的方式去定义了，以下是一个例子：

可以看到，在升级版的插件中，其定义java的方式完全和类里定义的完全一致了。这意味着，你可以用this来进行调用，你也可以覆盖其他方法如isAccess，beforeProcess等。

即便是java脚本组件，目前还依旧不可以定义迭代循环组件。这意味着即使你用了java-pro插件，你现在可以继承NodeIteratorComponent，但是你依旧无法正确执行。

值得注意的是，以上2个脚本插件虽然完全是Java的语法，但是你无法用@Resource或者@Autowired来进行注入spring的bean。

LiteFlow提供一个方法，用来获取Spring中的bean数据，如下示例：

这样就可以获得在spring上下文中注入的UserDomain对象了。

← 🌭脚本语言介绍 🥏Groovy脚本引擎→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-javax</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (xml):
```xml
<node id="s1" name="普通脚本1" type="script" language="java">
    <![CDATA[
    import cn.hutool.core.collection.ListUtil;
    import com.alibaba.fastjson2.JSON;
    import com.yomahub.liteflow.script.body.CommonScriptBody;
    import com.yomahub.liteflow.slot.DefaultContext;
    import com.yomahub.liteflow.spi.holder.ContextAwareHolder;
    import com.yomahub.liteflow.test.script.javax.common.cmp.Person;
    import com.yomahub.liteflow.test.script.javax.common.cmp.TestDomain;
    import com.yomahub.liteflow.script.ScriptExecuteWrap;
    import java.util.List;
    import java.util.function.ToIntFunction;

    public class Demo implements CommonScriptBody {
        public Void body(ScriptExecuteWrap wrap) {
            int v1 = 2;
            int v2 = 3;
            DefaultContext ctx = wrap.getCmp().getFirstContextBean();
            ctx.setData("s1", v1 * v2);

            TestDomain domain = ContextAwareHolder.loadContextAware().getBean(TestDomain.class);
            System.out.println(domain);
            String str = domain.sayHello("jack");
            ctx.setData("hi", str);

            List<Person> personList = ListUtil.toList(
                    new Person("jack", 15000),
                    new Person("tom", 13500),
                    new Person("peter", 18600)
            );

            int totalSalary = personList.stream().mapToInt(Person::getSalary).sum();

            System.out.println(totalSalary);
            ctx.setData("salary", 47100);

            return null;
        }
    }
    ]]>
</node>
```

Example 3 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-javax-pro</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 4 (xml):
```xml
<node id="s1" name="普通脚本1" type="script" language="java">
    <![CDATA[
    import cn.hutool.core.collection.ListUtil;
    import com.yomahub.liteflow.core.NodeComponent;
    import com.yomahub.liteflow.slot.DefaultContext;
    import com.yomahub.liteflow.spi.holder.ContextAwareHolder;
    import com.yomahub.liteflow.test.script.javaxpro.common.cmp.Person;
    import com.yomahub.liteflow.test.script.javaxpro.common.cmp.TestDomain;

    import java.util.List;

    public class Demo extends NodeComponent {
        @Override
        public void process() throws Exception {
            int v1 = 2;
            int v2 = 3;
            DefaultContext ctx = this.getFirstContextBean();
            ctx.setData("s1", v1 * v2);

            TestDomain domain = ContextAwareHolder.loadContextAware().getBean(TestDomain.class);
            System.out.println(domain);
            String str = domain.sayHello("jack");
            ctx.setData("hi", str);

            List<Person> personList = ListUtil.toList(
                    new Person("jack", 15000),
                    new Person("tom", 13500),
                    new Person("peter", 18600)
            );

            int totalSalary = personList.stream().mapToInt(Person::getSalary).sum();

            System.out.println(totalSalary);
            ctx.setData("salary", 47100);
        }
    }
    ]]>
</node>
```

---

## 🥠Kotlin脚本引擎

**URL:** https://liteflow.cc/pages/7c44ca/

**Contents:**
- 🥠Kotlin脚本引擎
- # 依赖
- # 使用
- # 脚本类型

使用aviator脚本语言，你需要额外依赖LiteFlow提供的脚本插件：

你需要在你的xml中去定义node节点，以下是一个示例：

在kotlin脚本中，上下文的获取一定要加bindings这个关键字。当然不仅仅是上下文，一切元信息里的东西都要加上这个关键字。

关于脚本中如何取到上下文以及和Java类进行交互的细节请看脚本与Java进行交互这章。

script：普通脚本节点，脚本里无需返回。

switch_script：选择脚本节点，脚本里需要返回选择的节点Id。

boolean_script：条件脚本节点，脚本里需要返回true/false。

for_script：数量循环节点，脚本里需要返回数值类型，表示循环次数。

← 🥐Aviator脚本引擎 🍣脚本与Java进行交互→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-kotlin</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (xml):
```xml
<node id="s1" type="script" language="kotlin">
    import com.yomahub.liteflow.slot.DefaultContext

    fun sum(a: Int, b: Int) = a + b
    var a = 2
    var b = 3
    // 从 bindings 中获取上下文
    val defaultContext = bindings["defaultContext"] as DefaultContext
    defaultContext.setData("s1", sum(a, b))
    println("Hello Kotlin!")
</node>
```

---

## 🏄LiteflowComponent

**URL:** https://liteflow.cc/pages/68320a/

**Contents:**
- 🏄LiteflowComponent

@LiteflowComponent注解是继承于Spring的@Component标签的，所以从作用上来说，和@Component标签并没有什么区别，但是@LiteflowComponent新增加了name属性，用于给组件起别名，在打印调用链的时候会体现。具体请查看打印信息详解章节，新版本开始，推荐大家使用@LiteflowComponent，当然@Component也同样可以继续沿用。

所以LiteFlow的组件也是受Spring容器管理的，你可以用Spring注解@AutoWired或者@Resource去注入任何其他Bean。

← ⌛️迭代循环组件 🛀组件内方法覆盖和调用→

---

## 🍝Lua脚本引擎

**URL:** https://liteflow.cc/pages/5f0cc7/

**Contents:**
- 🍝Lua脚本引擎
- # 依赖
- # 使用
- # 脚本类型
- # 如何取到上下文以及和Java类进行交互

使用lua脚本语言，你需要额外依赖LiteFlow提供的脚本插件：

你需要在你的xml中去定义node节点，以下是一个示例：

在lua中，调用java方法是用:来调用的，并不是.，比如defaultContext:setData("s1",a*b)。

script：普通脚本节点，脚本里无需返回。

switch_script：选择脚本节点，脚本里需要返回选择的节点Id。

boolean_script：条件脚本节点，脚本里需要返回true/false。

for_script：数量循环节点，脚本里需要返回数值类型，表示循环次数。

关于这部分，请详细参考脚本与Java进行交互这一章节。

← 🍧Python脚本引擎 🥐Aviator脚本引擎→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-lua</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (xml):
```xml
<node id="s1" name="普通脚本1" type="script">
    <![CDATA[
        local a=6
        local b=10
        if(a>5) then
            b=5
        else
            b=2
        end
        defaultContext:setData("s1",a*b)
        defaultContext:setData("s2",_meta:get("nodeId"))
    ]]>
</node>
```

---

## 🍧Python脚本引擎

**URL:** https://liteflow.cc/pages/114982/

**Contents:**
- 🍧Python脚本引擎
- # 依赖
- # 使用
- # 脚本类型
- # 如何取到上下文以及和Java类进行交互

使用python脚本语言，你需要额外依赖LiteFlow提供的脚本插件：

python解析执行依赖Jython环境，不安装部署启动会报错（IDEA里不会报错），环境安装说明如下

一、下载安装Jython Installer

https://www.jython.org/download (opens new window)

你需要在你的xml中去定义node节点，以下是一个示例：

上面的例子为python语法，你甚至可以引入一些python的原有的包来做逻辑。对于复杂的逻辑，推荐直接调用java类，关于如何和java互动请看下面。

如果遇到中文乱码的现象，请使用decode函数，比如：

script：普通脚本节点，脚本里无需返回。

switch_script：选择脚本节点，脚本里需要返回选择的节点Id。

boolean_script：条件脚本节点，脚本里需要返回true/false。

for_script：数量循环节点，脚本里需要返回数值类型，表示循环次数。

关于这部分，请详细参考脚本与Java进行交互这一章节。

← 🥞QLExpress脚本引擎 🍝Lua脚本引擎→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-python</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (java):
```java
Properties props = new Properties();
Properties preprops = System.getProperties();
props.put("python.home", jython安装目录);
PythonInterpreter.initialize (preprops, props, new String[]{});
```

Example 3 (xml):
```xml
<node id="s1" name="普通脚本1" type="script" language="python">
    <![CDATA[
        import json

        x='{"name": "杰克", "age": 25, "nationality": "China"}'
        jsonData=json.loads(x)
        name=jsonData['name']
        defaultContext.setData("name", name.decode('utf-8'))


        a=6
        b=10
        if a>5:
            b=5
            print 'hello'
        else:
            print 'hi'
        defaultContext.setData("s1",a*b)
    ]]>
</node>
```

Example 4 (python):
```python
print '你好'.decode('UTF-8')
```

---

## 🥞QLExpress脚本引擎

**URL:** https://liteflow.cc/pages/19db6d/

**Contents:**
- 🥞QLExpress脚本引擎
- # 依赖
- # 使用
- # 脚本类型
- # 如何取到上下文以及和Java类进行交互

你需要在你的xml中去定义node节点，以下是一个示例：

script：普通脚本节点，脚本里无需返回。

switch_script：选择脚本节点，脚本里需要返回选择的节点Id。

boolean_script：条件脚本节点，脚本里需要返回true/false。

for_script：数量循环节点，脚本里需要返回数值类型，表示循环次数。

关于这部分，请详细参考脚本与Java进行交互这一章节。

← 🧀Javascript脚本引擎 🍧Python脚本引擎→

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-script-qlexpress</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (xml):
```xml
<node id="s1" name="普通脚本" type="script">
    <![CDATA[
        a=3;
        b=2;
        defaultContext.setData("s1",a*b);
    ]]>
</node>

<node id="s2" name="条件脚本" type="switch_script">
    <![CDATA[
        count = defaultContext.getData("count");
        if(count > 100){
            return "a";
        }else{
            return "b";
        }
    ]]>
</node>
```

---

## 🥭什么叫声明式组件

**URL:** https://liteflow.cc/pages/46f0fa/

**Contents:**
- 🥭什么叫声明式组件

之前章节介绍的一些类型的组件，在写法上需要你自己去定义一个类去继承诸如NodeComponent之类的父类。这样一方面造成了耦合，另一方面由于java是单继承制，所以使用者就无法再去继承自己的类了，在自由度上就少了很多玩法。

声明式组件这一特性允许你自定义的组件不继承任何类和实现任何接口，普通的类也可以依靠注解来完成LiteFlow组件的声明。

甚至于你可以用一个类去定义多个组件，仅仅依靠注解就可以完成，这个特性也叫做方法级别式声明。

目前声明式组件只能在springboot环境中使用.

← 🛀组件内方法覆盖和调用 🧅类级别式声明→

---

## ⛰元数据操作器

**URL:** https://liteflow.cc/pages/7cb165/

**Contents:**
- ⛰元数据操作器

在LiteFlow框架中，最重要的两个概念就是规则以及组件。

框架提供了一个元数据管理器LiteflowMetaOperator用来管理这两大元素。

Chain getChain(String chainId)：通过chainId得到Chain对象

List<Chain> getChainsContainsNodeId(String nodeId)：找出含有指定nodeId的chain对象

void reloadAllChain()：刷新所有的规则

void reloadOneChain(String chainId, String el)：刷新某一个规则

void reloadOneChain(String chainId, String el, String routeEl)：刷新某一个规则，带决策路由。（有关决策路由的知识请参考决策路由概念和介绍）

void removeChain(String chainId)：从元数据卸载掉一个chain

void removeChain(String... chainIds)：从元数据中卸载掉多个chain

List<Node> getNodes(Executable executable)：从任意Executable对象中取到Node列表，Executable包括Chain，Condition，Node

List<Node> getNodes(String chainId)：通过chainId获得这个chain中所有的Node

List<Node> getNodesInAllChain(String nodeId)：通过nodeId找到在所有Chain中存在的Node对象列表

---

## 🍒前置和后置编排

**URL:** https://liteflow.cc/pages/9f93be/

**Contents:**
- 🍒前置和后置编排
- # 前置组件
- # 后置节点
- # 顺序问题
- # 层级和范围

LiteFlow支持了前置编排和后置编排特性。

此特性针对整个链路，在链路之前之后固定执行某些组件。用于业务的前置处理和后置处理。

前置组件和后置组件，均为串行节点，目前不支持异步。

固定在一个流程开始之前执行某些节点，规则表达式中用PRE关键字(必须大写)来表示:

固定在一个流程结束后执行某些节点，要注意的是后置节点不受Exception影响，即便节点出错，后置节点依旧会执行。在规则表达式中用FINALLY关键字(必须大写)表示：

前置节点一定要写在前面吗？后置节点一定要写在最后吗？

并不是，PRE和FINALLY可以写在任意地方。

下面这个表达式和上面是等价效果的, 即使不放在相对应的位置，还是一样的效果。

LiteFlow 2.9.5中能支持PRE和FINALLY写在表达式的任意层级。也意味着你在子流程中，子变量中也可以用前置和后置组件。

PRE和FINALLY只能写在THEN表达式中，如果你写在WHEN表达式中或者其他诸如SWITCH,IF的表达式中，是不会生效的，而且这样写也是毫无意义的。这点需要注意下。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    THEN(
        PRE(p1, p2), 
        a, b, c, 
        WHEN(d, e)
    );
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    THEN(
        a, b, c, 
        FINALLY(f1, f2)
    );
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    THEN(
        PRE(a), c, d, FINALLY(f1, f2)
    );
</chain>
```

Example 4 (xml):
```xml
<chain name="chain1">
    THEN(
        FINALLY(f1, f2), c, PRE(a), d
    );
</chain>
```

---

## ⛓布尔组件

**URL:** https://liteflow.cc/pages/cb0b59/

**Contents:**
- ⛓布尔组件

布尔组件是以前IF组件，WHILE组件，BREAK组件的统一。他们三个组件有共同特征，都是返回布尔类型，所以将三个组件类型合三为一，成为了布尔组件。

IF...ELIF...ELSE，可以参考条件编排这一章。

WHILE...DO...，可以参考循环编排这一章。

FOR...DO...BREAK,WHILE...DO...BREAK,ITERATOR...DO...BREAK，可以参考循环编排这一章。

布尔组件的定义，需要继承NodeBooleanComponent：

布尔组件的内部可以覆盖的方法和this关键字可调用的方法见组件内方法覆盖和调用这一章。

**Examples:**

Example 1 (java):
```java
@Component("x")
public class XCmp extends NodeBooleanComponent {
	@Override
	public boolean processBoolean() throws Exception {
	    //do your biz
		return true;
	}
}
```

---

## 🎋并行编排

**URL:** https://liteflow.cc/pages/b3446a/

**Contents:**
- 🎋并行编排
- # 基本用法
- # 等价用法
- # 和串行嵌套起来(一)
- # 和串行嵌套起来(二)
- # 忽略错误
- # 任一节点先执行完则忽略其他
- # 指定任意节点先执行完则忽略其他v2.11.1+
- # 随机N个任务执行完成后即可往下运行v2.15.0+
- # 开启WHEN线程池隔离v2.11.1+

如果你要并行执行a,b,c三个组件，你可以用WHEN关键字，需要注意的是，WHEN必须大写。

由于WHEN关键字用来表示并行语义上并不是很妥当，所以后期版本同时支持了PAR关键字，和WHEN是完全等价的。

接下来，让我们把THEN和WHEN结合起来用，看一个示例：

在以上示例里，b,c,d默认并行都执行完毕后，才会执行e。

上面的示例应该很好理解吧，那么再看一个示例：

WHEN关键字提供了一个子关键字ignoreError(默认为false)来提供忽略错误的特性，用法如下：

以上假设b,c,d中任一一个节点有异常，那么最终e仍旧会被执行。

WHEN关键字提供了一个子关键字any(默认为false)用来提供并行流程中，任一条分支先执行完即忽略其他分支，继续执行的特性。用法如下：

以上流程，假设e节点先执行完，那么不管其他分支是否执行完，会立马执行节点f。

LiteFlow支持了并行编排中指定节点的执行则忽略其他，WHEN 关键字新增子关键字 must (不可为空)，可用于指定需等待执行的任意节点，可以为 1 个或者多个，若指定的所有节点率先完成，则继续往下执行，忽略同级别的其他任务，用法如下：

以上流程中，must指定了b,c，则b，c是一定会被执行完毕了，如果b，c执行完毕了后d还未执行完，则忽略，直接执行下一个组件f。

以上是单节点的用法，must还可以指定一个或多个表达式。比如

在这个表达式中WHEN里有一个嵌套的THEN，如果需要指定这个表达式，则需要给这个表达式设置一个id，must里需要指定这个id，需要注意的是，must里指定id，需要用引号括起来。

LiteFlow支持在WHEN后随机指定N个任务，运行完之后则继续进行的特性。新增percentage关键字，用法如下：

以上表达式的意思为：在a,b,c,d,e五个组件里随机挑3个(5*0.6)来运行。执行完这3个即继续往下走。

percentage入参为数值类型，可选值为 [0, 1]。若percentage为0 ，则与any(true)效果一致；若为1，则相当于不加。

以上例子如果percentage值为0.66，则最终随机挑选4个(5*0.66=3.3，向上取整)。

目前liteflow设计里when线程池，如果你不单独设置自定义线程池，那么就会用默认的线程池。而这个线程池，是所有的when共同一个。

LiteFlow从2.11.1开始，提供一个liteflow.when-thread-pool-isolate参数，默认为false，如果设为true，则会开启WHEN的线程池隔离机制，这意味着每一个when都会有单独的线程池。这个特性对于运行复杂的嵌套when时是可以提升运行速度的且规避掉一些锁的问题。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    WHEN(a, b, c);
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    PAR(a, b, c);
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    THEN(
        a,
        WHEN(b, c, d),
        e
    );
</chain>
```

Example 4 (xml):
```xml
<chain name="chain1">
    THEN(
        a,
        WHEN(b, THEN(c, d)),
        e
    );
</chain>
```

---

## 🌳循环编排

**URL:** https://liteflow.cc/pages/fbf715/

**Contents:**
- 🌳循环编排
- # FOR循环
- # WHILE循环
- # ITERATOR迭代循环
- # BREAK
- # 多层嵌套循环中获取下标v2.12.3+
- # 多层嵌套循环中获取迭代对象v2.12.3+
- # 脚本中获取循环下标和迭代对象
- # 异步循环v2.11.0+

LiteFlow提供了循环编排表达式组合。

FOR循环表达式用于固定次数的循环，通常的用法为：

上述表达式表示把a->b这个链路固定循环了5次。

如果你在定义规则的时候并不确定要循环几次，要在代码运行的时候才知道。那你也可以这样定义：

其中f这个节点需要为次数循环组件，返回一个int循环次数，如何定义请参照次数循环组件。

WHILE循环表达式用于有条件的循环，通常用法为：

其中w这个节点需要为布尔组件，返回一个布尔值，为true则继续循环，如何定义请参照布尔组件。

WHILE(true)的支持v2.15.1+

如果你希望进行一个无限循环，仅靠BREAK来选择退出机制，则可以直接用：

注意，用WHILE(true)一定要搭配BREAK，否则将陷入死循环。

ITERATOR迭代循环表达式通常用于集合的循环，通常用法为：

其中x这个节点需要为迭代循环组件，返回一个迭代器，如何定义请参照迭代循环组件。

要注意的是，迭代循环组件只支持java定义，不支持脚本。

LiteFlow同样也支持BREAK语法，代表退出循环。

BREAK关键字可以跟在FOR，WHILE，ITERATOR后面，通常用法为：

其中c这个节点需要为布尔组件，返回一个布尔值，为true则退出循环。如何定义请参考布尔组件。

BREAK关键字是在每次循环的末尾进行判断的。

a组件要取到当前循环下标：this.getLoopIndex()或者this.getPreNLoopIndex(0)，这2者是等价的

a组件要取到第二层循环下标：this.getPreLoopIndex()或者this.getPreNLoopIndex(1)，这2者是等价的

a组件要取到第一层循环下标：this.getPreNLoopIndex(2)

唯一要关注的就是getPreNLoopIndex这个方法，里面的数字代表了往前取多少层，数字0就代表了当前层。以此类推。

a组件要取到当前迭代对象：this.getCurrLoopObj()或者this.getPreNLoopObj(0)，这2者是等价的

a组件要取到第二层迭代对象：this.getPreLoopObj()或者this.getPreNLoopObj(1)，这2者是等价的

a组件要取到第一层迭代对象：this.getPreNLoopObj(2)

唯一要关注的就是getPreNLoopObj这个方法，里面的数字代表了往前取多少层，数字0就代表了当前层。以此类推。

具体内容请参照脚本与Java进行交互中的元数据获取方式之二。

LiteFlow支持了异步循环特性，关于异步循环请参考高级特性中的异步循环模式。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    FOR(5).DO(THEN(a, b));
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    FOR(f).DO(THEN(a, b));
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    WHILE(w).DO(THEN(a, b));
</chain>
```

Example 4 (xml):
```xml
<chain name="chain1">
    WHILE(true).DO(THEN(a, b)).BREAK(b);
</chain>
```

---

## 🥥方法级别式声明

**URL:** https://liteflow.cc/pages/797830/

**Contents:**
- 🥥方法级别式声明

LiteFlow推出了方法级别的声明特性。

方法级别式声明可以让用户在一个类中通过注解定义多个组件，更加的灵活。

如果你有非常多的组件，又同时想避免类的定义过多的问题，那这个特性非常适合这种需求。

你可以像这样来在一个bean里定义多个组件：

如果你已经阅读，从上面的示例可以看到，这里和类级别声明组件相比，多了个nodeId参数。相同的组件的方法，都标识成一样的nodeId即可。其余的规则和类级别式声明一致。

以下是一个类里定义2个组件，每个组件定义3个方法的示例：

**Examples:**

Example 1 (java):
```java
@LiteflowComponent
public class CmpConfig {

    //普通组件的定义
    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS, nodeId = "a", nodeName = "A组件", nodeType = NodeTypeEnum.COMMON)
    public void processA(NodeComponent bindCmp) {
        ...
    }

    //SWITCH组件的定义
    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS_SWITCH, nodeId = "b", nodeName = "B组件", nodeType = NodeTypeEnum.SWITCH)
    public String processB(NodeComponent bindCmp) {
        ...
    }
    
    //布尔组件的定义
    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS_BOOLEAN, nodeId = "c", nodeName = "C组件", nodeType = NodeTypeEnum.BOOLEAN)
    public boolean processC(NodeComponent bindCmp) {
        ...
    }
    
    //FOR组件的定义
    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS_FOR, nodeId = "d", nodeName = "D组件", nodeType = NodeTypeEnum.FOR)
    public int processD(NodeComponent bindCmp) {
        ...
    }
    
    //迭代组件的定义
    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS_ITERATOR, nodeId = "e", nodeName = "E组件", nodeType = NodeTypeEnum.ITERATOR)
    public Iterator<?> processE(NodeComponent bindCmp) {
        ...
    }
}
```

Example 2 (java):
```java
@LiteflowComponent
public class CmpConfig {

    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS, nodeId = "a", nodeType = NodeTypeEnum.COMMON)
    public void processA(NodeComponent bindCmp) {
        ...
    }

    @LiteflowMethod(value = LiteFlowMethodEnum.IS_ACCESS, nodeId = "a", nodeType = NodeTypeEnum.COMMON)
    public boolean isAccessA(NodeComponent bindCmp){
        ...
    }

    @LiteflowMethod(value = LiteFlowMethodEnum.ON_SUCCESS, nodeId = "a", nodeType = NodeTypeEnum.COMMON)
    public void onSuccessA(NodeComponent bindCmp){
        ...
    }

    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS_BOOLEAN, nodeId = "f", nodeType = NodeTypeEnum.BOOLEAN)
    public boolean processF(NodeComponent bindCmp) {
        ...
    }

    @LiteflowMethod(value = LiteFlowMethodEnum.IS_ACCESS, nodeId = "f", nodeType = NodeTypeEnum.BOOLEAN)
    public boolean isAccessF(NodeComponent bindCmp){
        ...
    }

    @LiteflowMethod(value = LiteFlowMethodEnum.ON_SUCCESS, nodeId = "f", nodeType = NodeTypeEnum.BOOLEAN)
    public void onSuccessF(NodeComponent bindCmp){
        ...
    }
}
```

---

## 🌵条件编排

**URL:** https://liteflow.cc/pages/e76999/

**Contents:**
- 🌵条件编排
- # IF的二元表达式
- # IF的三元表达式
- # ELSE表达式
- # ELIF表达式

LiteFlow提供了条件编排表达式组合。

条件编排是选择编排一个变种，选择编排是根据逻辑去选择多个子项中的一项。而条件编排只有真和假2个子项，这处理某些业务的过程中非常有用。

其实简单来说，条件编排就是编程语言中的if else。只不过在LiteFlow EL语法中有一些不一样的用法。

以下IF和ELIF的第一个参数要求定义布尔组件，关于如何定义请参考布尔组件这一章节。

其中x为条件节点，为真的情况下，执行链路就为x->a->b，为假链路就为x->b。

其中x为条件节点，为真的情况下，执行链路就为x->a->c，为假链路就为x->b->c。

LiteFlow也提供了ELSE表达式，IF的二元表达式+ELSE表达式等同于IF三元表达式，比如：

ELIF关键字的用法其实和java语言的else if类似，可以跟多个，和IF二元表达式参数一样，一般最后还会跟个ELSE，用于多重条件的判断：

其实写过代码的，对这个表达式应该很好理解。

值得注意的是，只有IF的二元表达式后面才能跟ELIF，如果IF三元表达式后面跟ELIF，最后一个表达式会被ELIF的表达式覆盖，就比如：

这样x1即使为false，也不会执行到b，会去判断x2。虽然框架做了容错处理，但是我们在写表达式的时候，不推荐这样写。容易造成理解上的困扰。

其实IF三元表达式已经能表达一切的可能了，有多重条件也可以不用ELIF，可以用嵌套来完成，比如：

但是官方依旧不推荐你这么写，多重嵌套在理解起来会比较吃力，所以尽量用ELIF来代替。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    THEN(
        IF(x, a),
        b
    );
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    THEN(
        IF(x, a, b),
        c
    );
</chain>
```

Example 3 (xml):
```xml
<chain name="chain1">
    IF(x, a).ELSE(b);
</chain>
```

Example 4 (xml):
```xml
<chain name="chain1">
    IF(x, a, b);
</chain>
```

---

## 🌰构造EL

**URL:** https://liteflow.cc/pages/a3cb4b/

**Contents:**
- 🌰构造EL
- # 依赖
- # 基本用法
- # 在表达式上设置子关键字
- # 在节点上设置子关键字
- # 格式化输出EL表达式
- # 目前支持的表达式和关键字
- # EL表达式参数校验

从2.11.1版本开始，你可以在代码中动态组装EL表达式，包括创建、修改、输出EL表达式。

如果需要在代码中动态构建EL表达式，需要添加以下额外依赖：

你可以通过工厂类ELBus创建任何一个EL表达式。比如对于这样一个EL表达式：

你可以在相应的地方调用子关键字，比如id,tag,bind,any等等，下面是几个例子

以上都是在表达式层面设置关键字，可能会有人疑问，如果我要在节点上设置data,tag,bind怎么办呢。

这里你需要用到ELBus.element("a")或是ELBus.node("a")。这两者的效果分别如下：

可以看到，其实ELBus.then("a")和ELBus.then(ELBus.element("a")是等价的，不同的是后者是可以设置子关键字的。

而ELBus.node("a")则是给节点外面套上了node关键字，其意义是在加载的时候不检查和降级，关于node关键字的详细可参考组件名包装以及组件降级。

其实用java去构造EL表达式的思路和书写表达式的思路是一样的。其结构几乎是完全一样的。这个相信开发者多加以试试就能举一反三。

这里只是针对几种情况做一些介绍，不会一一介绍每个方法。

容易能发现toEL()方法输出的EL表达式是一行字符串，不方便查看以及校验EL表达式是否正确。可以使用 toEL(true) 方法以树形结构输出EL表达式，以下是一个例子：

目前支持到2.13.0版本的所有EL表达式，包括其中的关键字和高级特性。当前支持的详细内容如下表：

组装表达式时会对表达式的参数类型进行校验。包括是否为单节点组件、是否允许为与或非表达式等。比如，WHILE表达式WHILE(w).DO(THEN(a, b)); 中，w需要是返回布尔值的节点或与或非表达式。

更多测试样例请在 liteflow-testcase-el/liteflow-testcase-el-builder 模块中查看。

**Examples:**

Example 1 (xml):
```xml
<dependency>
    <groupId>com.yomahub</groupId>
    <artifactId>liteflow-el-builder</artifactId>
    <version>2.15.1</version>
</dependency>
```

Example 2 (java):
```java
// 组装EL表达式
ThenELWrapper el = ELBus.then(
        "a",
		ELBus.when("b", ELBus.then("c", "d")),
		"e");
System.out.println(el.toEL());
```

Example 3 (text):
```text
THEN(a,WHEN(b,THEN(c,d)),e)
```

Example 4 (java):
```java
String el = ELBus.switchOpt("x").to(ELBus.when("a,b").id("x1"), "c").toEL();
System.out.println(el);
//输出：SWITCH(x).TO(WHEN(a,b).id("x1"),c);
```

---

## 🥜构造Node

**URL:** https://liteflow.cc/pages/5bbee3/

**Contents:**
- 🥜构造Node
- # 什么时候构造
- # 构造Node

要说明的是，构造模式和规则配置模式，其实并不是只能二选一。他们既可以单独使用，也可以结合起来使用，并不冲突。事实上，即便是规则配置模式，底层也使用了构造模式。所以，您随意就是。

建议在项目启动时构造，以下只需要构造一次。千万不要每次执行的时候都去构造！！！

你可以像以下那样构造一个普通的Node，当然在spring/springboot环境，大多数情况你无需去构建一个Node，因为只要你的组件上标有@Component/@LiteflowComponent，并且被scan到的话，组件会自动注册。

我这里只是告诉您，可以这样去通过代码去构造，如果你的组件是动态代理类而不是一个静态存在的java类，或是脚本节点，这样的构建就显得很有意义了。

这里的节点类，不需要你去声明@LiteflowComponent或者@Component，如果项目是spring体系的话，LiteFlow框架会自动的把节点类注入到spring上下文中。

所以你仍旧可以在这个类里使用@Autowired和@Resource等等之类的spring任何注解。

**Examples:**

Example 1 (java):
```java
//构建一个普通组件
LiteFlowNodeBuilder.createCommonNode().setId("a")
                .setName("组件A")
                .setClazz("com.yomahub.liteflow.test.builder.cmp.ACmp")
                .build();

//构建一个选择组件
LiteFlowNodeBuilder.createSwitchNode().setId("a")
                .setName("组件A")
                .setClazz("com.yomahub.liteflow.test.builder.cmp.ACmp")
                .build();

//构建一个普通脚本组件
LiteFlowNodeBuilder.createScriptNode().setId("a")
                .setName("组件A")
                .setScript("你的脚本")
                .build();

//构建一个脚本选择组件
LiteFlowNodeBuilder.createScriptSwitchNode().setId("a")
                .setName("组件A")
                .setScript("你的脚本")
                .build();

//构建一个脚本组件，从file载入脚本
LiteFlowNodeBuilder.createScriptNode().setId("a")
                .setName("组件A")
                .setFile("xml-script-file/s1.groovy")
                .build();
```

---

## 🧬次数循环组件

**URL:** https://liteflow.cc/pages/5f971f/

**Contents:**
- 🧬次数循环组件
- # 用法
- # 当前循环下标获取
- # 多层嵌套循环中获取下标v2.12.3+

LiteFlow提供了次数循环组件。返回的是一个int值的循环次数。 主要用于FOR...DO...表达式。

关于FOR...DO...表达式的用法，可以参考循环编排这一章。

比如要对一段表达式进行固定次数的循环操作，可以如下定义：

f节点的定义，需要继承NodeForComponent，需要实现processFor方法：

内部可以覆盖的方法和this关键字可调用的方法见组件内方法覆盖和调用这一章。

关键字FOR...DO...中DO里面的任意java组件都可以通过this.getLoopIndex()来获得当前循环层的下标。

在脚本中通过_meta.loopIndex来获取。

a组件要取到当前循环下标：this.getLoopIndex()或者this.getPreNLoopIndex(0)，这2者是等价的

a组件要取到第二层循环下标：this.getPreLoopIndex()或者this.getPreNLoopIndex(1)，这2者是等价的

a组件要取到第一层循环下标：this.getPreNLoopIndex(2)

唯一要关注的就是getPreNLoopIndex这个方法，里面的数字代表了往前取多少层，数字0就代表了当前层。以此类推。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    FOR(f).DO(THEN(a, b));
</chain>
```

Example 2 (java):
```java
@LiteflowComponent("f")
public class FCmp extends NodeForComponent {
    @Override
    public int processFor() throws Exception {
        //这里根据业务去返回for的结果
    }
}
```

Example 3 (xml):
```xml
<chain name="chain1">
    FOR(x).DO(
        FOR(y).DO(
            FOR(z).DO(
                THEN(a,b)
            )
        )
    );
</chain>
```

---

## 🍕私有投递

**URL:** https://liteflow.cc/pages/fbb938/

**Contents:**
- 🍕私有投递
- # 什么叫私有投递
- # 解决方式

在之前的介绍中已经阐述了在一个请求中，各个LiteFLow的组件都共享同一个上下文。

在一个请求中，上下文里的所有数据对这个请求链路中所有的节点都是公开的。每个组件都可以存取数据。

但是存在这样一个情况，比如我的规则是这样定义的：

在执行完组件a之后，进行了同样的5个b组件的并发。在b组件上逻辑是同一套，但是要接收5个不同的参数。

我们知道，在之前的描述中，a组件可以往上下文里放数据，其他组件可以取到a组件往上下文放的东西，但是在这个场景中，普通的存放数据是无法让b组件取到5个不同的参数来进行并发处理的。

所以为此，LiteFlow特地设计了私有投递的概念，指的是：一个组件可以显示的声明为某个特定的组件去投递1个或多个参数，而投递的参数，也只有这个特定的组件才能获取到，其他组件是获取不到的。并且这个投递的参数(一个或多个)只能被取一次。

有了这个特性，那上述的场景就可以利用私有投递的特性去解决了。

可以看到我们为b组件进行了私有投递，调用了this.sendPrivateDeliveryData方法，指定了b组件

b组件调用了this.getPrivateDeliveryData()方法，获取了a组件投递的参数。因为参数只能被获取一次（内部用队列来实现），所以保证了每个b组件获取到的参数都是不一样的。

**Examples:**

Example 1 (xml):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<flow>
    <!-- 5个相同的b组件并发执行 -->
    <chain name="chain1">
        THEN(
            a,
            WHEN(b, b, b, b, b),
            c
        );
    </chain>
</flow>
```

Example 2 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeComponent {
	@Override
	public void process() {
		System.out.println("ACmp executed!");
		DefaultContext context = this.getContextBean(DefaultContext.class);
		context.setData("testSet", new HashSet<>());

		for (int i = 0; i < 5; i++) {
			this.sendPrivateDeliveryData("b",i+1);
		}
	}
}
```

Example 3 (java):
```java
@LiteflowComponent("b")
public class BCmp extends NodeComponent {
	@Override
	public void process() {
		System.out.println("BCmp executed!");
		Integer value = this.getPrivateDeliveryData();
		//do your biz
	}
}
```

---

## 🧅类级别式声明

**URL:** https://liteflow.cc/pages/18f548/

**Contents:**
- 🧅类级别式声明
- # 普通组件的声明
- # 选择组件的声明
- # 布尔组件的声明
- # 数值循环组件的声明
- # 迭代循环组件的声明

类级别式声明主要用处就是通过注解形式让普通的java bean变成LiteFlow的组件。无需通过继承类或者实现接口的方式。

由于LiteFlow的组件常规方式下需要继承类来定义，使得你无法再继承自己业务的类了。这个特性可以解决这个问题。但是和常规组件一样，需要一个类对应一个组件。

使用者无需继承NodeComponent了，相应的方法上加上LiteflowMethod注解，即可完成对任意自定义类的组件化工作。

其中@LiteFlowMethod的作用是把你自己的定义的方法映射成组件的注解。

原本继承式组件中可以覆盖的几个方法，在类声明式组件中也可以定义，需要像这么去定义：

@LiteflowMethod上需要加上NodeTypeEnum.SWITCH参数，其他规则和普通组件一致。

@LiteflowMethod上需要加上NodeTypeEnum.BOOLEAN参数，其他规则和普通组件一致。

@LiteflowMethod上需要加上NodeTypeEnum.FOR参数，其他规则和普通组件一致。

@LiteflowMethod上需要加上NodeTypeEnum.ITERATOR参数，其他规则和普通组件一致。

← 🥭什么叫声明式组件 🥥方法级别式声明→

**Examples:**

Example 1 (java):
```java
@LiteflowComponent("a")
public class ACmp{
  
	@LiteflowMethod(LiteFlowMethodEnum.PROCESS, nodeType = NodeTypeEnum.COMMON)
	public void processAcmp(NodeComponent bindCmp) {
		System.out.println("ACmp executed!");
	}
}
```

Example 2 (java):
```java
@LiteflowComponent("a")
public class ACmp{
  
	@LiteflowMethod(LiteFlowMethodEnum.PROCESS, nodeType = NodeTypeEnum.COMMON)
	public void processAcmp(NodeComponent bindCmp) {
		System.out.println("ACmp executed!");
	}

	@LiteflowMethod(LiteFlowMethodEnum.IS_ACCESS, nodeType = NodeTypeEnum.COMMON)
	public boolean isAcmpAccess(NodeComponent bindCmp){
		return true;
	}

	@LiteflowMethod(LiteFlowMethodEnum.BEFORE_PROCESS, nodeType = NodeTypeEnum.COMMON)
	public void beforeAcmp(NodeComponent bindCmp){
		System.out.println("before A");
	}

	@LiteflowMethod(LiteFlowMethodEnum.AFTER_PROCESS, nodeType = NodeTypeEnum.COMMON)
	public void afterAcmp(NodeComponent bindCmp){
		System.out.println("after A");
	}

	@LiteflowMethod(LiteFlowMethodEnum.ON_SUCCESS, nodeType = NodeTypeEnum.COMMON)
	public void onAcmpSuccess(NodeComponent bindCmp){
		System.out.println("Acmp success");
	}

	@LiteflowMethod(LiteFlowMethodEnum.ON_ERROR, nodeType = NodeTypeEnum.COMMON)
	public void onAcmpError(NodeComponent bindCmp, Exception e){
		System.out.println("Acmp error");
	}
	
	@LiteflowMethod(LiteFlowMethodEnum.IS_END, nodeType = NodeTypeEnum.COMMON)
	public boolean isAcmpEnd(NodeComponent bindCmp) {
		return false;
	}
    
    @LiteflowMethod(value = LiteFlowMethodEnum.ROLLBACK, nodeType = NodeTypeEnum.COMMON)
    public void rollbackA(NodeComponent bindCmp) throws Exception {
        System.out.println("ACmp rollback!");
    }
}
```

Example 3 (java):
```java
@LiteflowComponent("e")
public class ECmp{

    @LiteflowMethod(value = LiteFlowMethodEnum.PROCESS_SWITCH, nodeType = NodeTypeEnum.SWITCH)
    public String processSwitch(NodeComponent bindCmp) throws Exception {
        System.out.println("Ecomp executed!");
        return "g";
    }
}
```

Example 4 (java):
```java
@LiteflowComponent("x")
public class XCmp{

	@LiteflowMethod(value = LiteFlowMethodEnum.PROCESS_BOOLEAN, nodeType = NodeTypeEnum.BOOLEAN)
	public boolean processBoolean(NodeComponent bindCmp) throws Exception {
		//do your biz
		return true;
	}
}
```

---

## 🥝组件事件回调

**URL:** https://liteflow.cc/pages/3ee755/

**Contents:**
- 🥝组件事件回调
- # 成功事件
- # 失败事件
  - # 注意点1
  - # 注意点2
  - # 注意点3

LiteFlow支持了组件事件回调。目前支持的事件有2个，组件成功事件和失败事件。

如果你在组件里覆盖了onSuccess方法，那么组件成功后会回调这个方法。

在成功事件里，你可以通过同样的方法获取到上下文。

如果你在组件中覆盖了onError方法，那么组件发生异常后会回调这个方法。

onError方法执行后，因为主方法抛出异常，所以整个流程依旧是失败状态。response对象里依旧是主方法抛出的错。

如果onError方法本身抛错，那么最终抛到最外面的错，是主方法里的错，而onError方法所产生的异常会被打出堆栈，但不会抛出。比如：

那么最终response里的异常会是NullPointerException而不是IllegalAccessException，但是IllegalAccessException这个异常会被打出堆栈信息。

onError方法执行后，afterProcess方法还会执行吗（假设都有实现）？

会的，无论是否抛出错，afterProcess方法都会被执行。

**Examples:**

Example 1 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		DefaultContext context = this.getContextBean(DefaultContext.class);
		//do your biz
	}

	@Override
	public void onSuccess() throws Exception {
		DefaultContext context = this.getContextBean(DefaultContext.class);
		//do your biz
	}
}
```

Example 2 (java):
```java
@Component("d")
public class DCmp extends NodeComponent {

	@Override
	public void process() throws Exception{
		//mock throw exception
		throw new NullPointerException();
	}

	@Override
	public void onError(Exception e) throws Exception {
		DefaultContext context = this.getContextBean(DefaultContext.class);
		//do your biz
	}
}
```

Example 3 (java):
```java
@Component("d")
public class DCmp extends NodeComponent {

	@Override
	public void process() throws Exception{
		//mock throw exception
		throw new NullPointerException();
	}

	@Override
	public void onError(Exception e) throws Exception {
		throw new IllegalAccessException("错误事件回调本身抛出异常");
	}
}
```

---

## 🛀组件内方法覆盖和调用

**URL:** https://liteflow.cc/pages/83073e/

**Contents:**
- 🛀组件内方法覆盖和调用
- # 可以覆盖的方法
  - # isAccess
  - # isContinueOnError
  - # isEnd
  - # beforeProcess和afterProcess
  - # onSuccess和onError
  - # rollback
- # This关键字可以调用的方法
  - # 获取上下文

推荐实现isAccess方法，表示是否进入该节点，可以用于业务参数的预先判断

表示出错是否继续往下执行下一个组件，默认为false

如果覆盖后，返回true，则表示在这个组件执行完之后立马终止整个流程。对于这种方式，由于是用户主动结束的流程，属于正常结束，所以最终的isSuccess是为true的。

需要注意的是，如果isContinueOnError为true的情况下，调用了this.setIsEnd(true)，那么依旧会终止。response里的isSuccess还是true。

流程的前置和后置处理器，其中前置处理器，在isAccess 之后执行。

用于执行一些前置和后置处理，但是一般这个用不上。如果是统一做组件前置和后置，推荐用切面去完成。关于切面可以参考组件切面;

流程的成功失败事件回调，详情请参考组件事件回调。

流程失败后的回滚方法，详情请参考组件回滚。

在组件节点里，随时可以通过方法this.getContextBean(clazz)获取当前你自己定义的上下文，从而可以获取任何数据。

获取当前执行的流程名称，如果有嵌套，只获取最外层那个chain。

获取当前执行的流程名称，如果有嵌套，例如chain1调用chain2，如果当前组件在chain2里，那这里获取为chain2。

表示是否立即结束整个流程 ，用法为this.setIsEnd(true)。对于这种方式，由于是用户主动结束的流程，属于正常结束，所以最终的isSuccess是为true的。

需要注意的是，如果isContinueOnError为true的情况下，调用了this.setIsEnd(true)，那么依旧会终止。response里的isSuccess还是true。

获取这个组件的标签信息，关于标签的定义和使用，请参照tag语法。

调用隐式流程，关于隐式流程的说明和用法，请参考隐式子流程。

获得bind关键字绑定的数据，关于bind关键字的用法，请参考[绑定数据]

← 🏄LiteflowComponent 🥭什么叫声明式组件→

---

## 🍪组件切面

**URL:** https://liteflow.cc/pages/2373f5/

**Contents:**
- 🍪组件切面
- # 全局切面
- # Aspect的切面

LiteFlow支持组件的切面功能，你可以通过2种方式进行

全局切面是针对于所有的组件，进行切面。你只需要做如下实现即可：

LiteFlow同时也支持了Spring Aspect的切面，你可以用@Aspect标注对任意包，任意规则内的组件进行切面

**Examples:**

Example 1 (java):
```java
@Component
public class CmpAspect implements ICmpAroundAspect {
    @Override
    public void beforeProcess(NodeComponent cmp) {
        YourContextBean context = cmp.getContextBean(YourContextBean.class);
        //before business
    }

    @Override
    public void afterProcess(NodeComponent cmp) {
        YourContextBean context = cmp.getContextBean(YourContextBean.class);
        //after business
    }

    @Override
    public void onSuccess(NodeComponent cmp) {
        //do sth
    }

    @Override
    public void onError(NodeComponent cmp, Exception e) {
        //do sth
    }
}
```

Example 2 (java):
```java
@Aspect
public class CustomAspect {

    @Pointcut("execution(* com.yomahub.liteflow.test.aop.cmp1.*.process())")
    public void cut() {
    }

    @Around("cut()")
    public Object around(ProceedingJoinPoint jp) throws Throwable {
        //do before business
        Object returnObj = jp.proceed();
        //do after business
        return returnObj;
    }
}
```

---

## 🍑组件别名

**URL:** https://liteflow.cc/pages/92ef89/

**Contents:**
- 🍑组件别名
- # Springboot & Spring 扫描方式
- # 规则文件方式定义组件
- # 打印

LiteFlow支持了组件别名的设置，一般用来填写中文名称，方便记忆的名称。

设置了组件别名，在打印出步骤信息的时候，会带上相应别名。

大多数情况下，很多人使用的都是springboot/spring框架，那么只需要做如下改变

你定义的组件中，把@Component换成@LiteflowComponent，并做如下定义：

在非spring体系的工程里，组件是需要定义在规则文件里的，那么需要做如下添加

需要在<node>节点中加入name的属性

**Examples:**

Example 1 (java):
```java
@LiteflowComponent(id = "a", name = "组件A")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		System.out.println("ACmp executed!");
	}
}
```

Example 2 (xml):
```xml
<node id="a" name="组件A" class="com.yomahub.liteflow.test.config.cmp.ACmp"/>
<node id="b" name="组件B" class="com.yomahub.liteflow.test.config.cmp.BCmp"/>
```

---

## 🐚组件名包装

**URL:** https://liteflow.cc/pages/2df3d9/

**Contents:**
- 🐚组件名包装

LiteFlow的组件名是有规范的，不能以数字开头，并且中间不能有运算符号的出现。

比如这些都是不行的：88Cmp，cmp-11, user=123。

但是有些业务中组件名你需要自动生成，会打破这个规则，怎么办呢？

LiteFlow也提供了一种组件包装语法，让你可以用任意形式的组件名。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    THEN(a, b, 88Cmp, cmp-11);
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
    THEN(a, b, node("88Cmp"), node("cmp-11"));
</chain>
```

---

## 🐋组件回滚

**URL:** https://liteflow.cc/pages/y172l7/

**Contents:**
- 🐋组件回滚
  - # 回滚触发前提
  - # 基本用法
  - # 注意事项

LiteFlow中组件对异常的处理方法有以下三种：组件中的continueOnError方法、EL表达式中设置ignoreError以及RL表达式中设置CATCH关键字。如果这三种条件均不满足并且出现了异常，那么流程就会执行失败，触发回滚的逻辑。使用rollback功能的前提需要对LiteFlow的异常处理机制具有一定的了解。

在实际应用场景中，组件的执行流程会因为各种突发情况导致失败，所以组件需要一种能在流程执行失败之后对流程进行处理的机制，因此LiteFlow新增了回滚功能。

在流程执行失败，并且存在异常时会自动触发回滚机制，回滚机制会按照已经执行的组件的逆序执行其中的rollback方法。

如果上述全部组件均重写了rollback方法，在d中出现异常， 并且执行顺序为并且执行顺序为：a -> b -> c -> d的话，回滚顺序将会是：d -> c -> b -> a。

与组件中的其他方法类似，在回滚事件中，随时可以获取自己定义的上下文。

**Examples:**

Example 1 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeComponent {

	@Override
	public void process() {
		//do your biz
	}

	@Override
	public void rollback() throws Exception {
        DefaultContext context = this.getContextBean(DefaultContext.class);
		//do your biz
	}
}
```

Example 2 (java):
```java
LiteflowResponse response = flowExecutor.execute2Resp("yourChainName", "arg");
String rollbackStepStr = response.getRollbackStepStr(); // 以字符串形式获取回滚流程
String rollbackStepStrWithTime = response.getRollbackStepStrWithTime();
Queue<CmpStep> rollbackStepQueue = response.getRollbackStepQueue(); // 获取回滚的组件的步骤信息
Map<String, List<CmpStep>> rollbackSteps = response.getRollbackSteps(); // 获取回滚组件的步骤信息
```

---

## 🐠组件异步层面的线程池

**URL:** https://liteflow.cc/pages/02b08a/

**Contents:**
- 🐠组件异步层面的线程池
- # 全局线程池
- # Chain层面的线程池
- # 表达式层面的线程池
- # 各个维度线程池的优先级
- # 默认线程池的丢弃策略

LiteFlow中有很多编排场景，都涉及到了异步。分别为：

关于这个功能的介绍请参照开启WHEN线程池隔离。

默认情况下，以上这些场景都共用一个线程池，即全局线程池。全局线程池有默认提供实现方式，可以在配置项里进行配置线程池大小和队列大小。

当然框架也提供自定义的全局线程池的实现，你需要在配置项里的配置：

你可以替换默认实现，自己实现的线程池提供类需要实现ExecutorBuilder接口：

当然你定义了自定义的线程池实现类，liteflow.global-thread-pool-size和liteflow.global-thread-pool-queue-size失效。

如果你不想所有的都用同一个全局线程池，想为某个chain单独定义线程池，就需要如下定义：

如果你这样定义了，那么这个chain内的所有异步场景，都会走你定义的线程池。

同样的，这个自定义的线程池提供类需要你来实现：

如果你还想更细化点来定义你的线程池，LiteFlow还支持表达式层面的线程池自定义关键字:

当然这里循环必须要为异步parallel(true)，如果不是异步的，那么threadPool即使加了也没任何意义。

同样的，这个自定义的线程池提供类需要你来实现：

如果全局线程池，Chain层面线程池，表达式层面线程池共存，优先级顺序依次为：

表达式层面线程池 > Chain层面线程池 > 全局线程池

这里提一嘴，在2.13.0之后的默认线程池中的队列丢弃策略是ThreadPoolExecutor.CallerRunsPolicy()。

这意味着将不会丢弃线程，如果你的并发数量特别多，建议扩大线程池大小，或者自己定义。

← 🐋FlowExecutor层面的线程池 🪶虚拟线程→

**Examples:**

Example 1 (xml):
```xml
<chain id="chain1">
    WHEN(a, b, c);
</chain>
```

Example 2 (xml):
```xml
<chain name="chain1">
   FOR(2).parallel(true).DO(THEN(a,b,c));
</chain>
```

Example 3 (xml):
```xml
<chain name="chain2">
   WHILE(x).parallel(true).DO(THEN(a,b,c));
</chain>
```

Example 4 (xml):
```xml
<chain name="chain3">
   ITERATOR(x).parallel(true).DO(THEN(a,b,c));
</chain>
```

---

## 🥠组件降级

**URL:** https://liteflow.cc/pages/79289a/

**Contents:**
- 🥠组件降级
- # 使用方法
- # 多组件类型的支持

如果你在编排时写了一个不存在的组件，通常情况下是会报错的。

比如你的系统中只定义了 A，B，C 三个组件。但是你在规则里这样写：

组件降级的意义是，当你写了一个不存在的组件时，在运行时会自动路由到你指定的降级组件上，由这个降级组件来代替你不存在的组件执行，这样就不会报错了。

首先需要在配置文件开启组件降级功能，默认是关闭的：

若想将一个组件声明为降级组件，只需要在组件上添加 @FallbackCmp 注解。 比如可以通过以下方式定义一个普通组件的降级组件 E。

当组件 D 不存在时，会降级为组件 E 运行。

如果不加 node 关键字，是不会自动路由到降级组件的，所以一定得加。

LiteFlow 不仅支持普通组件的降级，对其他组件类型也提供了支持。以下示例分别声明了一个布尔降级组件和次数循环降级组件。

当组件 x1、x2 或 x3 不存在时，会分别路由到条件降级组件、次数循环降级组件以及普通降级组件。其他类型的组件也同理。

与或非表达式也可以使用降级组件，如下的 EL 表达式：

当组件 x 不存在时会路由到条件降级组件。

目前每种类型的组件只允许定义一个降级组件。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    THEN(A, B, C, D);
</chain>
```

Example 2 (properties):
```properties
liteflow.fallback-cmp-enable=true
```

Example 3 (java):
```java
@LiteflowComponent("E")
@FallbackCmp
public class ECmp extends NodeComponent {
    @Override
    public void process() {
        System.out.println("ECmp executed!");
    }
}
```

Example 4 (xml):
```xml
<chain name="chain1">
    THEN(A, B, C, node("D"));
</chain>
```

---

## 🍿自定义组件执行器

**URL:** https://liteflow.cc/pages/46bbed/

**Contents:**
- 🍿自定义组件执行器
- # 全局组件执行器
- # 单个组件配置特殊的执行器
- # 优先级
- # 自定义执行器对于重试功能的影响

LiteFlow允许用户定义自定义组件执行器，通过这个可以在执行组件时，加入自定义代码，重写重试策略。当然其他方式也可以达到相同的目的，比如说组件切面功能。

如果你没有非常明确这个功能是干什么的，建议还是用默认的方式。(其实就是不用看此章节的意思)

对于自定义组件执行器，你可以在全局上进行替换。默认的组件执行器为：com.yomahub.liteflow.flow.executor.DefaultNodeExecutor

你可以通过以下方式替换全局默认组件执行器：

自定义组件执行器需要继承com.yomahub.liteflow.entity.executor.NodeExecutor。

除了全局执行器，单个组件也支持配置自定义执行器。

你需要在定义组件的时候，实现getNodeExecutorClass 方法：

如果全局和单个组件都配置自定义执行器的情况下，优先使用单个组件上配置的执行器。

因为重试的逻辑是在默认执行器里面实现的。所以如果你自己配置了自定义执行器，那么重试的功能需要你自己去实现。并且全局重试参数配置还有@LiteflowRetry功能标签将失效。

当然你自己实现的自定义执行器，还是可以拿到重试参数，自己写特殊的重试策略的。只不过这一切都需要自己去完成。这点要注意下。

**Examples:**

Example 1 (properties):
```properties
liteflow.node-executor-class=com.yomahub.liteflow.test.nodeExecutor.CustomerDefaultNodeExecutor
```

Example 2 (java):
```java
public class CustomerDefaultNodeExecutor extends NodeExecutor {
    @Override
    public void execute(NodeComponent instance) throws Exception {
        LOG.info("使用customerDefaultNodeExecutor进行执行");
        super.execute(instance);
      
      	//在这里你可以加入自己的代码，包括上面的代码都可以去掉
      	//但是要确保至少要调用instance.execute()，否组件就真的无法被正确执行了
    }
}
```

Example 3 (java):
```java
@LiteflowComponent("d")
public class DCmp extends NodeComponent {

    @Override
    public void process() {
        System.out.println("DCmp executed!");
    }

    @Override
    public Class<? extends NodeExecutor> getNodeExecutorClass() {
        return CustomerNodeExecutorAndCustomRetry.class;
    }
}
```

---

## 🍄说明

**URL:** https://liteflow.cc/pages/74b4bf/

**Contents:**
- 🍄说明

在执行器执行流程时会分配数据上下文实例给这个请求。不同请求的数据上下文实例是完全隔离的。里面存放着此请求所有的用户数据。不同的组件之间是不传递参数的，所有的数据交互都是通过这个数据上下文来实现的。

数据上下文这个概念在LiteFlow框架中非常重要，你所有的业务数据都是放在数据上下文中。

要做到可编排，一定是消除每个组件差异性的。如果每个组件出参入参都不一致，那就没法编排了。

LiteFlow对此有独特的设计理念，平时我们写瀑布流的程序时，A调用B，那A一定要把B所需要的参数传递给B，而在LiteFlow框架体系中，每个组件的定义中是不需要接受参数的，也无任何返回的。

每个组件只需要从数据上下文中获取自己关心的数据即可，而不用关心此数据是由谁提供的，同样的，每个组件也只要把自己执行所产生的结果数据放到数据上下文中即可，也不用关心此数据到底是提供给谁用的。这样一来，就从数据层面一定程度的解耦了。从而达到可编排的目的。关于这个理念，也在LiteFlow简介中的设计原则有提到过，给了一个形象的例子，大家可以再去看看。

一旦在数据上下文中放入数据，整个链路中的任一节点都是可以取到的。

← 🐚组件名包装 🌯数据上下文的定义和使用→

---

## ⌛️迭代循环组件

**URL:** https://liteflow.cc/pages/64262b/

**Contents:**
- ⌛️迭代循环组件
- # 用法
- # 当前迭代对象的获取
- # 多层嵌套循环中获取迭代对象v2.12.3+

LiteFlow支持了迭代循环组件，相当于Java语言的Iterator关键字，主要用于ITERATOR...DO...表达式。

关于ITERATOR...DO...表达式的用法，可以参考循环编排这一章。

x节点的定义，需要继承NodeIteratorComponent，需要实现processIterator方法：

内部可以覆盖的方法和this关键字可调用的方法见组件内方法覆盖和调用这一章。

关键字ITERATOR...DO...中DO里面所有的节点都可以通过this.getCurrLoopObj()获得迭代循环的当前对象。

在脚本中通过_meta.loopObject来获取。

a组件要取到当前迭代对象：this.getCurrLoopObj()或者this.getPreNLoopObj(0)，这2者是等价的

a组件要取到第二层迭代对象：this.getPreLoopObj()或者this.getPreNLoopObj(1)，这2者是等价的

a组件要取到第一层迭代对象：this.getPreNLoopObj(2)

唯一要关注的就是getPreNLoopObj这个方法，里面的数字代表了往前取多少层，数字0就代表了当前层。以此类推。

← 🧬次数循环组件 🏄LiteflowComponent→

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    ITERATOR(x).DO(THEN(a, b));
</chain>
```

Example 2 (java):
```java
@LiteflowComponent("x")
public class XCmp extends NodeIteratorComponent {
    @Override
    public Iterator<?> processIterator() throws Exception {
        List<String> list = ListUtil.toList("jack", "mary", "tom");
        return list.iterator();
    }
}
```

Example 3 (xml):
```xml
<chain name="chain1">
    ITERATOR(x).DO(
        ITERATOR(y).DO(
            ITERATOR(z).DO(
                THEN(a,b)
            )
        )
    );
</chain>
```

---

## ✂️选择组件

**URL:** https://liteflow.cc/pages/c0f5d7/

**Contents:**
- ✂️选择组件
- # 根据nodeId进行选择
- # 根据表达式的id进行选择
- # 根据tag进行选择v2.9.0+
- # 表达式tag的选择v2.10.2+
- # 链路tag的选择v2.10.3+
- # 拿到当前Target节点列表v2.15.0+

在实际业务中，往往要通过动态的业务逻辑判断到底接下去该执行哪一个节点，这就引申出了选择节点，选择节点可以用于SWITCH关键字中。

关于SWITCH表达式的用法，可以参考选择编排一章。

选择节点a需要继承NodeSwitchComponent。

需要实现方法processSwitch方法。

这个方法需要返回String类型，就是具体的结果，以下代码示例了选择到了c节点。

如果我要a组件要选择到后面那个表达式，那么必须在后面那个表达式后面添加id表达式，赋值一个名称。然后你的a组件就直接返回w1就可以了。

关于tag(标签)的概念，请参照tag语法这一章。

LiteFlow支持对tag的选择，如果你想选择c组件，a组件可以返回c，也可以返回tag:dog。

选择节点的内部可以覆盖的方法和this关键字可调用的方法见组件内方法覆盖和调用这一章。

LiteFlow支持了表达式的tag选择，比如：

a中返回tag:w1或者:w1就能选择到后面的表达式。

事实上，a无论返回sub还是tag:w1都能选择到后面的链路。

你可以在选择组件中通过this.getTargetList()来拿到当前目标节点的Id列表。

**Examples:**

Example 1 (xml):
```xml
<chain name="chain1">
    SWITCH(a).to(b, c);
</chain>
```

Example 2 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeSwitchComponent {

    @Override
    public String processSwitch() throws Exception {
        System.out.println("Acomp executed!");
        return "c";
    }
}
```

Example 3 (xml):
```xml
<chain name="chain1">
    SWITCH(a).to(b, WHEN(c,d).id("w1"));
</chain>
```

Example 4 (java):
```java
@LiteflowComponent("a")
public class ACmp extends NodeSwitchComponent {

    @Override
    public String processSwitch() throws Exception {
        System.out.println("Acomp executed!");
        return "w1";
    }
}
```

---

## 🥑隐式子流程

**URL:** https://liteflow.cc/pages/80e873/

**Contents:**
- 🥑隐式子流程

隐式子流程在2.15.0这个版本中做了改版。和之前版本的有些许的不一样。

LiteFlow支持在一个节点里通过代码调用另外一条流程， 这个流程关系在规则文件中并不会显示。所以这里称之为隐式调用。

主流程和隐式子流程共同享有同一个上下文的数据。所以隐式子流程里也完全可以拿到这个请求中的所有数据。

值得注意的是，隐式子流程里的组件获得请求参数，同样是通过this.getRequestData()方法。这点和之前的版本有些不一样。

**Examples:**

Example 1 (java):
```java
@Component("g")
public class GCmp extends NodeComponent {

	@Override
	public void process() throws Exception {
		LiteflowResponse response = this.invoke2Resp("otherChainId", "requestData");
		if (!response.isSuccess()){
		    throw response.getCause();
		}
	}
}
```

---
