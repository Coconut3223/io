Enhanced Python
##############################

Script & Module & Package
****************************************

==script 脚本== 。是一个包含可执行代码的文件，一个 py 文件，更多时候是指可以直接运行的 py 文件。为一个特定任务写成。
==顶层代码== 。由用户指定的最先开始运行的那一个 py 文件，是应用程序的入口点。 它的 ``__name__``  被设为  ``__main__``
==module 模块== 。主要是被引用，包含了 **相关性较高** 的程式码。
==package 包== 。包含了一个或多个的 Module ，并且拥有  ``__init__.py`` 
==library 库== 。

顶层代码
==========

==顶层代码== 。由用户指定的最先开始运行的那一个 py 文件，是应用程序的入口点。

.. note:: 顶层代码的 ``__name__``  被设为  ``__main__`` 。"
    module 如果是 被 import，它的  ``__name__``  就会是它自己名字；如果是以 **脚本方式执行**，会把  ``__name__ = "__main__"`` 

    .. grid:: 2

        .. grid-item::

            .. code-block:: none
                :caption: dir

                + A
                    A1.py
                    A2.py
                    + subA
                        a1.py

        .. grid-item::

            .. code-block:: py
                :caption: dirA1.py

                print(f'in A1: {__name__}')

        .. grid-item::      
            .. code-block:: py
                :caption: A2.py

                from A1 import *
                from subA.a1 import *
                print(f'in A2: {__name__}')

        .. grid-item::    
            .. code-block:: py
                :caption: a1.py

                print(f'in a1: {__name__}')

    运行  ``python A2.py`` ， A2 是被运行的顶层代码， A1 & a1 时被 import 的module

    .. code-block:: pycon

        in A1: A1
        in a2: subA.a2  # 如果有上层，就会把上层文件也展示
        in A2: __main__  # A2 是被运行的顶层代码，被改为  ``__main__`` 

    .. note:: ""
        可以利用 ``if __name__ == '__main__':`` 来控制 **执行** 和 **被引用时** 的运行的代码内容。
        最好用  ``main``  进行封装，再调用。如果直接放在  ``if __name__ == '__main__':``  下的变量会成为 **全局变量**。

.. note::  ``__main__.py``  in package 参见 package section

Module
==========

==module 模块== 。主要是被引用，包含了 **相关性较高** 的程式码。

- 在 **模块内部** ，模块名 通过全局变量  ``__name__``  获取.
- 每个模块都有自己的 **私有命名空间** ，它会被用作模块中定义的所有函数的全局命名空间。

Package
==========

==package 包== 。包含了一个或多个的 Module ，并且拥有  ``__init__.py`` 。

但是一个比较齐全的包是：

.. code-block:: none

    + package
        __init__.py
        __main__.py
        module1.py

``__init__.py``
------------------------------

.. danger:: 需要有  ``__init__.py``  文件才能让 Python 将包含该文件的目录当作包来处理

| 从一个 package 里面调用东西的时候， ``__init__.py``  的代码会 **被首先执行**.
| 能帮助 package 完成 **批量导入和规范化导入**

.. warning:: 其可见性的维护是靠一套需要大家自觉遵守的"约定"
    
    | [Python中的__all__]: 使用  ``from xxx import *``  导入该文件时，只会导入  ``__all__``  列出的成员，可以其他成员都被排除在外。
    | 但是直接定位到精确调用是可以的

    .. note:: ""
        修改一个暴露的接口只修改一行，方便版本控制的时候看 diff

        .. grid:: 2

            .. grid-item:: 
                .. code-block:: none
                    :caption: dir

                    + A
                        __init__.py
                        A1.py
                        A2.py
                        + subA
                            a1.py
                            __init___.py

            .. grid-item:: 
                .. code-block:: py
                    :caption: subA.a1.py

                    def f1():
                        print("F1")
                    def f2():
                        print("F2")

                .. code-block:: py
                    :caption: subA.__init__.py

                    # 在 package 级别暴露接口
                    from sub.a1 import *
                    __all__ = [
                        "f1"
                    ]

    在 package 级别暴露接口，module level 也类似。
    
    
    .. grid:: 2

        .. grid-item::
            如果采用 ``from package import *`` 

            .. code-block:: pycon
                :caption: A1.py

                >>> from subA import *
                >>> f1()
                F1  # 成功了 
                >>> f2()
                NameError: name 'f2' is not defined. 
                Did you mean: 'f1'?

        .. grid-item::
            如果采用  ``from package.module import func``  精确调用

            .. code-block:: pycon
                :caption: A2.py

                >>> from subA.a1 import f1, f2
                >>> f1()
                F1
                >>> f2()
                F2

