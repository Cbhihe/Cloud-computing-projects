## Lab 5: Under the hood of Cloud advanced analytics services

In previous lab we suggested an "optional" task that uses the [Cloud Vision API](https://cloud.google.com/vision/) from Google as an example of Advanced Analytics as a Service in the Cloud. The platform to support this type of services require high performance computing resources as GPU accelerators and a powerful software, TensorFlow, as their advanced analytics engine. 

Let’s take a closer look to hardware and software requirements, in order to understand how to satisfy them. Using the Barcelona Supercomputing Center resources, we have access to a GPU cluster () and we will review the main characteristics of [TensorFlow](https://www.tensorflow.org), the most popular framework to date, to build AI models.

### Lab Tasks:

#### Task 1: Install TensorFlow in a Python virtual environment on your local host

- Follow the installation instructions from https://www.tensorflow.org/install/

- Clone or download this remote repo: 
https://github.com/jorditorresBCN/FirstContactWithTensorFlow-2nEdition

- Validate your TensorFlow installation (assuming that the VE directory is ~/Lab5 ), then issue the following comds in terminal:

```
$ git clone https://github.com/jorditorresBCN/FirstContactWithTensorFlow-2ndEdition.git
$ cd FirstContactWithTensorFlow-2ndEdition/
$ python ValidateYourInstallation.py
```

If the system outputs the following “Hello, TensorFlow!”, you are ready to begin writing TensorFlow programs!

#### Tasks 2: Follow the following tutorials:

- TF1: TensorFlow basics
- TF2: Linear Regression in TensorFlow
- TF3: Clustering in TensorFlow
- TF3.1: Single Layer Neural Network in TensorFlow
- TF3.2: Multi-layer Neural Network in TensorFlow (optional)
- TF4: Multiple GPUs and TensorFlow (optional)
