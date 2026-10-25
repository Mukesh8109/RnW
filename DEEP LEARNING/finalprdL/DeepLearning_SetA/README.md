# Deep Learning Practical Exam – Set A

This repository contains implementations and tasks corresponding to the **Deep Learning Practical Exam (Set A)**. It covers core deep learning concepts including Artificial Neural Networks (ANNs), computer vision preprocessing with OpenCV, Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Transformer-based NLP pipelines.

## 📋 Project Structure & Steps

The project is structured into six key evaluation phases:

### 1. Artificial Neural Network (ANN) — Diabetes Classification
* **Data Preparation:** Loads the Pima Indians Diabetes dataset, handles zero-values as missing data via median imputation, splits data with stratification, and applies `StandardScaler`.
* **Architecture:** A Feedforward Neural Network with an Input layer, two Dense hidden layers (`16` and `8` nodes with ReLU), and a single-node Sigmoid output layer.
* **Evaluation:** Trained with Binary Crossentropy and the Adam optimizer over 50 epochs. Generates training/validation curves and reports accuracy, precision, recall, F1-score, and a confusion matrix.
* **Artifact:** Saved as `ann_diabetes_model.h5`.

### 2. Computer Vision — OpenCV Image Preprocessing
* **Operations:** Preprocesses sample images extracted from the CIFAR-10 dataset.
* **Pipeline:** Resizes images to `128x128`, converts them to grayscale, applies a Gaussian Blur, performs Canny edge detection, extracts contours, and highlights the largest bounding region.
* **Grid Display:** Outputs a comprehensive 5x5 visual grid tracking every transformation stage.

### 3. Convolutional Neural Network (CNN) — CIFAR-10 Classification
* **Data Prep:** Evaluates 20,000 training and 4,000 test images from the CIFAR-10 dataset scaled between `0` and `1`.
* **Architecture:** Standard feature extraction using sequential `Conv2D` and `MaxPooling2D` layers, flattened into a `Dense` classifier layer with a 10-way `Softmax` output.
* **Evaluation:** Assesses multiclass metrics with detailed classification reports and builds visual true vs. predicted grids.
* **Artifact:** Saved as `cnn_cifar10_model.h5`.

### 4. Recurrent Neural Network (RNN) — Time Series Forecasting
* **Data Prep:** Uses the Monthly Airline Passengers dataset scaled via `MinMaxScaler` using a 12-month look-back window configuration.
* **Architecture:** Single `SimpleRNN` layer (50 units, Tanh activation) mapped to a linear continuous prediction node.
* **Evaluation:** Measures regression performance using Test Root Mean Squared Error (RMSE) accompanied by historical vs. predicted sequence plots.
* **Artifact:** Saved as `rnn_airline_model.h5`.

### 5. Transformers — Sentiment Inference Pipeline
* **Model:** Implements a pre-trained `distilbert-base-uncased-finetuned-sst-2-english` Hugging Face pipeline.
* **Tasks:** Conducts evaluation on 25 custom movie sentences divided into explicit (Positive/Negative) and neutral/ambiguous phrases. Runs inference tracking probability metrics and custom horizontal validation charts.

### 6. Results Summary & Dashboard
Consolidates training tracking variables into a structured final report dataframe monitoring metrics, dataset sizes, and runtime.

---

## 🛠️ Installation & Setup

Ensure you have Python 3 installed. Clone this repository and configure dependencies:

```bash
pip install tensorflow opencv-python transformers pandas numpy matplotlib scikit-learn
```

## 🚀 How to Run
Execute the Jupyter Notebook environment to sequentially run each cell module:
```bash
jupyter notebook
```

---
*Disclaimer: This repository is intended for academic validation and practical exam recording.*
