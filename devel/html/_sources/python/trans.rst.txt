交叉
##########

.. note:: array_tensor

    .. table::

        +-----------------+---------------------------+-------+--------+----------+
        |                 |                           |拷贝   |共享内存|创建新副本|
        +=================+===========================+=======+========+==========+
        |array_2_tensor   | ``torch.from_numpy(arr)`` | 浅拷贝|✅      |❌        |
        +                 +---------------------------+-------+--------+----------+
        |                 | ``torch.Tensor(arr)``     | 深拷贝|❌      |✅        |
        +-----------------+---------------------------+-------+--------+----------+
        |tensor_2_array   | ``t.numpy(arr)``          | 浅拷贝|✅      |❌        |
        +-----------------+---------------------------+-------+--------+----------+
        |dataframe_2_array| ``np.array(df)``          | 深拷贝|❌      |✅        |
        +-----------------+---------------------------+-------+--------+----------+
        |array_2_dataframe| ``pd.DataFrame(arr)``     | 浅拷贝|✅      |❌        |
        +-----------------+---------------------------+-------+--------+----------+
    
.. code-block:: pycon
    :caption: array_2_tensor

    >>> import torch
    >>> import numpy as np

    >>> arr = np.array([1, .2, 3])
    array([1. , 0.2, 3. ])
    >>> t1 = torch.from_numpy(arr)
    tensor([1.0000, 0.2000, 3.0000], dtype=torch.float64)
    >>> t2 = torch.Tensor(arr)
    tensor([1.0000, 0.2000, 3.0000])

    >>> arr[1] = 0
    array([1., 0., 3.])
    t1 = tensor([1., 0., 3.], dtype=torch.float64)
    t2 = tensor([1.0000, 0.2000, 3.0000])


.. code-block:: pycon
    :caption: tensor_2_array

    >>> import torch
    >>> import numpy as np
    >>> t = torch.tensor([1,.2, 3])
    tensor([1.0000, 0.2000, 3.0000])
    >>> arr = t.numpy() 
    array([1. , 0.2, 3. ], dtype=float32)
    >>> t[1]=0
    arr = array([1., 0., 3.], dtype=float32)

.. code-block:: pycon
    :caption: dataframe_2_array

    >>> import pandas as pd
    >>> import numpy as np

    >>> df = pd.DataFrame([[1,2],[2,3]])
        0   1
    0   1   2
    1   2   3
    >>> arr = np.array(df)
    array([[1, 2],[2, 3]], dtype=int64)

    >>> df[0][0]=0
    arr = array([[1, 2], [2, 3]], dtype=int64) 深拷贝


.. code-block:: pycon
    :caption: array_2_dataframe

    >>> import pandas as pd
    >>> import numpy as np

    >>> arr = np.array([[1,2],[3,4]]
    array([[1, 2],[3, 4]])
    >>> df = pd.DataFrame(arr)
        0  1
    0   1  2
    1   3  4

    >>> arr[0][0]=0
        0  1
    0   0  2
    1   3  4



`【Pytorch】numpy数组与tensor互相转换的多种方法 <https://blog.csdn.net/qq_42346574/article/details/120100424?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-120100424-blog-129714906.235^v43^pc_blog_bottom_relevance_base5&spm=1001.2101.3001.4242.1&utm_relevant_index=3>`_



.. note:: ``tensor.view(-1, n)`` & ``arr.reshape(-1, n)``

## modeling

### 划分数据集

.. code-block:: py

    from sklearn.model_selection import train_test_split


.. code-block:: py
    :caption: np.random.choice

    import numpy as np
    
    total, partition = len(datas), 0.2
    test_index = np.random.choice(
        np.arange(total),
        size=ceil(partition *total),   # 计算要抽的数量 
        replace=False  # 不放回抽样
    )
    test_index = np.array(test_index)
    train_index = np.delete(np.arange(total), test_index)  # 总共的索引删掉test的索引

    # 生成索引对应的数据集
    train_datas = list(map(lambda x: datas[x], train_index))
    test_datas = list(map(lambda x: datas[x], test_index))