``__main__.py`` 
------------------------------

``python -m package`` 。 使用  ``-m``  从命令行直接调用软件包本身时，将执行  ``__main__.py`` 。

``__main__.py``  的内容通常不会用  ``if __name__＝＝'__main__'``  块围起来。相反，这些文件会保持简短 **并从其他模块导入函数来执行。 这样其他模块就可以很容易地进行单元测试并可以适当地重用。**

.. note:: package 里的 module 的单元测试是在  ``__main__.py``  进行.

import
==========

为了 **快速加载模块（不是加速执行）** ，Python 把 **模块的编译版本** 缓存在  ``__pycache__ dir``  中，文件名为  ``module.version.pyc，version``  对编译文件格式进行编码

.. hint:: ""
    CPython 的 3.3 发行版中，spam.py 的编译版本 ==  ``__pycache__/spam.cpython-33.pyc`` 

.. note:: 为什么没有 运行脚本的已编译档案？
    运行脚本 当作程式的进入点，所以每一次执行  ``python xxx.py``  指令时，Python编译器都要进行编译，所以没有将  ``xxx.py``  进行快取的动作。

从内容区分
--------------------

-  ``import module``  = 调用 》  ``module.specific_func()`` 
-  ``from module import specific_func``  = 调用 》  ``specific_func()`` 
-  ``from module import *``  = 调用 》  ``specific_func()`` 

.. warning:: 尽量不要用  ``from module import *`` ，这种方式向解释器导入了一批未知的名称，可能会覆盖已经定义的名称。

.. note:: ``from module import *``  会导入 **所有不以下划线（_）开头** 的名称。

.. danger:: ""
    -  ``from package import item``  时，item 可以是包的子模块（或子包），也可以是包中定义的函数、类或变量等其他名称。
    -  ``import item.subitem.subsubitem``  时，除最后一项外， **每个 item 都必须是包；最后一项可以是模块或包** ，但不能是上一项中定义的类、函数或变量。

从方式区分
------------------------------

See 路径相关的 section

- 绝对导入
- 相对导入

路径相关
**********

.. danger:: 如果不是从脚本所在路径  ``python ./xxx.py``  运行脚本，就会有 working directory & script path 区别
    
    | 用户在磁盘上寻找文件或子目录时，所历经的线路叫路径。
    | 目录和文件夹是一个意思

==工作目录 working directory cwd== 。用户当前目录。 ``os.getcwd()`` 
==脚本路径 script path== 。脚本文件所在的路径。  ``__file__`` 
==系统路径 system path sys== 。操作系统用来查找 **可执行文件和库文件** 的一组目录路径。 ``sys.path:List`` 

- 加入sys  ``sys.path.append(new_path)`` 
- 查看  ``sys.path`` 

【process】

- 程序将<u>脚本所在的目录</u>加入到 <u>sys</u> 中，用来查找 **可执行文件和库文件**
    ``os.path.dirname(__file__) == sys.path[0]`` 
- 程序会实行<u>脚本里的代码</u>，在<u>cwd</u> 进行查找创造文件。

.. grid:: 2

    .. grid-item::
        .. code-block:: none
            :caption: dir

            + A
                A1.py
                + subA
                    a1.py

    .. grid-item::
        .. code-block:: py
            :caption: A1.py

            import os, sys

            if __name__=="__main__":
                print(f'working_directory = {os.getcwd()}')
                print(f'script_path = {__file__}' )
                print(f'system_path[0] = {sys.path[0]}')
                with open('1.txt', 'w'):
                    ...

在 subA 底下运行  ``A1.py``   ``.../python.exe .../A/A1.py`` 

.. code-block:: sh

    working_directory = ...\A\subA
    script_path = ...\A\A1.py
    system_path[0] = ...\A
    1.txt 在 subA 底下， # 在工作目录对应进行创建

import - module 搜索路径
==============================

当  ``import spam`` ，解释器：

1. 搜索  ``spam``  的内置模块。这些模块的名称在  ``sys.builtin_module_names``  中列出。
2. 如果未找到，它将在变量  ``sys.path``  所给出的目录列表中搜索

