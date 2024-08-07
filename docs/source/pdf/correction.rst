
# Correction

.. hint:: Example
    
    .. grid:: 2 
        
        .. grid-item::
            
            Left is original text.

        .. grid-item::
            right is the result

chatgpt
**********

prompts
==========

original
--------------------

.. hint:: Example

    .. code-block:: py

        """
        I got a transcript from Cantonese ASR. Can you help to correct those wrong recognition. 
        Here are the transcript.
        """
    
    .. grid:: 2 
        
        .. grid-item::

            大家好今日我哋好高興同大家宣佈香港政府呢個新環環保計劃。目的係！推廣海在新能源使用，而家就請講姐同大家喺廣州一下計劃嘅細節啦。香港政府嘅呢個新環保嘅話，系飛非常重要嘅目的系，希望減少我哋哋嘅太排房量同時。發展我哋嘅目標係將可在收能源嘅少使用用量提高度總能圓往客。之十宜家政府都會提供嘅經歷措施、古力企業同家庭庭去安裝在最生能如系統.
            
        .. grid-item::
            大家好，今日我哋好高興同大家宣佈香港政府呢個新環保計劃。目的係推廣海洋新能源使用，而家就請講者同大家喺廣州一齊講解呢個計劃嘅細節啦。香港政府嘅呢個新環保計劃嘅話，係非常重要嘅，目的係希望減少我哋嘅碳排放量同時發展我哋嘅目標係將可再生能源嘅使用量提高到總能源消耗嘅百分之十。而家政府都會提供嘅措施，係鼓勵企業同家庭去安裝最新嘅太陽能系統。


    .. table::
        :align: center

        +-----------+----------------------+--------------------------+---+
        |errror type|asr                   |res                       |eva|
        +===========+======================+==========================+===+
        |冗余       |環環保                |環保                      |✅ |
        +           +----------------------+--------------------------+---+
        |           |廣州一下              |廣州一齊                  |❌ |
        +           +----------------------+--------------------------+---+
        |           |飛非常重要            |非常重要                  |✅ |
        +           +----------------------+--------------------------+---+
        |           |我哋哋                |我哋                      |✅ |
        +           +----------------------+--------------------------+---+
        |           |能源嘅少使用用量      |能源嘅使用量              |✅ |
        +           +----------------------+--------------------------+---+
        |           |家庭庭                |家庭                      |✅ |
        +-----------+----------------------+--------------------------+---+
        |少字                                                             |
        +-----------+----------------------+--------------------------+---+
        |音似       |海在新能源            |海洋新能源                |❌ |
        +           +----------------------+--------------------------+---+
        |           |講姐                  |講者                      |✅ |
        +           +----------------------+--------------------------+---+
        |           |新環保嘅話            |新環保計劃嘅話            |❌ |
        +           +----------------------+--------------------------+---+
        |           |太排房量              |碳排放量                  |✅ |
        +           +----------------------+--------------------------+---+
        |           |可在收能源            |可再生能源                |✅ |
        +           +----------------------+--------------------------+---+
        |           |古力                  |鼓勵                      |✅ |
        +           +----------------------+--------------------------+---+
        |           |在最生能如系統        |最新嘅太陽能系統          |❌ |
        +-----------+----------------------+--------------------------+---+
        |边界       |目的係！推廣          |目的係推廣                |✅ |
        +           +----------------------+--------------------------+---+
        |           |非常重要嘅目的系，希望|非常重要嘅，目的係希望    |✅ |
        +-----------+----------------------+--------------------------+---+
        |ASR        |提高度總能圓往客。之十|提高到總能源消耗嘅百分之十|✅ |
        +           +----------------------+--------------------------+---+
        |           |提供嘅經歷措施        |提供嘅措施                |❌ |
        +-----------+----------------------+--------------------------+---+


引入音素信息
--------------------

| 但在中文ASR的场景下，很多情况是由于读音相同或相近导致的识别错误。
| 收录常见字的粤语发音作为输入的一部分
| `长文字自助粤语注音 <https://shyyp.net/romanizer?x=d529e75d76fc289af90b0fecbb8ca547>`_

