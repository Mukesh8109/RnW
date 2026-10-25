# Deep Learning Practicals

## About this notebook

This notebook contains practical exercises on image processing and
Convolutional Neural Networks (CNNs). It uses the CIFAR-10 image dataset
and demonstrates preprocessing, convolution, pooling, model training,
data augmentation, and transfer learning.

## Requirements

Install the following Python libraries before running the notebook:

``` bash
pip install numpy matplotlib tensorflow
```

## How to run

1.  Open `PR_4_reorganized.ipynb` in Jupyter Notebook or VS Code.
2.  Make sure Python and the required libraries are installed.
3.  Run the cells from top to bottom.
4.  The CIFAR-10 dataset may download automatically the first time it is
    loaded.
5.  Check the printed results, plots, image displays, and model
    summaries after running the cells.

## Practicals and tasks

### Practical 1: CIFAR-10 Dataset and Image Preprocessing

-   1.  Load CIFAR-10 dataset
-   2.  CIFAR-10 class names
-   3.  Count frequency of each pixel value
-   4.  Normalize pixel values from 0-255 to 0-1
-   5.  Plot normalized pixel distribution
-   6.  One-hot encode the labels
-   7.  Check first 5 labels

### Practical 2: Convolution, Padding, Stride and Feature Maps

-   8.  Select the first CIFAR-10 image
-   9.  Display the original image and grayscale version
-   10. Define a 3x3 edge detection kernel
-   11. Get image dimensions
-   12. Visualize the manual convolution result
-   13. Import the required library
-   14. Create a Conv2D layer with SAME padding
-   15. Compare convolution output shapes
-   16. Add zero padding manually
-   17. Conv2D with stride = 1
-   18. Conv2D with stride = 2
-   19. Compare output shapes for different strides
-   20. Create a Conv2D layer with 16 filters
-   21. Select one image
-   22. Create 4x4 grid

### Practical 3: Pooling Layers and CNN Architectures

-   23. Add MaxPooling after A2 model
-   24. Visualize feature maps after max pooling
-   25. Apply average pooling and check the output shape
-   26. Flatten the pooled feature maps
-   27. lenet5 = keras.Sequential(\[
-   28. cnn = keras.Sequential(\[
-   29. Count the CNN model parameters

### Practical 4: CNN Training and Backpropagation

-   30. Use CNN created in A3
-   31. Compile the CNN model
-   32. Set up early stopping and learning-rate reduction
-   33. Train the CNN model
-   34. Plot training and validation curves
-   35. Print the final training results
-   36. Track when the learning rate is reduced
-   37. Train again while logging learning-rate changes

### Practical 5: Data Augmentation

-   38. Import the required library
-   39. model_aug = keras.models.clone_model(cnn)
-   40. Compare original and augmented training curves
-   41. augmentation = keras.Sequential(\[
-   42. Evaluate the augmentation models

### Practical 6: Transfer Learning

-   43. Import the required library
-   44. model_tl.compile(
-   45. base_model.trainable = True
-   46. Compare transfer-learning validation accuracy

## Main topics covered

-   Loading and exploring CIFAR-10
-   Pixel-value distribution and normalization
-   One-hot encoding image labels
-   Convolution, kernels, padding, and stride
-   Feature maps and pooling layers
-   CNN architectures including LeNet-5
-   Model parameters, training, and backpropagation
-   Early stopping and learning-rate reduction
-   Data augmentation
-   Transfer learning and fine-tuning
-   Comparing model training and validation results

## Note

Some results, such as training accuracy and validation accuracy, are
generated when the notebook is run and may vary depending on the
environment and training settings.
