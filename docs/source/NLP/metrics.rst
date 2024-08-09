metrics
####################

text
**********



    | character error rate (CER) 纯 Mandarin
    | word error rate (WER) 纯 English
    | mix error rate (MER) 各自语言用各自统计

error rate
====================

||CER|WER|MER|
|level|character|word|separated|
|lang|zh|en|zh_en|


==Character Error Rate== the percentage of characters that have been transcribed incorrectly by the Text Recognition model. 

低于 10% 会认为很有效

.. math:: 

    \text{\_ER} = \cfrac{S+D+I}{\red{\text{ref}}}\qquad\begin{cases}S:=substitution\\D:=deletion\\I:=insertion\end{cases}


.. grid:: 2

    .. grid-item::

        .. code-block:: py

            """
            hyp = pred
            ref = target
            """
        
            from torchmetrics.text import CharErrorRate
            cer = CharErrorRate()
            cer(hyp, ref)

            import pywer
            pywer.cer(ref, hyp)

    .. grid-item::
        



