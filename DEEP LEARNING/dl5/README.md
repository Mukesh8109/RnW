# PR 5: Sentiment Analysis with RNN, LSTM and GRU

## Project overview
This practical builds sentiment classifiers for movie reviews using an order-blind ANN baseline, SimpleRNN, LSTM, and GRU. It covers text cleaning, tokenisation, padding, recurrent forward propagation, gradient flow, evaluation, and prediction on custom sentences.

## Dataset
Download **IMDB Dataset.csv** from the [Kaggle IMDB 50K Movie Reviews dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews). Place the CSV in the same folder as `DL_PR5.ipynb`. The file should contain `review` and `sentiment` columns.

Do not use `keras.datasets.imdb` for this practical because the assignment requires cleaning and tokenising the original text.

## Notebook
Open `DL_PR5.ipynb` in Jupyter Notebook or VS Code and run the cells from top to bottom. Each practical step is placed in a separate cell. Training all experiments may take a long time, especially on CPU.

## Preprocessing
- Remove duplicate reviews before splitting to reduce data leakage.
- Convert text to lowercase, remove HTML tags and punctuation other than apostrophes, and collapse extra spaces.
- Keep stop-words because negation such as “not good” changes sentiment.
- Split data into training and test sets with `test_size=0.2`, `random_state=42`, and stratification.
- Fit the tokenizer on training text only, with a 10,000-word vocabulary and an out-of-vocabulary token.
- Pad and truncate sequences before training.

## Models
- **ANN baseline:** Embedding, Flatten, Dense layers. It does not explicitly process word order.
- **SimpleRNN:** Reuses the same recurrent weights across time, but may struggle with long-range dependencies because of vanishing gradients.
- **LSTM:** Uses a cell state and forget, input, and output gates to preserve useful information over longer sequences.
- **GRU:** Uses update and reset gates and does not have a separate cell state; it often has fewer parameters than LSTM.

## Evaluation
The notebook calculates test accuracy, precision, recall, F1-score, ROC-AUC, classification reports, and confusion matrices. It also plots training curves, gradient norms, ROC curves, and review-length comparisons. Actual metrics depend on running the notebook with the dataset and installed packages; no results are claimed in advance.

## Dataset citation
Maas, A. L., Daly, R. E., Pham, P. T., Huang, D., Ng, A. Y., & Potts, C. (2011). *Learning Word Vectors for Sentiment Analysis*. Proceedings of ACL-HLT 2011. Stanford Large Movie Review Dataset.

## Tools used
Python, Jupyter Notebook, pandas, NumPy, Matplotlib, Seaborn, scikit-learn, TensorFlow/Keras.

## Video
Add your project explanation video link here after uploading it.

## Files
- `DL_PR5.ipynb` — notebook with separate cells for each practical step.
- `IMDB Dataset.csv` — download separately from Kaggle.
- `requirements.txt` — Python packages needed.
- `plots/` — generated plots and result CSV created while running the notebook.
