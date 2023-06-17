## Project Report.
### Abstract
### Index page
### 1. Introduction, Motivation:
* Sensing: automation, need tools to absorb lots of data, data that is immune to noise -> Fourier Transform, not simple but performant and has sparsity. Sensing needed to figure how/ why things work the way they do, both at the macroscopic level and at the microscopic level.
* As such the amount of large high quality data increasing exponentially, the need to process this data better.
* Explain the applications of rotations in Data augmentation for example for Convoluted Neural Networks. How this has become more relevant with the higher avaiability of large amounts of data.
* Explain the applications of rotations in Data Visualization for example for PETSCAN, risonanze magnetiche... least amount of artifacts in the images can prevent wrong diagnosis, or show things that were not visible before.
* Explain what the goal of the project is: Rotate very high quality 2D images as accurately as possible.
* What is the contribution made in this project: how to create a filter, show implementation and study the numeric performance.
	
### 2 State of the art
#### 2.1 What is being used now to rotate images.
* Explain paper and rotation used in paper. Briefly, no math.
* Include pictures from Diego and connect with Data visualization. Explain what is used in machine learning for data augmentation, keras tensorflow, looks like they just use nn or bilinear interpolation after simple rotation.

### 3 Methodology
Overview, Big picture connect with article, exaplain why the use of Fourier transform.

#### 3.1 Frequency domain. Fourier	, go into detail.
##### 3.1.1 Fourier transform of 1D signal
* Show Fourier Transform and some curious properties depending on the n. Complex conjugate, even or odd number of n. First value always Real and not imag...

##### 3.1.2 Fourier Shift theorem
* Show the derivation of the Shift Theorem did with Diego.

##### 3.1.3 Problems that arise with shift. Wavenum, correct indexing of frequencies
* Explain frequency indexing and wavenum, complex conjugate, n being even or odd... 

##### 3.1.4 Creation of a filter
* Show the creation of the filter starting with the base function and M.
* Choice of M

#### 3.2 Convolution of filter and signal.
* Here do the specific convolution that Diego described
* Explain how convolving our original signal with the filter can shift by the fractional amount and also smooth the result. Explain why we are not shfiting by the int part as well -> It screws up our approach of using a convolution with a kernel of any size....

### 4 Implementation, design
* Generally explain in a couple of lines what I used. C, MakeFile,CMake, jupyter notebook, python. No libraries except built-in C libraries and numpy and matplotlib for python.
* Start with design: bottom-up approach, jupyter notebbok to learn Fourier, concentrated on 1D signals. (Explain that problem is well suited for bottom-up approach since if it works fo 1D, it works for 2D and then also 3D...)
* Design easily portable to other Devices, GPU...

#### 4.1 Libraries
##### 4.1.1 Numpy & Matplotlib for python
* Briefly explain why we used these libraries...

##### 4.1.2 MakeFile, Cmake
* Same thing...

##### 4.1.3 C built-in libraries
* Same thing...

#### 4.2 Creating a Filter in the Frequency Domain
* Explain the approach used in implementing the method for creating the filter.
* Shift theorem of the filter kernel for the fractional part of the shift.
* Normal Inverse Foruier Transform, not much cost.

* Difficulties in implementation
#### 4.3 Convolution of the filter

##### 4.3.1 Direct convolution
* Explain the algorithm used for convolution and the advantage of defining at compile time the size of the filter. 

##### 4.3.2 Convolution algorihtm
* Explain why the convolutions algorithm was implemented in this way instead of simple for loops, Godbolt, analysing the assembly code to see which kind of instructions were being used. 
* Difficulties in implementation

#### 4.4 Integer shift
##### 4.4.1 Integer shift
* Memcpy the convoluted signal by the Integer amount we want to shift.ATTENTION: Do not convolve the original signal with the filter if the shift is just an Integer.
* Difficulties in implementation of memcpy

### 5. Results
#### 5.1 Results with 1d signals
* Start with plot of original function.
* Start with Fixed M=1
* Shift signal by different fractional values and plot.
* Change M see what changes.
* Show how M should change based on amount of fractional shift.

#### 5.2 Results on 2D signals, i.e images using Diego's library.
* Plot some images and results using Diego's library and explain what happens with Diego's library.

#### 6 Conclusion
* Summary -> High level, what was the contribution.
* Limits of the work done/ it's impact
* Serial code

#### 6. Future works
* Make the code run with CUDA/ MPI.


#### Bibliography / References