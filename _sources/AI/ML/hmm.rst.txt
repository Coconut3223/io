HMM 隐马尔可夫 Hidden Markov Model
########################################


理论
**********

Markov
==========

==Markov property 马尔可夫性质== := 当一个随机过程在给定现在状态及所有过去状态情况下，其未来状态的条件概率分布 **仅依赖于当前状态**; 换句话说, 在给定现在状态时, 它与过去状态 (即该过程的历史路径) 是条件独立的, 那么此随机过程即具有马尔可夫性质。

.. math::
    P(X_t\vert X_1,X_2,\dots,X_{t-1}) = P(X_t\vert X_{t-1})

.. note:: 现在此刻决定未来。

==马尔可夫假设 Markov assumption== := 假设描述一个模型具有马尔可夫性质，比如隐马尔可夫模型。


HMM
**********

假设
==========

1. **观测独立假设**：观测只依赖于该马尔科夫链的状态，与其他观测及状态无关。
    .. math::
        P(o_n\vert s_1, o_1, s_2, o_2, ..., s_n) = P(o_n\vert s_n)

2. **马尔可夫性假设**：当前状态只与前一状态有关 
    .. math::
        P(s_n\vert s_1, s_2, ..., s_{n-1}) = P(s_n\vert s_{n-1})

基于 隐马尔可夫模型的结构， **所有变量的联合概率分布** 为

.. math::

    P(s_1, o_1, ..., s_n, o_n) = P(s_1)P(o_1\vert s_1)\prod_{i=2}^n\big(P(s_i\vert s_{i-1})P(o_i\vert s_i)\big)\\

    \begin{cases}
    S:= (s_1, s_2, ..., s_n) = \text{state variables}\\
    O:= (o_1, o_2, ..., o_n) = \text{observation variables}\\
    \pi:= P(s_1)\\
    A:= P(s_i\vert s_{i-1})\\
    B:= P(o_i\vert s_i)\\
    Q:= \text{状态集合}\\
    V:= \text{观察集合}\\
    \end{cases}\\
    \implies \lambda = (A, B, \pi)

    

.. figure:: ./pics/hmm_1.png
    :scale: 50%

    隐马尔可夫模型的图结构

    **识别问题**：

.. figure:: ./pics/hmm_5.png
    :scale: 70%

    




.. hint:: Example: 盒子抽颜色
    
    假设有3个盒子, 每个盒子都有 R, W 两种颜色的球。按照以下步骤抽球，产生球颜色的观测序列。

    1. 开始根据 :math:`\pi` , 从3个盒子随机抽取1个盒子。
    2. 根据 **观测概率矩阵** :math:`B` 从抽取的盒子里随机抽出一个球，记录其颜色 **放回**
    3. 根据 **状态转移概率矩阵** :math:`A`  从当前盒子转移到下一个盒子
    4. 重复23 3次，得到一个球的颜色观测序列 (R, W, R)

    .. grid:: 2
    
        .. grid-item::

            .. table:: 观测概率

                +-----+----+----+----+
                |balls|box1|box2|box3|
                +=====+====+====+====+
                |R    |5   |4   |7   |
                +-----+----+----+----+
                |W    |5   |6   |3   |
                +-----+----+----+----+

            .. table:: 初始选择概率 π

                +------------+----+----+----+
                |            |box1|box2|box3|
                +============+====+====+====+
                |初始选择概率|.2  |.4  |.4  |
                +------------+----+----+----+

            .. table:: 状态转移概率
                
                +----+----+----+----+
                |    |box1|box2|box3|
                +====+====+====+====+
                |box1|.5  |.2  |.3  |
                +----+----+----+----+
                |box2|.3  |.5  |.2  |
                +----+----+----+----+
                |box3|.2  |.3  |.5  |
                +----+----+----+----+
        .. grid-item::
            
            .. math::
                B = \begin{bmatrix}.5&.5\\.4&.6\\.7&.3\end{bmatrix}\\
                R = B[:, 0] = \begin{bmatrix}.5&.4&.7\end{bmatrix}^T\\
                W = B[:, 1] = \begin{bmatrix}.5&.6&.3\end{bmatrix}^T\\
            
            .. math::
                \pi = \begin{bmatrix}.2\\.4\\.4\end{bmatrix}

            .. math::
                A = \begin{bmatrix}.5&.2&.3\\.3&.5&.2\\.2&.3&.5\end{bmatrix}

            .. math::
                \begin{cases}
                O=\{R, W, R\}\\
                S=\{\text{box}?, \text{box}?, \text{box}?\}\\
                Q=\{1, 2, 3\}\\
                V=\{R, W\}\end{cases}

