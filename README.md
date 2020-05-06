# FOTS: Fast Oriented Text Spotting with a Unified Network

**I am still working on this repo. So more codes and detailed instructions are coming soon!**

## Train from Scratch
### Pretrain with SynthText
1. Download [pre-trained ResNet-50](http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz) from [TensorFlow-Slim image classification model library](https://github.com/tensorflow/models/tree/master/research/slim) page and place it at the 'ckpt/resnet_v1_50' dir.<br>
```
cd ckpt/resnet_v1_50
wget http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz
tar -zxvf resnet_v1_50_2016_08_28.tar.gz
rm resnet_v1_50_2016_08_28.tar.gz
```
2. Download [Synth800k dataset](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) to pre-train the whole net.(The dataset is only available or non-commercial research and educational purposes)<br>

3. Preprocess the SynthText data.<br>
``` 
python FOTS/synthText2icdar.py
```

4. Train with SynthText for 10 epochs.<br>
```
sh train_synthText_10eps.sh
```

### Finetune with ICDAR 2015, ICDAR 2017 MLT or ICDAR 2013
- ICDAR 2015
  1. Train the pre-trained model with 9,000 images from ICDAR 2017 MLT training and validation datasets.
  2. Train the model with 1,000 images from ICDAR 2015 training dataset and 229 images from ICDAR 2013 training datasets.
  
- ICDAR 2017 MLT(text detection task only)
  1. Train the pre-trained model with 9,000 images from ICDAR 2017 MLT training and validation datasets.
  
- ICDAR 2013(horizontal text only)
  1. Train the pre-trained model with 9,000 images from ICDAR 2017 MLT training and validation datasets.
  2. Train the model with 229 images from ICDAR 2013 training datasets.

~~1. Download a [pre-trained model](https://github.com/Pay20Y/FOTS_TF/releases/download/v2/SynthText_6_epochs.tar) with [Synth800k dataset](https://www.robots.ox.ac.uk/~vgg/data/scenetext/) which can be originally found at [Pay20Y/FOTS_TF](https://github.com/Pay20Y/FOTS_TF/tree/dev).
2.~~


## References
- Paper
  - [FOTS: Fast Oriented Text Spotting with a Unified Network](https://arxiv.org/pdf/1801.01671.pdf)<br>
  - [Feature Pyramid Networks for Object Detection](https://arxiv.org/pdf/1612.03144.pdf)<br>
- Repos
  - https://github.com/yu20103983/FOTS<br>
  - https://github.com/Pay20Y/FOTS_TF/tree/dev<br>
  - https://github.com/tensorflow/models/tree/master/research/slim<br>
  - https://github.com/kaiminghe/deep-residual-networks<br>
  - https://github.com/Parquery/lanms<br>
