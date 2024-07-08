Vue
##########

| Vue 单文件组件 (Single-File Component，缩写为 SFC)。SFC 是一种可复用的代码组织形式，它将 **从属于同一个组件的 HTML、CSS 和 JavaScript 封装** 在使用 ``.vue`` 后缀的文件中。
| Vue 的核心功能是 ==声明式渲染== ：通过扩展于标准 HTML 的模板语法，我们可以根据 JavaScript 的状态来描述 HTML 应该是什么样子的。当状态改变时，HTML 会自动更新。


**安裝工具**

.. code-block:: bash
    :caption: install vue-cli

    $ npm install -g @vue/cli  # 全局安装
    $ vue --version
    @vue/cli 5.0.8

.. code-block:: bash
    
    $ vue create vue_demo  # 不支持大写
    # 初始化项目 

    $ cd vue_demo
    $ npm run serve  # 运行服务


`重新启用被弃用的TypeScript Vue Plugin (Volar)拓展  <https://github.com/vuejs/language-tools/issues/4205>`_


项目配置 & ``*.vue``
******************************

.. code-block:: none
    :caption: directory

    vue_demo
    ├── public
    ├── src  # !!! 源码文件
    │   ├── assets  # 存放静态资源
    │   │   ├── .css
    │   │   └── .png
    │   ├── components  # 公共组件
    │   │   └── .vue
    │   ├── App.vue  # 主入口的组件
    │   └── main.js  # 程式入口
    ├── ...  # 不重要
    ├── package.json
    └── package-lock.json 

每一个 \*.vue 文件都由三种顶层语言块构成：<template>、<script> 和 <style>，以及一些其他的自定义块

.. grid:: 2

    .. grid-item::
        .. code-block:: html
            :caption: template.vue

            <template>
            写html
            </template>

            <script>
            业务逻辑
            </script>

    .. grid-item::

        为了高亮显示，之后会拆，因为rst 不支持 ``.vue`` 的解析

        .. code-block:: html
            :caption: .<template>
            
            <!-- 写html -->


        .. code-block:: js
            :caption: .<script>

            // 组件逻辑 
            // 此处声明一些响应式状态

package management ``package.json``
==================================================

==npm== 是前端开发人员广泛使用的包管理工具，项目中通过 ==package.json== 来管理项目中所依赖的 npm 包的配置。

.. code-block:: json
    :caption: package.json

    {
        "name": "Your project name",
        "version": "1.0.0",
        "description": "Your project description",
        "main": "app.js",
        "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1",
        },
        "author": "Author name",
        "license": "ISC",
        "dependencies": {
            "dependency1": "^1.4.0",
            "dependency2": "^1.5.2"
        }
    }


**Ref**

- `深入浅出package.json <>`_


模版语法
**********

.. note:: Options API
    | Vue 的组件可以按两种不同的风格书写：选项式 API 和组合式 API。
    | ==Options API== : 用包含多个选项的对象来描述组件的逻辑，例如 data、methods 和 mounted。选项所定义的属性都会暴露在函数内部的 this 上，它会指向当前的组件实例。

.. note:: 指令是由 ``v-`` 开头的一种特殊 attribute。

.. danger:: Single-File Component 的意义

    ``*.vue`` 是单文件组件，一个 vue 文档就是一个组件。

    - ``this`` 来访问组件实例。组件实例会暴露 ``data`` 中声明的数据属性。我们可以通过改变这些属性的值来更新组件状态。

.. danger:: 变量在 ``*.vue`` 上被引用 (Options API)

    .. grid:: 2

        .. grid-item::

            .. code-block:: js
                :caption: <script>

                export default{
                    name: "componentA"  // 组件的名字以便被引用
                    data(){
                        return{  // 暴露出去被别的引用
                            var: value, // 直接
                            
                        }
                    },
                    methods:{ // 放函数的地方
                        /*
                        在事件中, 读取data里的属性, 需要 this.属性
                        */
                        func(){
                            this.var = xxx  
                        },
                        fun(arg){
                        },
                    }
                }
    
        .. grid-item::

            .. code-block:: html
                :caption: <template>

                {{var}}  <!-- 双大括号 -->






