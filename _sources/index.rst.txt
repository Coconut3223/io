.. cocobook documentation master file, created by
   sphinx-quickstart on Wed May 22 21:57:57 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to cocobook's documentation!
====================================


.. toctree::
   :caption: Content
   :maxdepth: 2

   AI <AI/index>
   ML <AI/ML/index>
   DL <AI/DL/index>
   CV <CV/index>
   NLP <NLP/index>
   python <python/index>
   SQL <SQL/index>
   utils <utils/index>
   frontend <frontend/index>
   

.. mermaid:: 

   flowchart LR

   B1["`faster_whisper_V3 
   & 100ms`"]
   B2["`faster_whisper_V3 
   & 1000ms`"]
   B3["`faster_whisper_V3 
   & 100ms`"]
   C{"`check 
   VAD & ASR`"}
   D{"`check 
   ASR`"}
   F["`whisper-small-Cantonese`"]
   G("`audio`")
   H("`audio segment 
   & its ASR`")
   I("`truth`")
   J1("`validated audio segment`")
   J2("`validated audio segment`")
   K("`ASR`")

   G-->B1-->H 
   G -->B2-->H
   H-.->C
   C -. pass .-> J1
   J2 --> B3 --> K
   J2 --> F --> K
   K -.-> D -. pass .-> I



