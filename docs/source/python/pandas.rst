pandas
##########

DataFrame configs
********************

index & columns
====================

.. note:: 这里行索引 ``.index`` 相较于下标的索引，更像是一个跟 ``.columns`` 同等概念的 **label**
    | 不是 1,2,3,... 
    | 也可以是 a,b,c,...
    | 也可以是自定义的 Lily, Lucy, ...

.. code-block:: pycon
    :emphasize-lines: 9,11

    >>> df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Aritra'],
    ...                    'Age': [25, 30, 35],
    ...                    'Location': ['Seattle', 'New York', 'Kona']},
    ...                   index=([10, 20, 30]))
    	Name	Age	Location
    10	Alice	25	Seattle
    20	Bob	30	New York
    30	Aritra	35	Kona
    >>> df.index  # 行label
    Index([10, 20, 30], dtype='int64')
    >>> df.columns  # 列label
    Index(['Name', 'Age', 'Location'], dtype='object')

.. danger:: axis = 0 & 1

    .. image:: ./pics/pandas_axis.png

    - ``axis = 0`` 向下执行方法
    - ``axis = 1`` 横向执行对应的方法

    `pandas中的axis=0,axis=1,傻傻分不清楚 <https://www.cnblogs.com/nxf-rabbit75/p/10044801.html>`_

Basic attributes
====================

.. code-block:: pycon

    >>> df.shape
    (5, 3)  # Tuple



operation
********************

check
==========

.. grid:: 2

    .. grid-item::
        .. code-block:: py

            df= pd.DataFrame(
                {
                    'Name': [None, 'Bob', 'Aritra'],
                    'Age': [25, 30, 35],
                    'Location': ['Seattle', 'New York', 'Kona']
                },
                index=([10, 20, 30])
            )

    .. grid-item::
        .. code-block:: pycon

                Name	Age	Location
            10	None	25	Seattle
            20	Bob	30	New York
            30	Aritra	35	Kona

.. code-block:: pycon

    >>> df.head(n)
    >>> df.tail(n)

空 NULL
----------

.. code-block:: pycon

    >>> df.isnull()  # 每一个值
        Name	Age	Location
    10	True	False	False
    20	False	False	False
    30	False	False	False
    >>> df.fillna(value=1)  # 填充空值
        Name	Age	Location
    10	1	25	Seattle
    20	Bob	30	New York
    30	Aritra	35	Kona

.. grid:: 2

    .. grid-item::
        .. code-block:: pycon
            :caption: axis = 0

            >>> df.null().any()  # 纵向check
                Name         True
            Age         False
            Location    False
            dtype: bool
            >>> df.dropna()  # 纵向搜寻一行行 drop行
            Name	Age	Location
            20	Bob	30	New York
            30	Aritra	35	Kona

    .. grid-item::
        .. code-block:: pycon
            :caption: axis = 1

            >>> df.null().any(axis=1)  # 横向check
            10     True
            20    False
            30    False
            dtype: bool
            >>> df.dropna(axis=1)  # 横向搜寻一列列 drop列
            Age	Location
            10	25	Seattle
            20	30	New York
            30	35	Kon


去重
----------

.. code-block:: pycon
    
    >>> df.duplicated()  # check 重复行
    >>> df.drop_duplicates()  # del 重复行

是否存在某些值
--------------------

.. code-block:: pycon
    
    >>> df.isin(values=['New York', 'BJ'])
        Name	Age	Location
    10	False	False	False
    20	False	False	True
    30	False	False	False


取 df 特定的行或列 
==============================

.. note:: ``i`` & ``[i]``

    前者 series， 后者 DataFrame

    .. grid:: 2

        .. grid-item::
            .. code-block:: py
                :caption: i =》Series

                temp_df['str']  # 列
                temp_df.loc[1]  # 行
                temp_df.loc[1:3, 'str']  # 列

        .. grid-item::
            .. code-block:: py
                :caption: [i] =》DataFrame

                temp_df[['str']]  # 列
                temp_df.loc[[1]]  # 行
                emp_df.loc[1:3, ['str']]  # 列

.. grid:: 2

    .. grid-item::
        .. code-block:: py
            :caption: generate dataframe

            import pandas as pd

            str_beg, int_beg, float_beg = ord('a'), 1, .1
            temp = list()
            for i in range(0, 10, 2):
                temp.append({
                    'str': chr(str_beg+i)*(i+1),
                    'int': int_beg+i,
                    'float': float_beg + i*.1
                    
                })
            temp_df = pd.DataFrame(temp)

    .. grid-item::
        .. table::

            +-+---------+---+-----+
            | |str      |int|float|
            +=+=========+===+=====+
            |0|a        |1  |0.1  |
            +-+------------+-----+
            |1|ccc      |3  |0.3  |
            +-+---------+---+-----+
            |2|eeeee    |5  |0.5  |
            +-+---------+---+-----+
            |3|ggggggg  |7  |0.7  |
            +-+---------+---+-----+
            |4|iiiiiiiii|9  |0.9  |
            +-+---------+---+-----+

