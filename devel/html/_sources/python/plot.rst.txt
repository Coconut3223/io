Plot
##########

.. code-block:: py

    import matplotlib.pyplot as plt

    plt.margins(x=0, y=0)  # 去除白邊


条形图
********************

.. code-block:: py
    :caption: bar plot
    


散点图 scatter
********************

.. danger:: 如果两点有可能有相同的坐标，但有不同的标签，显示的颜色将是后绘制点的颜色，可以使用透明颜色，用来显示重叠点。

.. grid:: 2

    .. grid-item::
        :columns: 7
        
        .. code-block:: py
            :caption: scatter plot

            import matplotlib.pyplot as plt
            def plot_with_labels(x, y, classes, filename):
                """
                :x: 坐标
                :y: 数字类别, 按1/2/3 
                :classes: 对应的类别标签  
                    len(classes) = len_of_class
                """

                fig, ax = plt.subplots(figsize=(15, 12))

                # 隐藏右&上面的坐标轴
                ax.spines['right'].set_visible(False)  
                ax.spines['top'].set_visible(False)

                fig.set_tight_layout(True)  # 紧密的排布
                plt.margins(x=0, y=0)  # 消除周围空白区域

                scatter = ax.scatter(
                    x[:,0], x[:, 1],  # xy轴
                    c=y,  # 指定对应的label
                    cmap="Spectral"
                )

                # 添加图例 
                """
                这个操作应该就是把图例的 y & 真实的含义对应起来 
                """       
                legend1 = ax.legend(
                    scatter.legend_elements()[0],
                    classes,
                    loc="upper right", 
                    title=target_name, title_fontsize=20,
                    fontsize=18, )
                ax.add_artist(legend1)
                
                # plt.show()
                plt.savefig(filename)

    .. grid-item::
        :columns: 5

        .. figure:: ./pics/plot_1.png
            :scale: 10%

            画的图

        .. note:: 关于散点图的 legend

            | 因为是使用类别的数值代码来给点上色，所以需要传给它数值代码所对应的类别列表。
            | We colored the scatterplot using numerical code for the species variable.
            | We can maually specify labels for legend. **We define labels using a list of species names first.**
            
            .. code-block:: py
                :caption: scatter.legend

                legend_ = ax.legend(
                    scatter.legend_elements()[0],
                    classes)

            - `Data Viz with Python and R <https://datavizpyr.com/add-legend-to-scatterplot-colored-by-a-variable-with-matplotlib-in-python/>`_
            - `Scatter plots with a legend <https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html>`_
            

                

configs
**********


尺寸
==============================

.. code-block:: py

    plt.rcParams['figure.figsize'] = (W, H)  # 单位是inches

配色方案 ``cmap``
==============================

``rainbow`` & ``blues`` 好像用得比较多

``Spectral``

- `Choosing Colormaps in Matplotlib <https://matplotlib.org/stable/users/explain/colors/colormaps.html>`_
- `【Matplotlib】plt.imshow() cmap色彩表 <https://blog.csdn.net/qq_43426078/article/details/123635851>`_
- `Python-matplotlib绘制散点图-plt.scatter-颜色设置（c, cmap） <https://blog.csdn.net/qq_37851620/article/details/100642566>`_



图例 legend
====================

.. code-block:: py

    .legend(
        ..., 
        loc="upper right",  # 位置
        title=target_name, title_fontsize=20,  # legend 的 title
        fontsize=18,  # legend 的内容
    )

坐标轴
====================

隐藏坐标轴
--------------------

.. code-block:: py

    ax.spines['right'].set_visible(False)  # 右面的边隐藏
    ax.spines['top'].set_visible(False)  # 上面的边隐藏


坐标轴刻度间隔以及刻度范围
----------------------------------------

.. note:: 设置刻度范围的时候，多设置半个刻度间隔。
    
    因为不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白。显得不会太挤。

.. code-block:: py

    import matplotlib.pyplot as plt
    from matplotlib.pyplot import MultipleLocator
    # 用于设置刻度间隔
    
    plt.tick_params(
        axis='both',  # 'x'、'y'、'both'
        width=2, length=20,  # 长宽
        color='red'  # 颜色
        which='major',
        labelsize=14
    )

    ax=plt.gca() # ax为两条坐标轴的实例

    # 刻度间隔
    x_major_locator = MultipleLocator(1)  # 刻度间隔=1
    y_major_locator=MultipleLocator(10)  # 刻度间隔=10
    ax.xaxis.set_major_locator(x_major_locator)  # x主刻度=1的倍数
    ax.yaxis.set_major_locator(y_major_locator)  # y主刻度=10的倍数

    # 刻度范围
    plt.xlim(-0.5,11)  # -0.5到11
    plt.ylim(-5,110)  # -5到110

.. grid:: 2

    .. grid-item::
        .. figure:: https://img-blog.csdnimg.cn/20190507110725787.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDUyMDI1OQ==,size_16,color_FFFFFF,t_70

            before

    .. grid-item::
        .. figure:: https://img-blog.csdnimg.cn/20190507112143613.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDUyMDI1OQ==,size_16,color_FFFFFF,t_70

            after

- `matplotlib命令与格式：tick_params参数刻度线样式设置 <https://blog.csdn.net/helunqu2017/article/details/78736554>`_
- `Python设置matplotlib.plot的坐标轴刻度间隔以及刻度范围 <https://blog.csdn.net/weixin_44520259/article/details/89917026>`_


一些杂的
====================

.. grid:: 2

    .. grid-item:: 
        .. code-block:: py

            plt.margins(x=0, y=0)  # 消除周围空白区域

    .. grid-item:: 
        .. image:: ./pics/plot_2.png
            :scale: 30%

中文乱码
--------------------

