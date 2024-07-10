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
        
        .. code-block:: py
            :caption: scatter plot

            import matplotlib.pyplot as plt
            def plot_with_labels(x, y, classes, filename='tsne.png'):
                """
                :x: 坐标
                :y: 数字类别, 按1/2/3 
                :classes: 对应的类别标签  len(classes) = len_of_class
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

        .. figure:: ./pics/plot_1.png
            :scale: 20%

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

            `Data Viz with Python and R <https://datavizpyr.com/add-legend-to-scatterplot-colored-by-a-variable-with-matplotlib-in-python/>`_

                

configs
**********

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

.. code-block:: py

    ax.spines['right'].set_visible(False)  # 右面的边隐藏
    ax.spines['top'].set_visible(False)  # 上面的边隐藏

一些杂的
====================

.. grid:: 2

    .. grid-item:: 
        .. code-block:: py

            plt.margins(x=0, y=0)  # 消除周围空白区域

    .. grid-item:: 
        .. image:: ./pics/plot_2.png
            :scale: 30%



