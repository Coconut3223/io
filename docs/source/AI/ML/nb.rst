Naive Bayes classifier
##############################

In statistics, ==naive Bayes classifiers== are a family of simple "**probabilistic classifiers**" based on applying Bayes' theorem with **strong (naive) independence assumptions** between the features.

Background
********************

| ==Conditional probability== 。  :math:`P(A|B)=\frac{P(AB)}{P(B)}, P(B|A)=\frac{P(AB)}{P(A)}` 
| ==Bayes' Theorem== Suppose  :math:`B_1, · · · , B_n`  form a partition of the sample space  :math:`S`  (mutually exclusive and collectively exhaustive), then for any  :math:`k = 1, · · · n`  and any event  :math:`A` 

.. math::
    P(B_k|A) =\frac{P(B_kA)}{P(A)}=\cfrac{P(A|B_k)P(B_k)}{P(A|B_1)P(B_1)+\dots+P(A|B_k)P(B_k)} :math:`` 

.. hint:: **cancer diagnostic testing.**
    | C denote the event that a patient has a cancer.
    | B denote the event that the test reports “positive” for the patient
    | Some laboratory studies show that  :math:`P (C) = 0.001, P (B|C)=0.99, P(B|C) = 0.01` .

    | We apply the Bayes’ Theorem to give
    | :math:`P (C|B) = \cfrac{P (C)P (B|C)}{P (C)P (B|C) + P (C)P (B|C)}=\cfrac{0.001 × 0.99}{0.999 × 0.01 + 0.001 × 0.99}= 0.09016393` 
    | So for the rare disease, even though the test is very precise, a positive report may still have an overwhelming probability to be a mistake.

Content
**********

| ==Bayesian Classifiers, Idiot's Bayes== .
| Choose value of  :math:`C`  that maximizes  :math:`P (C|A_1, A_2, . . . , A_n)` 

.. math::
    \begin{align*}C&:=\max_CP(C|A_1,...,A_n)\\&=\max_C\cfrac{P(A_1,...,A_n|C)P(C)}{P(A_1,...,A_n)}\\&\propto\max_CP(A_1,...,A_n|C)P(C)\end{align*}

**how to estimate**  :math:`P (A_1, . . . , An|C)`  ?

.. warning:: Assume independence among attributes  :math:`A_i`  when class is given  :math:`P(A_1,...,A_n|C_j) =\prod\limits_{i=1}^nP(A_i|C_j)`
    
    .. math::
        \begin{align*}C&:=\max_CP(C|A_1,...,A_n)\\&=\max_C\cfrac{P(A_1,...,A_n|C)P(C)}{P(A_1,...,A_n)}\\&\propto\max_CP(A_1,...,A_n|C)P(C)\\&\xlongequal{\text{Independent}}\max_C\prod\limits_{i=1}^nP(A_i|C)P(C)\end{align*} 

| **Wrong when lack represent data.**
| 如果在 C 类样本中在 i-th 特征上没有存在第 k 个值。那么按照原来的计算，只要 i-th = k，那么永远不可能是C，因为算出来直接为0.  :math:`P(A_{i:k}|C)=\cfrac{N_{i:k,C}}{N_C}\xlongequal{N_{k,C}=0}0\implies\prod\limits_{i=1}^nP(A_i|C)P(C)=0` 

引入 ==Laplace smoothing==

.. math::
    P(A_i|C) = \cfrac{N_{i,C}+\alpha}{N_C+\alpha\times(\#A_i)}

| :math:`\#A_i:=`  the total number of classes that Ai possibly belong to
| :math:`\alpha\gt0`  is a parameter. Usually set as 1.


.. hint:: New sample: Name=human; GiveBirth=yes; LayEggs=no; CanFly=no; HaveLegs=yes; Class=?

    .. image:: ./pics/nb_1.png
        :scale: 30%
    
    | mammal=5; Non-mammal=10,  :math:`\alpha=1` 
    | calculate  :math:`P(A_i|C)` 

    .. table::

        +------+--------------------------+--------------------------+--------------------------+--------------------------+---------------------------+
        |class |GiveB.=Y                  |LayE.=N                   |CanF.=N                   |HaveL.=Y                  | :math:`P(C)`              |
        +======+==========================+==========================+==========================+==========================+===========================+
        |Mammal| :math:`\frac{5+1}{5+2}`  | :math:`\frac{5+1}{5+2}`  | :math:`\frac{4+1}{5+2}`  | :math:`\frac{3+1}{5+2}`  | :math:`\frac{5+1}{15+2}`  |
        +------+--------------------------+--------------------------+--------------------------+--------------------------+---------------------------+
        |Non-  | :math:`\frac{1+1}{10+2}` | :math:`\frac{1+1}{10+2}` | :math:`\frac{7+1}{10+2}` | :math:`\frac{7+1}{10+2}` | :math:`\frac{10+1}{15+2}` |
        +------+--------------------------+--------------------------+--------------------------+--------------------------+---------------------------+

    | :math:`P(C=M|A_i)\propto\prod\limits_{i=1}^4P(A_i|C=M)P(C=M)=\frac{6}{17}\times\frac{6}{7}\times\frac{6}{7}\times\frac{5}{7}\times\frac{4}{7}=0.1058`  (bigger) :math:`\implies`  mammal
    | :math:`P(C=N|A_i)\propto\prod\limits_{i=1}^4P(A_i|C=N)P(C=N)=\frac{11}{17}\times\frac{1}{6}\times\frac{1}{6}\times\frac{2}{3}\times\frac{2}{3}=0.0080` 
