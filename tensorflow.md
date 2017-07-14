# Install
https://www.tensorflow.org/install/install_linux

## Install on Ubuntu 16.04: no-GPU, python27
```
sudo apt-get install python-pip python-dev
sudo pip install pip --upgrade (optional)
sudo pip install tensorflow 
``` 
Location: /usr/local/lib/python2.7/dist-packages/tensorflow

# Run examples

## MNIST softmax
```
~/$ gitclone https://github.com/tensorflow/tensorflow.git tensorflow-master
~/$ cd tensorflow-master/tensorflow/examples/tutorials/mnist
~/tensorflow-master/tensorflow/examples/tutorials/mnist$ python mnist_softmax.py
Successfully downloaded train-images-idx3-ubyte.gz 9912422 bytes.
Extracting /tmp/tensorflow/mnist/input_data/train-images-idx3-ubyte.gz
Successfully downloaded train-labels-idx1-ubyte.gz 28881 bytes.
Extracting /tmp/tensorflow/mnist/input_data/train-labels-idx1-ubyte.gz
Successfully downloaded t10k-images-idx3-ubyte.gz 1648877 bytes.
Extracting /tmp/tensorflow/mnist/input_data/t10k-images-idx3-ubyte.gz
Successfully downloaded t10k-labels-idx1-ubyte.gz 4542 bytes.
Extracting /tmp/tensorflow/mnist/input_data/t10k-labels-idx1-ubyte.gz
2017-07-10 18:11:19.912267: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-10 18:11:19.963886: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-10 18:11:19.963902: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-10 18:11:19.963907: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-10 18:11:19.963912: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
0.9186
```

## MNIST with tensor board
```
~/$ gitclone https://github.com/tensorflow/tensorflow.git tensorflow-master
~/$ cd tensorflow-master/tensorflow/examples/tutorials/mnist
~/tensorflow-master/tensorflow/examples/tutorials/mnist$ python mnist_with_summaries.py
Extracting /tmp/tensorflow/mnist/input_data/train-images-idx3-ubyte.gz
Extracting /tmp/tensorflow/mnist/input_data/train-labels-idx1-ubyte.gz
Extracting /tmp/tensorflow/mnist/input_data/t10k-images-idx3-ubyte.gz
Extracting /tmp/tensorflow/mnist/input_data/t10k-labels-idx1-ubyte.gz
2017-07-10 18:24:34.164170: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-10 18:24:34.277910: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-10 18:24:34.277931: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-10 18:24:34.277936: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-10 18:24:34.277941: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
Accuracy at step 0: 0.0773
Accuracy at step 10: 0.6496
Accuracy at step 20: 0.7931
Accuracy at step 30: 0.8618
Accuracy at step 40: 0.8801
Accuracy at step 50: 0.8878
Accuracy at step 60: 0.896
Accuracy at step 70: 0.9006
Accuracy at step 80: 0.903
Accuracy at step 90: 0.9055
Adding run metadata for 99
Accuracy at step 100: 0.9126
Accuracy at step 110: 0.9146
Accuracy at step 120: 0.9187
Accuracy at step 130: 0.9199
Accuracy at step 140: 0.9209
Accuracy at step 150: 0.9216
Accuracy at step 160: 0.9296
Accuracy at step 170: 0.9301
Accuracy at step 180: 0.9283
Accuracy at step 190: 0.9294
Adding run metadata for 199
Accuracy at step 200: 0.9347
Accuracy at step 210: 0.9346
Accuracy at step 220: 0.9308
Accuracy at step 230: 0.9349
Accuracy at step 240: 0.9325
Accuracy at step 250: 0.936
Accuracy at step 260: 0.9384
Accuracy at step 270: 0.9373
Accuracy at step 280: 0.9391
Accuracy at step 290: 0.9411
Adding run metadata for 299
Accuracy at step 300: 0.9431
Accuracy at step 310: 0.9384
Accuracy at step 320: 0.9427
Accuracy at step 330: 0.9438
Accuracy at step 340: 0.9439
......
......
Accuracy at step 890: 0.9659
Adding run metadata for 899
Accuracy at step 900: 0.9661
Accuracy at step 910: 0.969
Accuracy at step 920: 0.9684
Accuracy at step 930: 0.967
Accuracy at step 940: 0.9685
Accuracy at step 950: 0.9684
Accuracy at step 960: 0.9684
Accuracy at step 970: 0.9667
Accuracy at step 980: 0.968
Accuracy at step 990: 0.9664
Adding run metadata for 999
~/tensorflow-master/tensorflow/examples/tutorials/mnist$ tensorboard --logdir=/tmp/tensorflow/mnist/logs/mnist_with_summaries/train
Starting TensorBoard 54 at http://localhost(or hostname):6006
(Press CTRL+C to quit)
```

# tensorboard

https://github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/tensorboard/README.md

https://www.tensorflow.org/get_started/summaries_and_tensorboard