**sys.path的初始化：**

- 被 **命令行直接运行的脚本所在的目录**。
- PYTHONPATH （目录列表，与 shell 变量 PATH 的语法一样）。
- 依赖于安装的默认值（按照惯例包括一个 site-packages 目录，由 site 模块处理）。

.. note::  ""
    程序将<u> ``run.py``  脚本所在的目录</u>加入到 <u>sys</u> 中，用来查找 **可执行文件和库文件**

自己写的包注意 import 路径，从系统路径中能不能找到，能不能形成可到达的路径

1. 通过  ``sys``  添加搜索路径  ``sys.path.append('package path')`` 
2. 绝对引用。当包由多个子包构成时，可以使用绝对导入来引用 **同级包的子模块**。
3. 相对引用。

.. danger:: 主模块始终使用 <u>绝对导入</u>

    相对导入基于当前模块名 ``module.__name__`` 。

    - 模块作为 **顶层文件被执行** 时， ``__name__="__main__"`` ，不包含任何包的名字
    - 但作为 **普通模块被 import**， 就会被包含包。

.. note:: 绝对引用 & 相对引用
    .. grid:: 2

        .. grid-item::

            .. code-block:: none
                :caption: dir

                + A
                    A1.py
                    A2.py

        .. grid-item::

            .. code-block:: py
                :caption: A1.py

                import A2  # 绝对引用
                import .A2  # 相对引用

[import 问题浅谈]

Others
**********

- Magic Number 魔数（中性词）
    | [编程中的「魔数」（magic number）是什么意思？平时我们能接触到哪些魔数？]
    | 一般是指 **硬写到代码里的整数常量**，数值是编程者自己指定的，其他人不知道数值有什么具体意义，表示不明觉厉，就称作magic number。编程教材书用magic number指代 **初学者不定义常量直接写数的不良习惯。**
    
    - **贬义词**: 指的是代码中出现的没有说明的数字。代码中突然出现一个没说明用途的数字会让其它阅读代码、维护代码的的人非常难受。
        .. hint:: ""
            例如写3.1416这种数字，也应该改为数学库中的π常数，例如Unity中的Mathf.PI。

    - **褒义词**: 通过一些底层原理实现骚操作
    - **中性词**：
        .. hint:: Example
            | ELF文件头会写入一个magic number，检查这个数和自己预想的是否一致可以判断文件是否损坏。
            | 如果你用16进制编辑器打开一个文件，它的开头不是FFD8FF，那就不是jpg文件。这个魔数一般会在相关文件标准中进行规定，所有人都要遵守

ipynb
**********

`jupyter notebook中找不到anaconda中的python环境解决方法  <https://blog.csdn.net/sean2100/article/details/83744679>`_

.. code-block:: bash

    conda install nb_conda_kernels


.. warning:: 但是最近好像有点问题 对于高版本会显示 ``3.1x``


常用的别的
********************


os
==========

.. danger:: ``os.listdir()`` 返回的只是一个某个路径下的文件和列表的名称, 甚至不是相对路径，只是文件名字

    需要 ``os.path.join()`` 来拼接


进度条
====================

``tqdm``

.. code-block:: py

    from tqdm import tqdm

    for i in tqdm(range(10)):
        ...

    for x in tqdm(lst):
        ...

    for idx, x in enumerate(tqdm(lst)):
        ...


logging
====================

.. code-block:: py

    import logging
    logging.basicConfig(filename='log_name.log', 
                        # filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG  # the minimum message level it will accept
                        )

    logging.info("Running Urban Planning")  # 写入log

    logger = logging.getLogger('urbanGUI')  # ?

`message level <https://docs.python.org/3/library/logging.html#logging-levels>`_

.. table::

    +-------------+--------------+-------------+------------+---------------+-------------+----------------+
    |Level        |logging.NOTSET|logging.DEBUG|logging.INFO|logging.WARNING|logging.ERROR|logging.CRITICAL|
    +=============+==============+=============+============+===============+=============+================+
    |Numeric value|0             |10           |20          |30             |40           |50              |
    +-------------+--------------+-------------+------------+---------------+-------------+----------------+


.. danger:: 低于设定 level 的会被忽略。


脚本传参
====================

.. code-block:: bash
    :caption: 两种格式

    python script.py 0,1,2 10  # sys.argv
    python script.py --gpus=0,1,2 --batch_size=10  # argparse


