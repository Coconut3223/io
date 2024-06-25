
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


.. _深入浅出package.json: https://juejin.cn/post/7099041402771734559
