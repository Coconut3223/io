Scrapy
####################




二进制数据
********************

.. code-block:: py
    :caption: media

    import requests

    res = requests.get('https://www.gaoyuanqi.cn/images/avatar.png')
    with open('avatar.png', 'wb') as f:
        f.write(res.content)

.. code-block:: py
    :caption: str
        str = bytes.decode('UTF-8')


.. code-block:: py
    :caption: 写 & 读

    f = open(file, 'rb')
    f.read()
    f = open(file, 'wb')
    f.write()
    
Audio
**********

m3u8
==========

| M3U8视频格式是一种基于 **HTTP Live Streaming, HLS** 协议的视频文件格式。
| M3U8视频格式将整个视频分成 **多个小片段进行传输**，这些小片段可以根据网络情况自动调节其质量和大小。这种方式使得M3U8视频格式非常适合在网络环境不稳定或带宽不足的情况下播放视频。

.. code-block:: py

    import m3u8_To_MP4

    m3u8_To_MP4.multithread_download(video_url, mp4_file_dir='./videos/', mp4_file_name=name)

`【入门指南】M3U8格式是什么：一步步了解视频流媒体 <https://cloud.tencent.com/developer/article/2302011>`_

