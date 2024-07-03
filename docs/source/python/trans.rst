
# 交叉

.. note:: array_2_tensor

    - ``torch.from_numpy(arr)`` 浅拷贝, 直接共享内存内存空间的，这样效率更高
    - ``torch.Tensor(arr)`` 深拷贝，创建一个新的副本
    
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



.. note:: ``tensor.view(-1, n)`` & ``arr.reshape(-1, n)``