识别问题
====================

**概率计算算法** ： 给定 :math:`\lambda=(A, B, \pi)`, 计算其产生观测序列 :math:`O=\{o_1, o_2, ..., o_n\}` 的概率 :math:`P(O\vert \lambda)`

.. figure:: ./pics/hmm_2.png
    :scale: 50%
    
    应用

.. note:: 在给定参数下计算样本出现的概率， 根据概率的大小进行识别。
    
    **前向算法**


.. hint:: Example: 盒子抽颜色

    .. math::

        P(O\vert\lambda) = P(\text{R, W, R}\vert(A, B, \pi))

    
    .. grid:: 2
    
        .. grid-item::
            :columns: 7

            .. math::
                
                s_1 = \pi = \begin{bmatrix}.2\\.4\\.4\end{bmatrix} \\
                o_1(R) = s_1 \cdot R = \begin{bmatrix}.2\\.4\\.4\end{bmatrix} \cdot \begin{bmatrix}.5\\.4\\.7\end{bmatrix} = \begin{bmatrix}.1\\.16\\.28\end{bmatrix} \\
                \begin{align*}
                s_2 = A \times o_1 &=  \begin{bmatrix}.5&.2&.3\\.3&.5&.2\\.2&.3&.5\end{bmatrix}^T\times\begin{bmatrix}.1\\.16\\.28\end{bmatrix} \\
                &= \begin{bmatrix}.5&.3&.2\\.2&.5&.3\\.3&.2&.5\end{bmatrix}\times\begin{bmatrix}.1\\.16\\.28\end{bmatrix} \\
                &= \begin{bmatrix}.154\\.184\\.202\end{bmatrix}  \red{\sim\begin{bmatrix}\text{box1}\\ \text{box2}\\ \text{box3}\end{bmatrix}}
                \end{align*} \\
                o_2(W) =  s_2 \cdot W = \begin{bmatrix}.154\\.184\\.202\end{bmatrix} \cdot \begin{bmatrix}.5\\.6\\.3\end{bmatrix} =  \begin{bmatrix}.077\\.1104\\.0606\end{bmatrix} \\ 
                \begin{align*}
                s_3 = A \times o_2 &=  \begin{bmatrix}.5&.2&.3\\.3&.5&.2\\.2&.3&.5\end{bmatrix}^T\times\begin{bmatrix}.077\\.1104\\.0606\end{bmatrix} \\
                &= \begin{bmatrix}.5&.3&.2\\.2&.5&.3\\.3&.2&.5\end{bmatrix}\times\begin{bmatrix}.077\\.1104\\.0606\end{bmatrix} \\
                &= \begin{bmatrix}.08374\\.08878\\.07548\end{bmatrix} \red{\sim\begin{bmatrix}\text{box1}\\ \text{box2}\\ \text{box3}\end{bmatrix}}
                \end{align*} \\
                o_3(R) =  s_3 \cdot R = \begin{bmatrix}.08374\\.08878\\.07548\end{bmatrix} \cdot \begin{bmatrix}.5\\.4\\.7\end{bmatrix} = \begin{bmatrix}.04187\\.035512\\.052836\end{bmatrix} \\
                P(O\vert\lambda) = \sum(\begin{bmatrix}.04187\\.035512\\.052836\end{bmatrix}) = 0.130218

        .. grid-item::
            :columns: 5

            .. code-block:: pycon

                >>> import numpy as np
                >>> pi = np.array([.2, .4, .4])
                >>> B = np.array([[.5, .5],
                ...             [.4, .6],
                ...             [.7 , .3]
                ...             ])
                >>> A = np.array([[.5, .2, .3],
                ...             [.3, .5, .2],
                ...             [.2, .3, .5]])
                >>> R, W = B[:, 0], B[:, 1]
                >>> R, W
                (array([0.5, 0.4, 0.7]), 
                array([0.5, 0.6, 0.3]))
                >>> o1 = pi * R
                array([0.1 , 0.16, 0.28])
                >>> s2 = A.transpose().dot(o1)
                array([0.154, 0.184, 0.202])
                >>> o2 = s2 * W
                array([0.077 , 0.1104, 0.0606])
                >>> s3 = A.transpose().dot(o2)
                array([0.08374, 0.08878, 0.07548])
                >>> o3 = s3 * R
                array([0.04187 , 0.035512, 0.052836])
                >>> sum(o3)
                np.float64(0.130218)

            .. math::

                A_{ij} = P(s_t=j\vert s_{t-1}=i) = i\rightarrow j\\
                i,j = 1,\dots,N\\
                s_t = \begin{bmatrix}1\\2\\\vdots\\N\end{bmatrix} = \red{A^T} \times s_{t-1}\\
                \Leftrightarrow {s_t}_{i} = \sum_{j=1}^N\red{A_{ji}\times {s_{t-1}}_j}

            

                
            
