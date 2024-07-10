pandas
##########

operation
********************

取 df 特定的行或列
==============================

.. grid:: 2

    .. grid-item::
        .. code-block:: py
            :caption: generate dataframe

            import pandas as pd

            str_beg, int_beg, float_beg = ord('a'), 1, .1
            temp = list()
            for i in range(10):
                temp.append({
                    'str': chr(str_beg+i),
                    'int': int_beg+i,
                    'float': float_beg + i*.1
                    
                })
            temp_def = pd.DataFrame(temp)

    .. grid-item::
        .. table::

            +-+---+---+-----+
            | |str|int|float|
            +=+===+===+=====+
            |0|a  |1  |0.1  |
            +-+---+---+-----+
            |1|b  |2  |0.2  |
            +-+---+---+-----+
            |2|c  |3  |0.3  |
            +-+---+---+-----+
            |3|d  |4  |0.4  |
            +-+---+---+-----+
            |4|e  |5  |0.5  |
            +-+---+---+-----+
            |5|f  |6  |0.6  |
            +-+---+---+-----+
            |6|g  |7  |0.7  |
            +-+---+---+-----+
            |7|h  |8  |0.8  |
            +-+---+---+-----+
            |8|i  |9  |0.9  |
            +-+---+---+-----+
            |9|j  |10 |1.0  |
            +-+---+---+-----+

.. grid:: 2

    .. grid-item::
        .. code-block:: pycon
            :caption: 简单取行

    .. grid-item::
        .. code-block:: pycon
            :caption: 简单取列

            >>> temp_df'['str']
            pandas.core.series.Series
            >>> temp_df[['str']]
            pandas.core.frame.DataFrame

            >>> temp_df[['str', 'int']]  # 取两列


取行
----------



取列
----------









`pandas取dataframe特定行/列 <https://www.cnblogs.com/nxf-rabbit75/p/10105271.html>`_