.. hint:: Example

    .. code-block:: py

        """
        I got a transcript from Cantonese ASR. Can you help to correct those wrong recognition. 
        Here are the transcript and its Cantonese pronunciation:
        """
    .. grid:: 2 
        
        .. grid-item::

            | 大家好今日我哋好高興同大家宣佈香港政府呢個新環環保計劃。目的係！推廣海在新能源使用，而家就請講姐同大家喺廣州一下計劃嘅細節啦。香港政府嘅呢個新環保嘅話，系飛非常重要嘅目的系，希望減少我哋哋嘅太排房量同時。發展我哋嘅目標係將可在收能源嘅少使用用量提高度總能圓往客。之十宜家政府都會提供嘅經歷措施、古力企業同家庭庭去安裝在最生能如系統.
            | daai6 gaa1 hou2 gam1 jat6 ngo5 dei6 hou2 gou1 hing1 tung4 daai6 gaa1 syun1 bou3 hoeng1 gong2 zing3 fu2 ne1 go3 san1 waan4 waan4 bou2 gai3 waak6。muk6 dik1 hai6 ！teoi1 gwong2 hoi2 zoi6 san1 nang4 jyun4 si3  jung6 ， ji4  gaa1 zau6 cing2 gong2 ze2 tung4 daai6 gaa1 hai2 gwong2 zau1 jat1 haa6 gai3 waak6 ge3 sai3 zit3 laa1。hoeng1 gong2 zing3 fu2  ge3 ne1 go3 san1 waan4 bou2 ge3 waa6 ， hai6 fei1 fei1 soeng4 zung6 jiu3 ge3 muk6 dik1 hai6 gai3, hei1 mong6 gaam2 siu3 ngo5 dei6 dei6 ge3 taai3 paai4 fong4 loeng6 tung4 si4。faat3 zin2 ngo5 dei6 ge3 muk6 biu1 hai6 zoeng3 ho2 zoi6 sau1 nang4 jyun4 ge3 siu3 si3 jung6 jung6 loeng6 tai4 gou1 dok6 zung2 nang4 jyun4 wong5 haak3。zi1 sap6 ji4 gaa1 zing3 fu2 dou1 wui6 tai4 gung1 ge3 ging1 lik6 cou3 si1、 gu2 lik6 kei5 jip6 tung4 gaa1 ting4 ting4heoi3 on1 zong1 zoi6 zeoi3 saang1 nang4 jyu4 hai6 tung2.
            
        .. grid-item::
            大家好，今日我哋好高興同大家宣佈香港政府呢個新環保計劃。目的係推廣海洋新能源使用，而家就請講者同大家喺廣州一齊講解呢個計劃嘅細節啦。香港政府嘅呢個新環保嘅話，系非常重要嘅，目的係希望減少我哋嘅碳排放量同時發展我哋嘅目標係將可再生能源嘅使用量提高到總能源消耗嘅百分之十。而家政府都會提供嘅措施，係鼓勵企業同家庭去安裝最新嘅太陽能系統。


    .. table::

        +-----------+----------------------+--------------------------+---+
        |errror type|asr                   |res                       |eva|
        +===========+======================+==========================+===+
        |冗余       |環環保                |環保                      |✅ |
        +           +----------------------+--------------------------+---+
        |           |廣州一下              |廣州一齊                  |❌ |
        +           +----------------------+--------------------------+---+
        |           |飛非常重要            |非常重要                  |✅ |
        +           +----------------------+--------------------------+---+
        |           |我哋哋                |我哋                      |✅ |
        +           +----------------------+--------------------------+---+
        |           |能源嘅少使用用量      |能源嘅使用量              |✅ |
        +           +----------------------+--------------------------+---+
        |           |家庭庭                |家庭                      |✅ |
        +-----------+----------------------+--------------------------+---+
        |少字                                                             |
        +-----------+----------------------+--------------------------+---+
        |音似       |海在新能源            |海洋新能源                |❌ |
        +           +----------------------+--------------------------+---+
        |           |講姐                  |講者                      |✅ |
        +           +----------------------+--------------------------+---+
        |           |新環保嘅話            |新環保計劃嘅話            |❌ |
        +           +----------------------+--------------------------+---+
        |           |太排房量              |碳排放量                  |✅ |
        +           +----------------------+--------------------------+---+
        |           |可在收能源            |可再生能源                |✅ |
        +           +----------------------+--------------------------+---+
        |           |古力                  |鼓勵                      |✅ |
        +           +----------------------+--------------------------+---+
        |           |在最生能如系統        |最新嘅太陽能系統          |❌ |
        +-----------+----------------------+--------------------------+---+
        |边界       |目的係！推廣          |目的係推廣                |✅ |
        +           +----------------------+--------------------------+---+
        |           |非常重要嘅目的系，希望|非常重要嘅，目的係希望    |✅ |
        +-----------+----------------------+--------------------------+---+
        |ASR        |提高度總能圓往客。之十|提高到總能源消耗嘅百分之十|✅ |
        +           +----------------------+--------------------------+---+
        |           |提供嘅經歷措施        |提供嘅措施                |❌ |
        +-----------+----------------------+--------------------------+---+

    没有变化