.. grid:: 2

    .. grid-item::
        ``sys.argv``

        .. code-block:: py

            import sys
            gpus = sys.argv[1]
            gpus = [int(gpus.split(','))]
            batch_size = sys.argv[2]
            print(gpus)
            print(batch_size)
        
        .. code-block:: bash

            python script.py 0,1,2 10

    .. grid-item::
        ``argparse``

        .. code-block:: py

            import argparse
            parser = argparse.ArgumentParser(description='manual to this script')
            parser.add_argument('--gpus', type=str, default = None)
            parser.add_argument('--batch_size', type=int, default=32)

            args = parser.parse_args()
            print(args.gpus)
            print(args.batch_size)

        .. code-block:: bash

            python script.py --gpus=0,1,2 --batch_size=10



- `命令行运行Python脚本时传入参数--3种方法 <https://blog.csdn.net/helloasimo/article/details/124210144>`_
- `命令行运行Python脚本时传入参数的三种方式 <https://blog.csdn.net/weixin_35653315/article/details/72886718?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-3.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-3.pc_relevant_antiscanv2&utm_relevant_index=6>`_


shell 命令
====================

``shutil`` & ``os``

文件 & 文件夹
--------------------

- ``shutil.copy()`` 复制 & ``shutil.move()`` 移动
    操作都一样
- ``os.remove(file)``  & ``shutil.rmtree(folder)`` 删除


.. code-block:: py

    import shutil
    import Others

    shutil.copy('demo.txt','new_folder')  # 单纯复制过去
    shutil.move('demo.txt','new_folder/demo1.txt')  # 移动并改名

    os.remove(file)  # del 文件
    shutil.rmtree(folder)  # del folder

- `【Python】移动、复制文件到另一个文件夹、删除文件（夹） <https://blog.csdn.net/Asher117/article/details/109083247>`_

RE
==========


表达式
--------------------

.. code-block:: py

-  ``flags=0``  用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
    - re.I 忽略大小写
    - re.X 为了增加可读性，忽略规则表达式中的空白和注释，并允许使用 ’#’ 来引导一个注释。这样可以让你把规则写得更美观些。

    .. table::

        +-------------+------------------------------------+---------------------------------------------------------------+
        |symbol       |meaning                             |special usage                                                  |
        +=============+====================================+===============================================================+
        | ``\D``      |任何非十进制数字的字符              | ``re.sub(r'\D', '', string)``  只保留十进制数字               |
        +-------------+------------------------------------+---------------------------------------------------------------+
        | ``[0-9-]+`` |0-9 还有 ``-`` 号,  ``+`` ：不止一个| ``re.match('[0-9-]+', string)``  提取的仅包含数字和-的电话号码|
        +-------------+------------------------------------+---------------------------------------------------------------+

-  ``re.match(pattern, string, flags=0)`` 
    - 从字符串的 **起始位置** 匹配一个模式
    - 成功  ``return <re.Match object; span=(0, end_idx), match=pattern>`` 
        -  ``<re.Match object>.group()``  返回正则匹配的字符串
        -  ``<re.Match object>.start()`` ,  ``<re.Match object>.end()`` 
        -  ``<re.Match object>.span()`` : (start, end)
        - 不是起始位置匹配成功  ``return None`` 

-  ``re.sub(pattern, repl, string, count=0, flags=0)`` 
    -  ``count=0`` : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。





Request
====================


测试
**********

时间
==========

简单感觉时间可用time，但是对优化来说，得看quota，看哪部分占比比较明显，如果是那些外调的函数比较明显的话，那也木有办法。

.. warning:: 加载模型尽量在外部一次加载，load是比较慢的，不要每次调每次都加载。

time
--------------------

.. code-block:: py

    import time

    start = time.time()
    main()
    print(time.time()-start)  # 秒

``cProfile``  +  ``pstats`` 
----------------------------------------
.. table::

    +---------------------+-------------------------------------------------------------+
    | ``cProfile``  结果列|意思                                                         |
    +=====================+=============================================================+
    |ncalls               |调用次数                                                     |
    +---------------------+-------------------------------------------------------------+
    |tottime              |在指定函数中消耗的总时间<u>（不包括调用子函数的时间）</u>    |
    +---------------------+-------------------------------------------------------------+
    |percall              | = tottime / ncalls                                          |
    +---------------------+-------------------------------------------------------------+
    |cumtime              |指定的函数<u>及其所有子函数</u>（从调用到退出）消耗的总时间。|
    +---------------------+-------------------------------------------------------------+
    |percall              | = cumtime / ncalls, 函数运行一次的平均时间                  |
    +---------------------+-------------------------------------------------------------+
    |filename             |函数名                                                       |
    +---------------------+-------------------------------------------------------------+

