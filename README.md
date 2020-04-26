# FOTS: Fast Oriented Text Spotting with a Unified Network

This repo is python3 version of https://github.com/yu20103983/FOTS.

## Train from Scratch
1. Get [pre-trained ResNet-50](http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz). from [TensorFlow-Slim image classification model library](https://github.com/tensorflow/models/tree/master/research/slim) page.<br>
2. Pretraining the whole net by [Synth800k dataset](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) for 10 epochs.<br>

~~1. Download a [pre-trained model](https://github.com/Pay20Y/FOTS_TF/releases/download/v2/SynthText_6_epochs.tar) with [Synth800k dataset](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) which can be originally found at [Pay20Y/FOTS_TF](https://github.com/Pay20Y/FOTS_TF/tree/dev).
2.~~

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
  - https://github.com/Parquery/lanms<br>
