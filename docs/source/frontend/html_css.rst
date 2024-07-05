
# HTML & CSS 一些用过的部件

## Grid

这个 grid 的部件能实现 把页面分成几个网格，然后并排展示

.. code-block:: html


    <div class="grid" style="grid-template-columns: repeat(3, 1fr) !important;" markdown>
    <figure markdown="span" style="grid-column-start: 1; grid-column-end: 3;">![](./pics/LSTM_3.webp)</figure>
    <p style="grid-column-start: 3; grid-column-end: 4;">展示效果：左图右字，分了3格，左图占2， 右字占1</p>
    </div>

**展示：**

<div class="grid" style="grid-template-columns: repeat(3, 1fr) !important;" markdown>
<figure markdown="span" style="grid-column-start: 1; grid-column-end: 3;">![]()</figure>
<p style="grid-column-start: 3; grid-column-end: 4;">展示效果：左图右字，分了3格，左图占2， 右字占1</p>
</div>

**可能用到的链接：**

- [grid-template-columns](https://css-tricks.com/almanac/properties/g/grid-template-columns/)



## html 

## 理论

.. danger:: 从左到右 从上到下 从外到内


**常用的标签**

- 双标签

    - ``<div></div>`` 竖着排 ``<span></span>`` 横着排
    - ``<button></button>``

- 单标签

    - ``<input type="checkbox/text/number" place-holder="占位符">``

### DOM


==DOM 文档对象模型, Document Object Model== 是一个用于表示和交互网页的标准API。它将 HTML、XML 等文档表示为一个树状结构,每个节点都是文档的一部分。

.. note:: 整个 HTML 文档被表示为一个 DOM 树结构。每个 HTML 标签都对应一个 DOM 元素节点。这些节点以树状的方式组织在一起,形成 DOM 树。

- ==DOM 元素== 是 DOM 树中的基本单位。

    DOM 元素有各种属性和方法,可以用来访问和操作它们。

    .. hint:: <span> 标签在 HTML 中定义了一个行内元素,它就是一个 DOM 元素。


### form

- ``<form @submit.prevent="func"></form>``

    ``form`` 的提交默认行为是提交后刷新页面，为了阻止它提交刷新 ``.prevent``，而是只需执行 ``func``

#### input

- ``placeholder`` 占位符，当绑定的字符串为空 🟰 没有输入的时候，就会展示，但不会影响真实的值。

## css

| ``<span class={class1: condition>`` 
| 如果 ``condition=true``，则 ``class1`` 类名会被应用到 ``<span>`` 元素上。否则,该类名不会被应用。


.. code-block:: html

    <div>This is general box</div> <!--内置的div-->
    <div class="box1">self-defined box1</div> 
    <!--div为基础新的box1类-->

    <style>
        div { /*内置的类不需要加点*/
            background-color: blue;
            color: white;
        }
        .box1 { /* 自定义的类前面要加点 */
            background-color: red;
        }
    </style>

### padding & margin

在 margin 不起作用的时候加 padding。
加了 padding 之后 不想外面的盒子太大，就加上 box-sizing

.. danger:: 盒子的高度 = padding 内边距 + height 实际高度 

.. grid:: 2

    .. grid-item:: 

        .. code-block:: css

            .box1{
                margin-top: 30px;
            }

    .. grid-item:: 

        .. code-block:: css
            
            .box1{
                padding: 30px;
                box-sizing: border-box
            }