.. table::

    +-----------------+--------------------------------------------------+
    | ``pstats``  函数|意思                                              |
    +=================+==================================================+
    |strip_dirs()     |移除了所有模块名称中的多余路径                    |
    +-----------------+--------------------------------------------------+
    |sort_stats(key)  |对key列 ==降序== 排序                         |
    +-----------------+--------------------------------------------------+
    |print_stats(n)   | 打印统计数据 , default n = all                   |
    +-----------------+--------------------------------------------------+
    |print_callers(n) |每个被列出的函数的调用方列表 , default n = all    |
    +-----------------+--------------------------------------------------+


.. code-block:: py
    :caption: main.py

    def run():
        pass
    
    if __name__ == '__main__':
        for i in rang(10):
            run()

.. code-block:: bash

    python -m cProfile -o output_file main.py
    # 将结果写入文件

.. code-block:: py
    :caption: analysis.py

    import pstats
    from pstats import SortKey
    p = pstats.Stats('./output_file')

    # 按一个函数中的累计时间对性能分析数据进行排序,打印多的30行
    p.sort_stats(SortKey.CUMULATIVE).print_stats(30)
    # 每个函数耗费的时间进行排序，然后打印前十个函数的统计数据 
    p.sort_stats(SortKey.TIME).print_stats(10)
    # 以时间为主键，并以累计时间为次键进行排序，然后打印10条
    p.sort_stats(SortKey.TIME, SortKey.CUMULATIVE).print_stats(.5)

time
==========

.. code-block:: py
    :caption: 秒的换算关系

    def second_2_standard(total_second):
        hours, reminder = divmod(total_second, 3600) 
        minutes, reminder = divmod(reminder, 60)
        seconds, reminder = divmod(reminder, 1)
        centiseconds = reminder * 100
        milliseconds = centiseconds * 10
        print(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(milliseconds):03}")


        second_2_standard(11111.33)
        # 03:05:11,329


json
==========


.. grid:: 2

    .. grid-item::
        
        .. code-block:: py
            :caption: dict -- Str

            dict = json.loads(str)
            str = json.dumps(str)


    .. grid-item::

        .. code-block:: py
            :caption: dict -- json 文件

            dict = json.load(json_file)
            with open(json_file, 'w') as fp:
                json.dump(dict, fp)




.. note:: 写中文

    - ``encoding='utf-8'``
    - ``ensure_ascii=False``

