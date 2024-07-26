Phonetic related 
##############################

`基于音形码的汉字相似度比对算法 <https://cn.oversea.cnki.net/KCMS/detail/detail.aspx?filename=HDZJ201811016&dbcode=CFJD&dbname=>`_ ``2018``
************************************************************************************************************************************************************************************

.. hint:: Abstract

    ==字音== ==字形== ==编码== ==相似度==

    汉字相似度计算不仅是语言研究最基础的一项研究,而且对汉字输入法的校验有着重要的意义.为了准确的计算出汉字的相似,基于编辑距离算法的基础上,文中提出一种 ==基于音形码汉字匹配算法== ;最后,通过实验证明在两种算法编码方式相同的情况下,音形码汉字匹配算法准确率高于编辑距离算法.

.. note:: Summary

    1. 特征：字音 + 字形
    2. 编码：自创编码 转成二进制
    3. 距离：汉明 dis

**keypoints：**

1. 每一个汉字 :math:`a` =》 10 个音形码 :math:`d=f(a)`

    - 前4个字音 = (韵母，声母，补码，声调)
    
        **补码：** 如果汉字拼音的声母和韵母之间有一个辅音的话，利用的是韵母表映射的表示规则，如果没有的话默认0
        .. caution:: 什么是辅音，辅音和声母又有什么区别？？paper没有为1的例子

    - 后6个字形 = （结构，左上角，右上角，左下角，右下角）
    - 替代的规则是：查自定义的表

2. 10个音形码  :math:`d=f(a)` =》 40个二进制编码 :math:`q=c_0c_1\dots c_39`

    - :math:`c_i` 为1比特

    - 若音形码的某一位超出16进制则转为16进制，留高位舍低位。
    
        .. hint:: G = 16 => 1

3. 如果是字符串，将每个词中相应汉字的音形码进行 **累加**，将累加后的音形码转化为二进制作为改词的音形码的值。

    .. caution:: 这真的可以吗？？看不懂例子

4. 汉明距离：位不同的个数 

.. math::

    Sim(a, b) = 1-\cfrac{hm(a,b)}{\text{length } 40} 

.. hint:: example

    .. mermaid::

        flowchart LR
        A[琅]
        B[lang2]
        C[字形]
        D[F702]
        E[11313B]
        F[F70211313B]
        G[111101110000001000010001]
        A --字音--> B
        A --字形--> C
        B --查表--> D
        C --查表-->E
        D --拼接-->F
        E --拼接-->F
        F-->G

        H[F702]
        I[15 07 00 02]
        J[1111 0111 0000 0010]
        H --16--> I 
        I --16_to_2--> J

    .. table::


        +------+------------------------+------------------------+------------------------------+
        |      |琅                      |狼                      |dis                           |
        +======+========================+========================+==============================+
        |拼音  |lang2                   |lang2                   |                              |
        +------+------------------------+------------------------+------------------------------+
        |音形码|F702                    |F702                    |edit-distance                 |
        +      +                        +                        +                              +
        |      |11313B                  |14323A                  |:math:`1-\cfrac{4}{10}=.6`    |
        +------+------------------------+------------------------+------------------------------+
        |二进制|1111011100000010        |1111011100000010        |paper                         |
        +      +                        +                        +                              +
        |      |000100010011000100111001|000101000011001000111010|:math:`1-\cfrac{5}{40}=.875`  |
        +------+------------------------+------------------------+------------------------------+


MFCCs 和 DTW 在拼音相似度中的研究
****************************************

`HANSpeller++: A unified framework for Chinese spelling correction <https://scholar.google.com.au/citations?view_op=view_citation&hl=sl&user=2Sp3OuMAAAAJ&citation_for_view=2Sp3OuMAAAAJ:UeHWp8X0CEIC>`_
**********************************************************************************************************************************************************************************************************************************************************

.. hint:: Abstract

    | Increased interest in China from foreigners has led to a corresponding interest in the study of Chinese. However, the learning of Chinese by non-native speakers will encounter many difficulties, Chinese spelling check techniques for Chinese as a Foreign Language (CFL) learners is highly desirable. This paper presents our work on the **SIGHAN-2015 Chinese Spelling Check task.** The task focuses on spelling checking on Chinese essays written by CFL learners. We propose a unified framework called HANSpeller++ based on our previous HANSpeller for Chinese spelling correction. 
    | **The framework consists of candidate generating, candidates re-ranking and final global decision making. Experiments show good performance on the test data of the task.**

**process**

1. preprocess：

    1. 用标点切分子句，子句是 basic unit of the error correction process
    2. 用 unicode 筛删 非中文字符
2. candidate generating top K

    | We first initialize a fixed size priority queue for a certain input sub sentence, this queue is used to store intermediate sub sentences.
    | For each character of sentences in the priority queue, we try to replace it by its candidate character. The possible candidate character include its homophone, near-homophone, similar shape character and confusion pair
