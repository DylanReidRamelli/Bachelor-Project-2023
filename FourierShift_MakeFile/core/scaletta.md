## Project mini mind-map.
Everything is just in general. Obviously I will add all the necessary parts in the correct places to explain as well as I can what is going on. Mostly relying on images and some math here and there. 
Maybe some code in the part of the convolution algorithm bu I don't know.

### Introduction, Motivation:
	- Explain the state of Big Data, amount increasing exponentially, the need to process this data...
	- Applications in Data Augmentation for Convoluted Neural Networks, Data Visualization for multi-model imaging...
	- Goal of the project, based on article "...".
### State of the art
	- Explain what is being used now to rotate images accurately.
	- Include pictures from Diego.

### Methodology
	- Explain the method of rotation that was used in article. Three matrices part. Three translations.
	- Fourier Transform and Fourier Shift, why we chose to shift in Frequency space...
	- Explain frequency indexing and wavenum, complex conjugate, n being even or odd... 


### Implementation, design
	- Start with design: bottom-up approach, jupyter notebbok to learn Fourier, concentrated on 1D signals. Explain that problem is well suited for bottom-up approach since if it works fo 1D, it works for 2D and then also 3D...
	- Explain our approach
		- Create filter from a cos function defined in Frequency Domain
		- Shift theorem of the filter kernel for the fractional part of the shift.
		- Convolve the filter in time domain with original signal, explain the algorithm used for convolution and the advantage of defining at compile time the size of the filter.
		- Memcpy the convoluted signal by the Integer amount we want to shift
		- ATTENTION: Do not convolve the original signal with the filter if the shift is just an Integer.

### Results on 1D signals
### Results on 2D signals, i.2 images using Diego's library.

### Future works
	- Probably continue the project and implement it with CUDA if there wasn't time to finish.