.. code-block:: py

    import json
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
    except FileNotFoundError:
        print(f'{json_path} doesnt exist.')
        return ''

    with open('./built-in.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=4, ensure_ascii=False)

pip 环境
******************************

``requirements.txt``, ``environment.yml`` 是同一类的东西，它们提供的是当前软件包安装运行所需要的环境或者依赖信息，即这些东西的安装是当前软件包安装和运行的前提条件。这些信息相当于是开发者给使用者提供的用于恢复自己开发时的环境的信息。

.. danger:: ``environment.yml`` !!

    1. ``environment.yml`` 已指定 虚拟环境的名字，要check 当前虚拟环境列表里没有重名的
    2. check yml文件最后一行是 ``prefix: E:\anacodna3\envs\pytorch`` 这是个虚拟环境路径

.. grid:: 2

    .. grid-item::

        **requirements.txt** --- ``pip``
        .. code-block:: bash
            :caption: 只想生成当前项目依赖的

            cd project/root
            pip install pipreqs
            pipreqs . --encoding=utf8 --force  
            # 当前目录生成

            # 安装
            pip install -r requirements.txt

    .. grid-item::

        **environment.yml**  --- ``conda env create``

        .. code-block:: bash
            :caption: 只想生成当前项目依赖的

            cd project/root
            conda env export > environment.yml
            # 当前目录生成

            # 创建
            conda env create -f environment.yml

`Python库安装之requirements.txt, environment.yml <https://blog.csdn.net/chenxy_bwave/article/details/121187923>`_

Type & Typing 类型声明
******************************


判断 变量是哪种类型
==============================

- ``isinstance()``：认为子类是一种父类类型，考虑继承关系
- ``type()``：不会认为子类是一种父类类型，不考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。


.. danger:: Type 变量是哪种类型

    .. grid:: 2

        .. grid-item::
            .. code-block:: pycon 
                :caption: Wrong

                >>> from typing import List
                >>> a = [1,2,3]
                >>> type(a)==List
                False
        
        .. grid-item::
            .. code-block:: pycon 
                :caption: True
                
                >>> type(a)==list
                True

.. note:: 中英文 & 数字

    利用 **Unicode**

    - 中文（基本汉字）在Unicode编码中的范围：\u4e00-\u9fa5
    - 英文单词在Unicode中的范围就是acsii码中的前英文字母，即在unicode的前128种

    .. grid:: 2

        .. grid-item:: 

            .. code-block:: py
                :caption: 是否是纯中文

                def isChinese(ch):
                    return '\u4e00' <= ch <= '\u9fff'

                all(map(isChinese, s))


        .. grid-item:: 

            .. code-block:: py
                :caption: 是否是纯英文

                def isEnglish(ch):
                    return 5 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122

                all(map(isEnglish, s))

            
    `中文字符和英文字符判断 <https://blog.csdn.net/u014147522/article/details/126308776>`_


`python 判断变量类型 是否为list(列表) 以及dict(字典) 类型 —— isinstance() type() <https://blog.csdn.net/weixin_42649856/article/details/103578109>`_

.. note:: 只是一种类型提示，对运行实际上是没有影响的，就算不对，不会报错，也不会对参数进行类型转换

.. code-block:: py

    from typing import List, Tuple, 

    names: List[str] = ['Germey', 'Guido']
    person: Tuple[str, int, float] = ('Mike', 22, 1.75)
    operations: Dict[str, bool] = {'show': False, 'sort': True}

    from typing import Sequence  # 序列类型 无畏 list or tuple

    from typing import NoReturn
    def hello() -> NoReturn:
        print('hello')

    from typing import Union  # 并集
    def func(a:Union[int, str]):
        ...

    from typing import Optional  # = Union[type, None]
    # 这个参数可以传为 None
    def func(a:Optional[str]):
        ...


.. table::

    +----+---------------+--------+
    |注解|参数           |返回类型|
    +====+===============+========+
    |字典|``Mapping``    |``Dict``|
    +----+---------------+--------+
    |集合|``AbstractSet``|``Set`` |
    +----+---------------+--------+

.. note:: 关于 字典 ``Dict`` & ``Mapping``

    .. grid:: 2

        .. grid-item::

            - ==Dict== 、字典, 是 dict 的泛型； **注解返回类型**
            - ==Mapping== , 映射, 是 collections.abc.Mapping 的泛型 **注解参数**
            - ==MutableMapping== 则是 Mapping 对象的子类，在很多库中也经常用 MutableMapping 来代替 Mapping。

            ``Dict|Mapping[type_of_key, type_of_value]``

        .. grid-item::

            .. code-block:: py

                from typing import Dict, Mapping

                def size(rect: Mapping[str, int]) -> Dict[str, int]:
                    return {'width': rect['width'], 'height': rect['width']}


.. note:: 关于 集合 ``set`` & ``AbstractSet``

    .. grid:: 2

        .. grid-item::

            - ``Set`` 集合，是 set 的泛型； **注解返回类型**
            - ``AbstractSet`` 是 collections.abc.Set 的泛型。 **注解参数**

        .. grid-item::

            .. code-block:: py

                from typing import Set, AbstractSet
                def describe(s: AbstractSet[int]) -> Set[int]:
                    return set(s)

`Python 中 typing 模块和类型注解的使用 <https://cuiqingcai.com/7071.html>`_


Todo
********************

[import雜談之三———sys.path的洪荒之時]

[import雜談之三———sys.path的洪荒之時]: https://ithelp.ithome.com.tw/articles/10196901
[Python中的__all__]:https://zhuanlan.zhihu.com/p/54274339
[import 问题浅谈]:https://zhuanlan.zhihu.com/p/69099185
[编程中的「魔数」（magic number）是什么意思？平时我们能接触到哪些魔数？]:https://www.zhihu.com/question/22018894
