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

# Code 
## conv2d()
IntelliJ
tensorflow/python/ops/gen_nn_ops.py, which is a registered operation in [tensorflow/core/ops/nn_ops.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/ops/nn_ops.cc)
```
def conv2d(input, filter, strides, padding, use_cudnn_on_gpu=None,
           data_format=None, name=None):
  r"""Computes a 2-D convolution given 4-D `input` and `filter` tensors.

  Given an input tensor of shape `[batch, in_height, in_width, in_channels]`
  and a filter / kernel tensor of shape
  `[filter_height, filter_width, in_channels, out_channels]`, this op
  performs the following:

  1. Flattens the filter to a 2-D matrix with shape
     `[filter_height * filter_width * in_channels, output_channels]`.
  2. Extracts image patches from the input tensor to form a *virtual*
     tensor of shape `[batch, out_height, out_width,
     filter_height * filter_width * in_channels]`.
  3. For each patch, right-multiplies the filter matrix and the image patch
     vector.

  In detail, with the default NHWC format,

      output[b, i, j, k] =
          sum_{di, dj, q} input[b, strides[1] * i + di, strides[2] * j + dj, q] *
                          filter[di, dj, q, k]

  Must have `strides[0] = strides[3] = 1`.  For the most common case of the same
  horizontal and vertices strides, `strides = [1, stride, stride, 1]`.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `float32`.
      A 4-D tensor. The dimension order is interpreted according to the value
      of `data_format`, see below for details.
    filter: A `Tensor`. Must have the same type as `input`.
      A 4-D tensor of shape
      `[filter_height, filter_width, in_channels, out_channels]`
    strides: A list of `ints`.
      1-D tensor of length 4.  The stride of the sliding window for each
      dimension of `input`. The dimension order is determined by the value of
        `data_format`, see below for details.
    padding: A `string` from: `"SAME", "VALID"`.
      The type of padding algorithm to use.
    use_cudnn_on_gpu: An optional `bool`. Defaults to `True`.
    data_format: An optional `string` from: `"NHWC", "NCHW"`. Defaults to `"NHWC"`.
      Specify the data format of the input and output data. With the
      default format "NHWC", the data is stored in the order of:
          [batch, height, width, channels].
      Alternatively, the format could be "NCHW", the data storage order of:
          [batch, channels, height, width].
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
    A 4-D tensor. The dimension order is determined by the value of
    `data_format`, see below for details.
  """
  result = _op_def_lib.apply_op("Conv2D", input=input, filter=filter,
                                strides=strides, padding=padding,
                                use_cudnn_on_gpu=use_cudnn_on_gpu,
                                data_format=data_format, name=name)
  return result
```

Code search:  [tensorflow/tensorflow/python/layers/convolutional.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/layers/convolutional.py)

