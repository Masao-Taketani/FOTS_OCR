# FOTS: Fast Oriented Text Spotting with a Unified Network

This repo is python3 version of https://github.com/yu20103983/FOTS.

## Dataset
Use one of the ICDAR text detection and recognition datasets.
For this project I will plan to use [ICDAR 2019 Robust Reading Challenge on Multi-lingual scene text detection and recognition](https://rrc.cvc.uab.es/?ch=15&com=downloads)

## Train

`python multigpu_train.py [gpu_list]`

You should give the path to the dataset labeled in ICDAR format in file 'FOTS/dataset/dataReader.py'

## References
Paper: [FOTS: Fast Oriented Text Spotting with a Unified Network](https://arxiv.org/pdf/1801.01671.pdf)<br>
Codes: https://github.com/yu20103983/FOTS<br>