.. grid:: 2

    .. grid-item::
        .. code-block:: pycon
            :caption: 简单取行

            ???

    .. grid-item::
        .. code-block:: pycon
            :caption: 简单取列

            >>> temp_df['str']
            pandas.core.series.Series
            >>> temp_df[['str']]
            pandas.core.frame.DataFrame
            >>> temp_df[['str', 'int']]  # 取两列

``loc``
----------

Purely label-location based indexer for selection by label.

.. note:: 这里行索引 相较于下标的索引，更像是一个跟 column_name 同等概念的 **label**
    | 不是 1,2,3,... 
    | 也可以是 a,b,c,...
    | 也可以是自定义的 Lily, Lucy, ...

- 行列 ``,`` 隔开
- 行列的输入格式都可以是 

    - ``label`` 纯label = 单行 or 单列 or 单个值 =》 ``series``
    - ``[label]`` 跟上面除了返回形式是 ``dataframe`` 不一样，值一样
    - ``beg:end`` 切片形式
    - ``(label1, label2, ...)`` 选择性挑行或列
    - ``condition`` & ``list[bool]*n`` 可對齊 bool sequence

- ``dataframe.loc[行,列]``
- ``dataframe.loc[行]``
- ``dataframe.loc[:, 列]``

.. grid:: 2

    .. grid-item:: 
        .. code-block:: pycon
            :caption: 行索引切片

            >>> temp_df.loc[1]  # Series
            str      ccc
            int        3
            float    0.3
            Name: 1, dtype: object
            >>> temp_df.loc[1:3]  # 全部显示列
            	str	int	float
            1	ccc	3	0.3
            2	eeeee	5	0.5
            3	ggggggg	7	0.7
            >>> temp_df.loc[1:3, 'str']  # 锁定 str 列 Series
            1        ccc
            2      eeeee
            3    ggggggg
            Name: str, dtype: object
            >>> temp_df.loc[1:3, ['str']]  # 锁定 str 列 dataframe
                str
            1	ccc
            2	eeeee
            3	ggggggg



    .. grid-item:: 
        .. code-block:: pycon
            :caption: 行索引列表

            >>> temp_df.loc[[1, 2, 3]]  # 行索引列表  dataframe
                str	int	float
            1	ccc	3	0.3
            2	eeeee	5	0.5
            3	ggggggg	7	0.7
            >>> temp_df.loc[[1, 2, 3], 'str']  # 锁定 str 列  Series
            1        ccc
            2      eeeee
            3    ggggggg
            Name: str, dtype: object

    .. grid-item::
        .. code-block:: pycon
            :caption: condition = 一一对应的bool 列表

            >>> temp_df.loc[temp_df['int']>5]
            str	int	float
            3	ggggggg	7	0.7
            4	iiiiiiiii	9	0.9
            >>> temp_df.loc[[True, False, True, False, True], ['int']]
            #  bool list
            	int
            0	1
            2	5
            4	9
            >>> temp_df.loc[map(lambda x:len(x)>3, temp_df['str'])]
            # 实质也是bool list
            	str	int	float
            2	eeeee	5	0.5
            3	ggggggg	7	0.7
            4	iiiiiiiii	9	0.9
            >>> temp_df.loc[len(temp_df['str'])>3, ['int']]
            KeyError: 'True: boolean label can not be used without a boolean index'

.. grid-item::
    .. code-block:: pycon
        :caption: 取列

        >>> temp_df.loc[:, 'str':'int']
        	str	int
        0	a	1
        1	ccc	3
        2	eeeee	5
        3	ggggggg	7
        4	iiiiiiiii	9
        >>> temp_df.loc[1:2, 'str':'int']  # 1-3, str-int
        str	int
        1	ccc	3
        2	eeeee	5
        >>> temp_df.loc[[1,3], ('str','float')]  # 1&3, str&float
            str	float
        1	ccc	0.3
        3	ggggggg	0.7


df 替换 
==========


`iloc <https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html>`_

.. note:: Purely integer-location based indexing for selection by position.
    纯靠索引, 无论是行还是列, 无论是否有label.

.. grid:: 2

    .. grid-item::

        .. code-block:: pycon
            
        >>> df.iloc[1:3, 0:3]
        >>> df.iloc[[0, 2], [1, 3]]
        >>> df.iloc[:, lambda df: [0, 2]]




`pandas取dataframe特定行/列 <https://www.cnblogs.com/nxf-rabbit75/p/10105271.html>`_
`pandas.DataFrame.loc <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html>`_