提供错误的类型，追加分类任务
----------------------------------------

`by pycorrector <https://github.com/shibing624/pycorrector/raw/master/docs/git_image/error_type.png>`_

.. table::

    +----------+----+---------------------+------------------+----------------+
    |冗余      |少字|音似                 |边界              |ASR             |
    +==========+====+=====================+==================+================+
    |Redundancy|Lack|Similar Pronunciation|Punctuation errors|Contextual error|
    +----------+----+---------------------+------------------+----------------+

.. hint:: Example

    .. code-block:: py

        """
        I got a transcript from Cantonese ASR. Can you help to correct those wrong recognition and classify the errors with '1.Redundancy, 2.Lack, 3.Similar Pronunciation error, 4.Punctuation errors, 5, Contextual error'. Here are the transcript:
        """
    .. grid:: 2 
        
        .. grid-item::

            大家好今日我哋好高興同大家宣佈香港政府呢個新環環保計劃。目的係！推廣海在新能源使用，而家就請講姐同大家喺廣州一下計劃嘅細節啦。香港政府嘅呢個新環保嘅話，系飛非常重要嘅目的系，希望減少我哋哋嘅太排房量同時。發展我哋嘅目標係將可在收能源嘅少使用用量提高度總能圓往客。之十宜家政府都會提供嘅經歷措施、古力企業同家庭庭去安裝在最生能如系統.

Act as a Cantonese Pronunciation Helper
--------------------------------------------------

Act as a Prompt Generator
----------------------------------------

.. hint:: Example

    .. code-block:: py

        """
        I got a transcript from Cantonese ASR. Can you help to correct those wrong recognition. 
        Here are the transcript and its Cantonese pronunciation:
        """
    .. grid:: 2 
        
        .. grid-item::

            | 大家好今日我哋好高興同大家宣佈香港政府呢個新環環保計劃。目的係！推廣海在新能源使用，而家就請講姐同大家喺廣州一下計劃嘅細節啦。香港政府嘅呢個新環保嘅話，系飛非常重要嘅目的系，希望減少我哋哋嘅太排房量同時。發展我哋嘅目標係將可在收能源嘅少使用用量提高度總能圓往客。之十宜家政府都會提供嘅經歷措施、古力企業同家庭庭去安裝在最生能如系統.
            | daai6 gaa1 hou2 gam1 jat6 ngo5 dei6 hou2 gou1 hing1 tung4 daai6 gaa1 syun1 bou3 hoeng1 gong2 zing3 fu2 ne1 go3 san1 waan4 waan4 bou2 gai3 waak6。muk6 dik1 hai6 ！teoi1 gwong2 hoi2 zoi6 san1 nang4 jyun4 si3  jung6 ， ji4  gaa1 zau6 cing2 gong2 ze2 tung4 daai6 gaa1 hai2 gwong2 zau1 jat1 haa6 gai3 waak6 ge3 sai3 zit3 laa1。hoeng1 gong2 zing3 fu2  ge3 ne1 go3 san1 waan4 bou2 ge3 waa6 ， hai6 fei1 fei1 soeng4 zung6 jiu3 ge3 muk6 dik1 hai6 gai3, hei1 mong6 gaam2 siu3 ngo5 dei6 dei6 ge3 taai3 paai4 fong4 loeng6 tung4 si4。faat3 zin2 ngo5 dei6 ge3 muk6 biu1 hai6 zoeng3 ho2 zoi6 sau1 nang4 jyun4 ge3 siu3 si3 jung6 jung6 loeng6 tai4 gou1 dok6 zung2 nang4 jyun4 wong5 haak3。zi1 sap6 ji4 gaa1 zing3 fu2 dou1 wui6 tai4 gung1 ge3 ging1 lik6 cou3 si1、 gu2 lik6 kei5 jip6 tung4 gaa1 ting4 ting4heoi3 on1 zong1 zoi6 zeoi3 saang1 nang4 jyu4 hai6 tung2.
            
        .. grid-item::
            大家好，今日我哋好高興同大家宣佈香港政府呢個新環保計劃。目的係推廣海洋新能源使用，而家就請講者同大家喺廣州一齊講解呢個計劃嘅細節啦。香港政府嘅呢個新環保嘅話，系非常重要嘅，目的係希望減少我哋嘅碳排放量同時發展我哋嘅目標係將可再生能源嘅使用量提高到總能源消耗嘅百分之十。而家政府都會提供嘅措施，係鼓勵企業同家庭去安裝最新嘅太陽能系統。

