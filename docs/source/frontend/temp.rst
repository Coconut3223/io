
# Temporal


## operations

1. ``npm init`` 生成 package.json

## utils


### package management ``package.json``

==npm== 是前端开发人员广泛使用的包管理工具，项目中通过 ==package.json== 来管理项目中所依赖的 npm 包的配置。

.. code:: json
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

- `深入浅出package.json`_


## theroy

### Modules & Packages

一个 Node.js 文件就是一个模块，这个文件可能是 Javascript 代码、JSON 或者编译过的 C/C++ 扩展。

Node.js 有三大類的模組

    - Core Modules (原生模組)
    - Local Modules (自建模組)
    - Third Party Modules (第三方模組)

.. hint:: example

    ``var http = require('http')``. 其中，http 是 Node.js 的一个核心模块，其内部是用 C++ 实现的，外部用 Javascript 封装。我们通过 require 函数获取了这个模块，然后才能使用其中的对象。


Node.js 提供了两个 ``exports`` 和 ``require`` 两个对象

    - ``exports`` 是模块公开的接口
    - ``var module = require('module_name');`` 用于从外部获取一个模块的接口，即获取模块的 exports 对象。

        根據不同的module，它回傳的將會是一個物件，函式，屬性，或是其他的javascript 型別。



.. danger:: ``require`` 不会重复加载模块
    
    实际上和对象又有本质的区别: **无论调用多少次 require，获得的模块都是同一个。**

.. grid:: 2

    
    .. grid-item::

        .. code-block:: none
            :caption: directory

            - moduleA.js
            - code.js


    .. grid-item::

        .. code-block:: js
            :caption: moduleA.js (自定义)

            var name;

            export.simplehello = 'Hello World.'   // 使用屬性
            exports.setName =  function(uname){  // 使用函式, 名字=setName
                name = uname;
            };
            exports.sayhello =  function(){
                console.log('Hello' + name);
            };

    
    .. grid-item::

        .. code-block:: js
            :caption: code.js

            var http = require('http');  // 引用公开的

            var module_a = require('./moduleA'); // 引用自定义
            
            console.log(module_a.simplehello);  // 使用屬性
            module_a.setName('Lily');  // 使用函式
            module_a.sayhello();
        
        .. code-block:: bash    
            :caption: terminal

            Hello World.
            Hello Lily

#### Core Modules

- http：它包含可以用來建立http server 的一些類別, 方法, 及事件。
- url：它包含可以解析url的一些方法。
- querystring：它包含可以處理由client端傳來querystring的一些方法。
- path：它包含可以處理一些檔案或資料夾路徑的方法。
- fs：它包含檔案的存取／操作的一些類別，方法及事件。
- util：它包含一些可供程序者使用的效能函式。


**Ref**

- `Node.js 模块和包（Modules）`_
- `Day3 - Node.js Modules 介紹及載入`_
- `Day5 - 關於 module.exports 的兩三事`_





### 路由 rounter

.. note:: 認識網址規則

    - ``https`` ：有分為 http 與 https 協定，而 https 有加密功能
    
        .. danger:: 簡單說就是如果有需要填寫表單，請務必檢查是否是 https 開頭的喔！

    - ``www.google.com``：這個為網址，或稱為 domain。
    - ``/search``：這是路徑，這邊代表搜尋（名稱可以自訂）。
    - ``?q=xxxx``：此為參數，會用 ?q 代表，q 代表 query。
    - ``&``：多個參數會用 & 做串聯。


    .. hint:: example

        透過 express 建立一個 Web 伺服器，如果沒有特別給路徑，預設為根目錄，而這次給予兩個路徑。

        .. code-block:: js
            :caption: app.js

            const express = require('express');
            const app = express();

            app.get("./page/index", (req, res) => {
                res.send(`<h1>Hello, Node</h1>`);
            });

            app.get("./page/about", (req, res) =>{
                res.send(`<h1>About Node</h1>`);
            });

            const port = process.env. port || 3000;
            app.listen(port);

        .. code-block:: none
            :caption: localhost:3000/page/index

            Hello, Node

            // 當網址輸入為 /page/index，則會出現 Hello,Node!


### 网络方法

#### ``get`` & ``post``


- GET方法请求一个指定资源的表示形式，使用GET的请求应该只被用于获取数据
- POST方法用于将实体提交到指定的资源，通常导致在服务器上的状态变化或副作用

| 本质上都是TCP链接，并无差别
| 但是由于HTTP的规定和浏览器/服务器的限制，导致他们在应用过程中会体现出一些区别

**Ref**

- `Node.js - 路由設計`_






.. _深入浅出package.json: https://juejin.cn/post/7099041402771734559
.. _Node.js 模块和包（Modules）: https://developer.aliyun.com/article/553861
.. _Day3 - Node.js Modules 介紹及載入: https://ithelp.ithome.com.tw/m/articles/10184564
.. _Day5 - 關於 module.exports 的兩三事: https://ithelp.ithome.com.tw/m/articles/10185083
.. _Node.js - 路由設計: https://hsuchihting.github.io/node/20221023/885469299/