预测问题
====================

**解码** ： 给定 :math:`\lambda=(A, B, \pi)` 观测序列 :math:`O=\{o_1, o_2, ..., o_n\}` ， 计算与观测序列最匹配的状态序列 :math:`S=\{s_1, s_2, ..., s_n\}`

.. note:: 由观测样本得到隐状态

    维特比算法

.. figure:: ./pics/hmm_4.png
    :scale: 70%

    



维特比算法
--------------------

数据量大时，维特比算法效果明显，可以降到线性计算量。

.. figure:: ./pics/hmm_6.png
    :scale: 70%


.. hint:: Example: 盒子抽颜色

    .. math::

        S = \max(P(O\vert S,\lambda))

    
    .. grid:: 2
    
        .. grid-item::
            :columns: 7

            .. math::
                s_1 = \pi = \begin{bmatrix}.2\\.4\\\red{.4}\end{bmatrix} \red{\rightarrow 3}\\
                o_1(R) = s_1 \cdot R = \begin{bmatrix}.2\\.4\\\red{.4}\end{bmatrix} \cdot \begin{bmatrix}.5\\.4\\.7\end{bmatrix} = \begin{bmatrix}.1\\.16\\\red{.28}\end{bmatrix} \\
                \begin{align*}
                s_2 = A \overline{\times} o_1 &=  \begin{bmatrix}.5&.2&.3\\.3&.5&.2\\.2&.3&.5\end{bmatrix}^T\overline{\times}\begin{bmatrix}.1\\.16\\\red{.28}\end{bmatrix} \\
                &= \begin{bmatrix}.5&.3&.2\\.2&.5&.3\\.3&.2&.5\end{bmatrix}\cdot\begin{bmatrix}.1&.16&.28\\.1&.16&.28\\.1&.16&\red{.28}\end{bmatrix} \\
                &=\begin{bmatrix}.05&.048&.056\\.02&.08&.084\\.03&.032&\red{.14}\end{bmatrix}\\
                &\xrightarrow{\text{max at axis=1}}\begin{bmatrix}.056\\.084\\\red{.14}\end{bmatrix} \red{\rightarrow 3}
                \end{align*}\\
                o_2(W) = s_2 \cdot W = \begin{bmatrix}.056\\.084\\\red{.14}\end{bmatrix} \cdot \begin{bmatrix}.5\\.6\\.3\end{bmatrix} =  \begin{bmatrix}.028\\.0504\\.042\end{bmatrix} \\ 
                \begin{align*}
                s_3 = A \overline{\times} o_2 &=  \begin{bmatrix}.5&.2&.3\\.3&.5&.2\\.2&.3&.5\end{bmatrix}^T\overline{\times}\begin{bmatrix}.028\\.0504\\\red{.042}\end{bmatrix} \\
                &= \begin{bmatrix}.5&.3&.2\\.2&.5&.3\\.3&.2&.5\end{bmatrix}\cdot\begin{bmatrix}.028&.0504&\red{.042}\\.028&.0504&.042\\.028&.0504&\red{.042}\end{bmatrix} \\
                &=\begin{bmatrix}.014&.01512&.0084\\.0056&.0252&.0126\\.0084&.01008&\red{.021}\end{bmatrix}\\
                &\xrightarrow{\text{max at axis=1}}\begin{bmatrix}.01512\\.0252\\\red{.021}\end{bmatrix} \red{\rightarrow 3}
                \end{align*}\\
                o_3(R) =  s_3 \cdot R = \begin{bmatrix}.01512\\.0252\\\red{.021}\end{bmatrix} \cdot \begin{bmatrix}.5\\.4\\.7\end{bmatrix} = \begin{bmatrix}00756\\.01008\\\red{.0147}\end{bmatrix} \\
                \red{.0147\rightarrow.021\rightarrow.042\rightarrow.14\rightarrow.28\rightarrow.4}\\
                \implies \bold{3\rightarrow3\rightarrow3}

            .. figure:: ./pics/hmm_3.png

        .. grid-item::
            :columns: 5

            .. code-block:: pycon

                >>> import numpy as np
                >>> pi = np.array([.2, .4, .4])
                >>> B = np.array([[.5, .5],
                ...             [.4, .6],
                ...             [.7 , .3]
                ...             ])
                >>> A = np.array([[.5, .2, .3],
                ...             [.3, .5, .2],
                ...             [.2, .3, .5]])
                >>> R, W = B[:, 0], B[:, 1]
                >>> R, W
                (array([0.5, 0.4, 0.7]), 
                array([0.5, 0.6, 0.3]))
                >>> o1 = pi * R
                array([0.1 , 0.16, 0.28])
                >>> o1_ = np.repeat(o1.reshape(1,3), 3, axis=0)
                array([[0.1 , 0.16, 0.28],
                [0.1 , 0.16, 0.28],
                [0.1 , 0.16, 0.28]])
                >>> s2 = np.max(o1_*A.transpose() , axis=1)
                array([0.056, 0.084, 0.14 ])
                >>> o2 = s2 * W
                array([0.028 , 0.0504, 0.042 ])
                >>> o2_ = np.repeat(so2.reshape(1,3), 3, axis=0)
                >>> s3 = np.max(o2_*A.transpose() , axis=1) 
                array([0.01512, 0.0252 , 0.021])
                >>> o3 = p2 * R
                array([0.00756, 0.01008, 0.0147 ])

            开始回溯

            .. math::

                \red{.0147-.021-.042-.14-.28-.4}\\
                \implies \bold{3\rightarrow3\rightarrow3}

            最佳隐状态是： box3 -》 box3 -》 box3


            
                
         
对比
********************

局限
====================


1. 状态值存在长距离的依赖，但是 HMM 要求离散时间点
2. 观测值有非独立的交叉特征，但 HMM 要求观察独立

HMM v.s. CRF
====================

.. list-table:: 
    :width: 100%
    :widths: 6 47 47
    :header-rows: 1

    * - 
      - HMM
      - CRF 
    * - 
      - 生成模型

        根据 X, 输出 Y 的生成关系
      - 判别模型

        根据 X, 预测输出的 Y 


HMM v.s. Bayes
====================

.. list-table:: 
    :width: 100%
    :widths: 6 47 47
    :header-rows: 1

    * - 
      - HMM
      - Bays 
    * - 
      - 变量间存在相关性，但难以获得显式的因果关系
      - 获得显式的因果关系


Reference
********************

- `HMM隐马尔可夫模型的例子、原理、计算和应用 <https://zhuanlan.zhihu.com/p/111899116>`_