.. code-block:: js
    :caption: <script>

    export default{
        data(){
            // 该组件暴露的数据
        },
        method:{
            // 该组件暴露的函数
        },
        computed:{
            // 计算属性。
            // 使用 computed 选项声明一个响应式的属性，它的值由其他属性计算而来：
        },
        components:{
            // 挂载组件
        },
        props:{
            // 暴露给父组件的
            // 接受父组件的数据
        },
        emits:[ 
            // 暴露给父组件
            // 发给父组件的数据
        ]
    }


js & html & css 绑定数据
========================================

配合 js 的 ``data()`` 

- ``{{content}}`` 文本
- ``<.. v-html="content"></..>`` 富 html 
- ``<.. v-bind:attri="attri_v"></..>`` & ``<.. :attri="attri_v"></..>`` 属性

.. code-block:: html
    :caption: <template>

    <!-- 传内容 -->
    <div>Header:: {{ header }}</div>  <!-- raw 文本形式 -->
    <div v-html="header"></div>  <!-- html 编译 -->

    <!-- 传代码 -->
    <div v-bind:id="dynamicId"></div>  <!-- 以 动态传属性 id 为例 -->
    <div :id="dynamicId"></div>        <!-- 可简写忽略 v-bind -->
    <h1 :class="red">Make me red</h1>  <!-- 绑定 js传过来的格式 来改颜色 -->

.. grid:: 2

    .. grid-item::
        .. code-block:: js
            :caption: <script>

            export default{
                data(){  // 配合 data() 里的 return 设置数据
                    return{
                        header: "<h1>Message</h1>",
                        dynamicId: 111,
                        red:"red"  // 绑定 css 的格式
                    }
                }
            }
    
    .. grid-item::
        .. code-block:: css
            :caption: <style>

            .red{
                color : red;
            }


**解析js 表达式**

会在当前活动实例的数据作用域下作为 javascript 被解析。但是每个绑定只能包含 **单个表达式**

