javascript
####################


变量 & 对象
********************

.. note:: 变量 & 对象

    对象可以直接修改整个，也可以修改单个属性值，可以动态添加属性

    .. code-block:: js

        let var = "aaa"  // 创建变量
        let obj = {  // 创建对象
            name: "aaa",  // 属性用冒号
            size: 123,
            bool: true,
        }

``var`` & ``let`` & ``const`` 
========================================

.. danger:: 变量提升 hoisting
    一种 JavaScript 机制，其中 **变量和函数声明** 在代码执行之前被移动到其作用域的顶部。

    只是 ==声明== ，并不包括初始化。

    .. danger:: 变量声明 & 变量初始化

        .. grid:: 2

            .. grid-item:: 
                .. code-block:: js

                    var a = 222;  // 变量声明 + 初始化

            .. grid-item:: 
                .. code-block:: js

                    var a;  // 变量声明
                    a = 222;  // 变量初始化

.. table::

    +------------+-----------------+----------------+------------------------+
    |            | ``var``         | ``let``        | ``const``              |
    +============+=================+================+========================+
    |作用域 scope|全局 or 函数体内 |      块作用域 ``{}``                    |
    +------------+-----------------+----------------+------------------------+
    |重新声明    |✅               |❌              |❌                      |
    +------------+-----------------+----------------+------------------------+
    |重新更新    |✅               |✅              |❌，但是可以更新对象属性|
    +------------+-----------------+----------------+------------------------+
    |变量提升    |✅               |✅              |✅                      |
    +------------+-----------------+----------------+------------------------+
    |独自声明    |✅               |✅              |❌必须初始化            |
    +------------+-----------------+----------------+------------------------+
    |变量提升时  |✅               |❌              |❌                      |
    +------------+                 +                +                        +
    |进行初始化  |``undefined``    |                |                        |
    +------------+-----------------+----------------+------------------------+
    |notes       |                 |                |保持恒定值              |
    +------------+-----------------+----------------+------------------------+

`Var、Let 和 Const 有什么区别？ <https://www.freecodecamp.org/chinese/news/var-let-and-const-whats-the-difference/>`_

.. note:: ``let`` is better than ``var``

    | 同一个变量名 使用 ``var`` 可以重新声明，所以可能会忘记在曾经声明的，影响到其他部分，导致错误。
    | 同一个变量名 使用 ``let`` 在同一作用域不可以重新声明，在不同作用域可以再次声明，但仅存在其作用域，不会影响别的


.. grid:: 2

    .. grid-item:: 

        .. code-block:: js

            var a = "a";
            var t =4;
            if (t>3) {
                var a = 'A';  
                // 不算函数体内，重新声明&更新了 A
            };
            console.log(a)  // A

        .. code-block:: console

            A  # 更新了全局的 a
            A

    .. grid-item:: 

        .. code-block:: js

            var a = "a";
            var t =4;
            if (t>3) {
                let a = 'A';
                console.log(a)
            };
            console.log(a)  

        .. code-block:: console

            A  # 只在块内
            a 

.. grid:: 2

    .. grid-item:: 

        .. code-block:: js
            :caption: 在同一作用域内，let 不能重新声明

            let a = "a";
            let a = 'A'

        .. code-block:: console

            SyntaxError: 
            Identifier 'a' has already been declared

    .. grid-item:: 

        .. code-block:: js
            :caption: 在不同作用域内, 同一个变量名可以被let重新声明

            let a = "a";
            var t =4;
            if (t>3) {
                let a = 'A';
                console.log(a)
            };

        .. code-block:: console

            A
            
.. grid:: 2

    .. grid-item::
        .. code-block:: js
            :caption: var 提升

            console.log(a);
            var a = 'a';

        .. code-block:: console

            undefined
    
    .. grid-item::
        .. code-block:: js
            :caption: var 提升 等同于
            :emphasize-lines: 2

            var a;
            a = 'undefined';
            console.log(a);
            a = 'a';

    .. grid-item::
        .. code-block:: js
            :caption: let 提升

            console.log(a);
            let a = 'a';

        .. code-block:: console

            ReferenceError: 
            Cannot access 'a' before initialization
    
    .. grid-item::
        .. code-block:: js
            :caption: let 提升 等同于

            let a;
            console.log(a);
            a = 'a';

    .. grid-item::
        .. code-block:: js
            :caption: const 不能更新变量

            const a = 'a';
            a = 'A'  // 不能更新
            console.log(a);

        .. code-block:: console

            TypeError: Assignment to constant variable.

    .. grid-item::
        .. code-block:: js
            :caption: const 能更新对象属性

            const a = {
                name:'a',
            };
            a.name = 'A'
            console.log(a);


        .. code-block:: console

            { name: 'A' }

URL object
====================

| 在过去，在出现 URL 对象之前，人们使用字符串作为 URL。
| 而现在，URL 对象通常更方便，但是仍然可以使用字符串。在很多情况下，使用字符串可以使代码更短。
| 如果使用字符串，则需要手动编码/解码特殊字符。

.. grid::2

    .. grid-item::
        .. code-block:: js

            new URL(url, [base])  // New

            let url1 = new URL('https://base.dddd/url');
            let url2 = new URL('/url', 'https://base.ddd');
            console.log(url1)
            console.log(url2)

    .. grid-item::
        .. code-block:: console

            URL {  
                # 一摸一样的结果，所以只放一个
                href: 'https://base.dddd/url',
                origin: 'https://base.dddd',
                protocol: 'https:',
                username: '',
                password: '',
                host: 'base.dddd',
                hostname: 'base.dddd',
                port: '',
                pathname: '/url',
                search: '',
                searchParams: URLSearchParams {},
                hash: ''
                }

.. grid:: 2

    .. grid-item::
        .. figure:: https://zh.javascript.info/article/url/url-object.svg
            
            URL  组件

    .. grid-item::

        - ``href`` 是完整的 URL 与 ``url.toString()`` 相同
        - protocol 以冒号字符 ``:`` 结尾
        - search —— 以问号 ``?`` 开头的一串参数
        - hash 以哈希字符 ``#`` 开头
        - 如果存在 HTTP 身份验证，则这里可能还会有 ``user`` 和 ``password`` 属性：http://login:password@site.com（图片上没有，很少被用到）。

`URL 对象 <https://zh.javascript.info/url>`_

数组
==========

- ``arr.push(x)`` 末尾添加
- ``arr.unshift`` 头部添加
- ``arr.splice(start, delcount, x1, x2)`` 插入中间指定位置

    - ``start`` 要插入的起始位置
    - ``delcount`` 要删除原数组元素的个数

数字
==========

- ``++`` ; ``--`` 自增自减。

    - 放前面的话 先操作再用；放后面的话 先用再操作

操作符
**********

逻辑运算符
==========

- ``&&`` and ``||`` or
- ``!`` 取反
 
.. note:: ``==`` 等于 & ``===`` 绝对等于

    - ``==`` 等于 只管 **值**
    - ``===`` 绝对等于 不仅管 **值** ， 还管 **类型**

    .. code-block:: js

        let num = 2;
        let str = '2';

        num == str  // true 
        num === str  // false

if - for
==========

.. code-block:: js

    if(condition){
        // true
    }else{
        // false
    }


    for(let i=0; i<3; i++){
        // for-loop
    }



Array
**********

``.filter(func)``: 创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。

遍历删除指定元素