
# node

.. danger:: node 安装

    | 接从官网上下载 installer，会直接在全局安装，需要 root 去调用，容易 ``raise PermissionError`` 
    | `解决-安装node.js后，使用npm命令时报没有权限的错误Error: EACCES: permission denied <https://blog.csdn.net/HuangLin_Developer/article/details/80050981>`_.
    | mac 使用 `nvm <https://github.com/nvm-sh/nvm>`_ 工具

    .. code-block:: bash

        $ nvm install node  # 下载最新的
        $ nvm install 12  # 下载 node==12

        $ nvm ls  # 查看下载了哪些
        ->      v22.3.0
                system
        
        % nvm use system
        Now using system version of node: v20.14.0 (npm v10.7.0)
        % nvm use 22  # 切换到 node==22
        Now using node v22.3.0 (npm v10.8.1)

## ?

`Windows系统配置NodeJS环境之fnm（小白向） <https://juejin.cn/post/7338645701658296357#heading-0>`_