.. grid:: 2

    .. grid-item::
        .. code-block:: html
            :caption: succeded

            {{ number + 1 }}
            {{ ok ? "Yes" : "No" }}

    .. grid-item::
        .. code-block:: html
            :caption: failed

            {{ var a = 1 }}  // 语句 not 表达式
            {{ if (ok) {return message}  // 流程控制    

监听事件
====================

``v-on:event="func"`` & 简写 ``@event="func"`` 指令监听 DOM 事件

==HTML DOM 事件== 允许 JavaScript 在 HTML 文档中的元素上注册不同的事件处理程序。事件通常与函数结合使用，在事件发生之前函数不会被执行（例如当用户单击按钮时）。

`HTML DOM 事件 <https://www.w3school.com.cn/jsref/dom_obj_event.asp>`_

.. hint:: 可以直接在里面写一些简单 js 语句

    .. grid:: 2

        .. grid-item::

            .. code-block:: html
                :caption: <template>

                <button @="counter += 1">Click: {{counter}}</button>

        .. grid-item::

            .. code-block:: js
                :caption: <script>

                export default{
                    data(){
                        return{
                            counter = 0,
                        }
                    }
                }

.. note:: 带参数的话

    .. grid:: 2

        .. grid-item::

            .. code-block:: html
                :caption: <template>

                <button @="func(arg)">Click: {{this.message}}</button>

        .. grid-item::

            .. code-block:: js
                :caption: <script>

                export default{
                    data(){
                        return{
                            message = ""
                        }
                    },
                    methods:{
                        func(arg){
                            this.message = arg
                        }
                    }
                }

**常见：**

- ``click`` 单击

.. hint:: Example：点击按钮会+1

    .. grid:: 2

        .. grid-item::

            .. code-block:: js
                :caption: <script>

                export default{
                    data(){
                        return{
                            count:0
                        }
                    },
                    methods: {
                        increment(){
                            this.count++; 
                            // 访问该组件 data 里的 count
                            console.log(this.count)
                        }
                    }
                }

        .. grid-item::

            .. code-block:: html
                :caption: <template>     

                <button @click="increment">  
                    <!-- 点击绑定计数+1的函数 --> 
                    click: {{count}}
                </button>


双向数据绑定
====================

``v-model="绑定的值"`` 在 ``<textarea/>``, ``<input/>``, ``<select/>`` 元素上创建双向数据绑定。他会根据控件类型自动选取正确的方法自动更新数据，并在某种极端场景下进行一些特殊处理。

.. danger:: ``v-model`` 是实时同步的。实时同步消耗很大 !!!!
    | 绑定的数据会随输入进行实时更新。
    | 添加 ``.lazy`` 修饰符，从而转为在 change 事件之后在进行同步。

    .. table::

        +--------+------+
        |ele     |change|
        +========+======+
        | input  | 回车 |
        +--------+------+
        |textarea|      |
        +--------+------+
        |select  |      |
        +--------+------+

**修饰符**

    - ``.lazy`` 不实时同步
    - ``.trim`` 过滤输入首尾空白字符

.. hint:: Example: 输入框

    .. grid:: 2

        .. grid-item::

            .. code-block:: js
                :caption: <script>

                export default{
                    data(){
                        return{
                            input: ""
                        }
                    }    
                }

        .. grid-item::

            .. code-block:: html
                :caption: <template>     

                <input v-model.lazy="input" placeholder="Type in"/>
                <!-- 添加 lazy 修饰符 -->
                <p>
                    the content you typed is "{{input}}"
                </p>
            
            .. image:: ./pics/v-model_1.png



条件渲染
====================

1. ``v-if="condition"`` & ``v-else`` & ``v-else-if``
2. ``v-show="condition"``

.. danger:: ``v-if`` & ``v-show``

    .. table:: 

        +------+--------------------------+--------+------------+----------------+
        |      |                          |切换开销|初始渲染开销|选择            |
        +======+==========================+========+============+================+
        |v-if  |真渲染，假销毁            |高      |低          |运行条件很少改变|
        +------+--------------------------+--------+------------+----------------+
        |v-else|all渲染，只是基于css不显示|低      |高          |频繁地切换      |
        +------+--------------------------+--------+------------+----------------+

    ``v-if`` ： 真正的条件渲染。确保在 ``condition=True|False`` 的切换过程中，条件块内的事件监听 & 子组件 适当地被销毁和重建

.. grid:: 2

    .. grid-item::

        .. code-block:: html
            :caption: v-if <template>

            <span v-if="condition">
                <button @click="change_condition">
                    condition
                </button>
                <p>HelloWorld</p>
            </span>
            <button @click="change_condition">
                condition
            </button>
        
        .. figure:: ./pics/v-if_1.png
            
            when condition = true
        
        .. figure:: ./pics/v-if_2.png
            
            when condition = false
            
            整一块都没被渲染

    .. grid-item::

        .. code-block:: html
            :caption: v-show <template>

            <span v-show="condition">
                <button @click="change_condition">
                    condition
                </button>
                <p>HelloWorld</p>
            </span>
            <button @click="change_condition">
                condition
            </button>

        .. figure:: ./pics/v-show_1.png
            
            when condition = true
        
        .. figure:: ./pics/v-show_2.png
            
            when condition = false
            
            基于 css display = None


.. hint:: Example: 按钮修改条件真假，然后条件渲染

    .. grid:: 2

        .. grid-item::
            .. code-block:: js
                :caption: <script>

                export default{
                    data(){
                        return{
                            condition:true
                            }
                    },
                    methods:{
                        change(){
                            this.condition = !this.condition
                            }
                    }
                }

        .. grid-item::
            .. code-block:: html
                :caption: <template>     

                <button @click="change">TorF</button>
                <p v-if="condition">T</p>
                <p v-else>F</p>


列表渲染
==========

.. code-block:: html
    
    <li v-for="item in items" :key="item.id|idx">
        {{item.attr}}
    </li>

**维护状态：**

| 当更新使用 ``v-for`` 渲染的元素列表时，默认使用 **就地更新** 策略，如果使用数据项的顺序被改变，vue 不会移动 DOM 元素来匹配数据项的顺序，而是就地更新 DOM 元素，并且确保它们在每个索引位置正确渲染。
| 为了给 Vue 一个提示以便它跟踪每个节点的身份，从而重用和重新排序现有元素，需要为每项提供唯一的 ``key`` attribute.

.. hint:: ``:key`` 的取值

    看似是需要 index, 但其实业务上来说 都是从数据库拿或者将要存到数据库，都会有唯一的 ID.

.. hint:: Example: Todo list

    .. image:: ./pics/todo.png

    .. hint:: ``array.push(item)`` & ``array.filter(func)``

    .. code-block:: js
        :caption: <script>

        let id = 0  // 初始化唯一索引
        export default {
            data() {
                return {
                    newTodo: '',
                    hideCompleted: false,  // 决定是否展示全部
                    todos: [{ 
                        id: id++, 
                        text: 'todo', 
                        done: false }]
                }
            },
            methods: {
                addTodo() {
                    this.todos.push({ 
                        id: id++, 
                        text: this.newTodo, 
                        done: false });
                    this.newTodo = '';
                },
                removeTodo(todo) {
                    this.todos = this.todos.filter((t) => t !== todo);
                }
            },
            computed: {
                filteredTodos() {
                    return  // 如果是hide那就是filter出来 否则就是原本
                        this.hideCompleted ?
                        this.todos.filter((t) => !t.done) : this.todos
                }
            },
        }


    .. code-block:: html
        :caption: <template>  

        <form @submit.prevent="addTodo">  <!--表单用来提交--> 
            <input v-model="newTodo"><button>add Todo</button>
        </form>
        <ul>
            <li v-for="todo in filteredTodos" :key="todo.id">
            <input type="checkbox" v-model="todo.done">
            <span :class="{done: todo.done}"> {{todo.text}}</span>
            <button @click="removeTodo(todo)">x</button>
            </li>
        </ul>
        <button @click="hideCompleted = !hideCompleted">
            <!--按一下改变原来的值-->
            {{hideCompleted ? "show all" : "hide completed" }}
            <!--条件判断切换按钮的文字-->
        </button>

    .. code-block:: css
        :caption: <style>  

        .done{
            text-decoration: line-through;
        }


生命周期
==========

.. grid:: 2

    .. grid-item::
        每个 Vue 组件实例在创建时都需要经历一系列的初始化步骤，比如设置好数据侦听，编译模板，挂载实例到 DOM，以及在数据改变时更新 DOM。在此过程中，它也会运行被称为生命周期钩子的函数，让开发者有机会在特定阶段运行自己的代码。

    .. grid-item::

        .. image:: ./pics/lifecycle.png

最常用的是 ``mounted`` 、``updated`` 和 ``unmounted`` 。

==模板引用== 指向模板中一个 DOM 元素的 ref。``<dom ref="ref_name">``

| 通过这个特殊的 ref attribute 来实现模板引用，指向某特定的 DOM 元素。
| 此元素将作为 ``this.$refs.ref_name`` 暴露在 ``this.$refs`` 上。然而， **只能在组件挂载之后访问它**

.. danger:: 避免用箭头函数来定义生命周期钩子，因为如果这样的话你将无法在函数中通过 this 获取组件实例。

    所有生命周期钩子函数的 ``this`` 上下文都会自动指向 **当前调用它的组件实例**。

.. hint:: 添加一个 mounted 钩子，然后通过 ``this.$refs.pElementRef`` 访问 ``<p>``，并直接对其执行一些 DOM 操作。(例如修改它的 textContent)。

    .. code-block:: js
        :caption: <script>   

        export default {
            mounted() {
                // 此时组件已经挂载。
                this.$refs.pElementRef.textContent = "Mounted"
            }
        }

    .. code-block:: html
        :caption: <template> 

        <p ref="pElementRef">Hello</p>


侦听器
==========
``watch``


.. hint:: 有些情况下，我们需要在状态变化时执行一些“副作用”
    
    | 例如更改 DOM，或是根据异步操作的结果去修改另一处的状态。
    | 监听数据变化并执行相应的操作,如发送 API 请求、更新 UI 等。
    | 实现一些复杂的逻辑,如防抖、节流等。
    | 实现数据的联动效果,当一个数据变化时,触发对其他数据的更新。

.. note:: 侦听器与计算属性的区别:
    | 计算属性用于根据现有数据衍生出新的数据,而侦听器用于在数据变化时执行副作用操作。
    | 计算属性的值是基于它依赖的数据实时计算出来的,而侦听器是异步执行的。

.. hint::  当 ID 改变时抓取新的数据。

    .. grid:: 2

        .. grid-item::
            | 在右边的例子中就是这样一个组件。该组件被挂载时，会从模拟 API 中抓取 todo 数据，同时还有一个按钮可以改变要抓取的 todo 的 ID。
            | 现在，尝试实现一个侦听器，使得组件能够在按钮被点击时抓取新的 todo 项目。
        .. grid-item::
            .. image:: ./pics/todo_1.png

    .. code-block:: js
        :caption: <script> 

        export default {
            data() {
                return {
                    todoId: 1,
                    todoData: null
                }
            },
            methods: {
                async fetchData() {
                    this.todoData = null
                    const res = await fetch(
                    `https://jsonplaceholder.typicode.com/todos/${this.todoId}`
                    )
                    this.todoData = await res.json()
                }
            },
            mounted() {this.fetchData()},
            watch:{
                todoId(){
                    this.fetchData()
                }
            }
        }

    .. code-block:: html
        :caption: <template> 

        <p>Todo id: {{ todoId }}</p>
        <button @click="todoId++" :disabled="!todoData">Fetch next todo</button>
        <p v-if="!todoData">Loading...</p>
        <pre v-else>{{ todoData }}</pre>



父组件 & 子组件
====================

真正的 Vue 应用往往是由嵌套组件创建的。 父组件可以在模板中渲染另一个组件作为子组件。 

通常一个应用会以 **一棵嵌套的组件树** 来组织。


.. grid:: 2

    .. grid-item::

        .. code-block:: js
            :caption: parent.<script>

            import ComponentA from './components/Component.vue'  // 1. 引入组件

            export default{
                components:{
                    ComponentA,  // 2. 挂载组件
                }
            }

        .. code-block:: html
            :caption:  parent.<template>

            <ComponentA/>  // 3. 显示使用组件

    .. grid-item::

        .. code-block:: js
            :caption:  child.<script>

            export default{
                name: "ComponentA",  // 子组件的名字
            }

    

.. mermaid::

    flowchart LR

    A[父组件]
    B[子组件]
    A --"props + :属性传递数据"--> B
    B --"emit + @监听触发事件"--> A


``this.$emit()`` 的第一个参数是事件的名称。其他所有参数都将传递给事件监听器。

.. hint:: props 传递数据

    .. grid:: 2

        .. grid-item::

            .. code-block:: js
                :caption: ChildComp.vue <script> 

                export default {
                    props: {
                        msg: String  
                        // 在props声明 而不是data
                    }
                }

            .. code-block:: html
                :caption: ChildComp.vue <template> 

                <h2>{{ msg || 'No props passed yet' }}</h2>

        .. grid-item::

            .. code-block:: js
                :caption: ParentComp.vue <script> 

                import ChildComp from './ChildComp.vue'  // 导入

                export default {
                    components: {ChildComp},  // 注册
                    data() {
                        return {
                            greeting: 'Hello from parent'
                        }
                    }
                }

            .. code-block:: html
                :caption: ParentComp.vue <template> 

                <!--用dom形式使用子组件-->
                <ChildComp :msg="greeting"/> 
                <!--用属性的方式传过去-->



.. hint:: emit 触发事件

    .. grid:: 2

        .. grid-item::

            .. code-block:: js
                :caption: ChildComp.vue <script> 

                export default {
                    emits: ['response'],
                    created() {  // 生命周期函数
                        this.$emit('response', 'hello from child')
                        // 发送 response
                    }
                }

            .. code-block:: html
                :caption: ChildComp.vue <template> 

                <h2>Child component</h2>

        .. grid-item::

            .. code-block:: js
                :caption: ParentComp.vue <script> 

                import ChildComp from './ChildComp.vue'

                export default {
                    components: {ChildComp},
                    data() {
                        return {
                            childMsg: 'No child msg yet'
                        }
                    }
                }

            .. code-block:: html
                :caption: ParentComp.vue <template> 

                <ChildComp @response="msg => childMsg=msg"/>
                <!--监听response-->
                <p>{{ childMsg }}</p>
插槽
==========

links
**********

`vuejs tutorial <https://vuejs.org/tutorial/#step-1>`_