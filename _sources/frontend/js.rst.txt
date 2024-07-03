
# javascript

- ``let`` 创建变量和对象

.. note:: 变量 & 对象

    对象可以直接修改整个，也可以修改单个属性值，可以动态添加属性

    .. code-block:: js

        let var = "aaa"  // 创建变量
        let obj = {  // 创建对象
            name: "aaa",  // 属性用冒号
            size: 123,
            bool: true,
        }


### 数组

- ``arr.push(x)`` 末尾添加
- ``arr.unshift`` 头部添加
- ``arr.splice(start, delcount, x1, x2)`` 插入中间指定位置

    - ``start`` 要插入的起始位置
    - ``delcount`` 要删除原数组元素的个数

### 数字

- ``++`` ; ``--`` 自增自减。

    - 放前面的话 先操作再用；放后面的话 先用再操作

## 操作符

### 逻辑运算符

- ``&&`` and ``||`` or
- ``!`` 取反
.. note:: ``==`` 等于 & ``===`` 绝对等于

    - ``==`` 等于 只管 **值**
    - ``===`` 绝对等于 不仅管 **值** ， 还管 **类型**

    .. code-block:: jscon

        >>> let num = 2;
        >>> let str = '2';

        >>> num == str
        true 
        >>> num === str
        false

### if - for

.. code-block:: js

    if(condition){
        // true
    }else{
        // false
    }


    for(let i=0; i<3; i++){
        // for-loop
    }



## Array

``.filter(func)``: 创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。

遍历删除指定元素