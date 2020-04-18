# FOTS: Fast Oriented Text Spotting with a Unified Network

This repo is python3 version of https://github.com/yu20103983/FOTS.

## Dataset
~~1. Get [pre-trained ResNet-50](https://onedrive.live.com/?authkey=%21AAFW2-FVoxeVRck&id=4006CBB8476FF777%2117887&cid=4006CBB8476FF777).~~<br>
~~2. Convert the caffe model into TF checkpoint by convert.py from [tensorflow-resnet
 by ry](https://github.com/ry/tensorflow-resnet).~~<br>
~~3. Pretraining the whole net by [Synth800k dataset](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) for 10 epochs.~~<br>

1. Download a [pre-trained model](https://github.com/Pay20Y/FOTS_TF/releases/download/v2/SynthText_6_epochs.tar) with [Synth800k dataset](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) which can be originally found at [Pay20Y/FOTS_TF](https://github.com/Pay20Y/FOTS_TF/tree/dev).
2. 

## Train

`python multigpu_train.py [gpu_list]`

You should give the path to the dataset labeled in ICDAR format in file 'FOTS/dataset/dataReader.py'

## References
- Paper
  - [FOTS: Fast Oriented Text Spotting with a Unified Network](https://arxiv.org/pdf/1801.01671.pdf)<br>
  - [Feature Pyramid Networks for Object Detection](https://arxiv.org/pdf/1612.03144.pdf)<br>
- Repos
  - https://github.com/yu20103983/FOTS<br>
  - https://github.com/Pay20Y/FOTS_TF/tree/dev<br>
  - https://github.com/kaiminghe/deep-residual-networks<br>
  - https://github.com/ry/tensorflow-resnet<br>
