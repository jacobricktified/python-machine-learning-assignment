
# Python Machine Learning Assignment

**Name:** Jacob Gichira Mbuco

## Project Title
Supervised and Unsupervised Machine Learning Using Python

## 1. Supervised Machine Learning: Student Exam Score Prediction

This project uses Linear Regression to predict a student's examination
score based on the number of hours studied.

The dataset contains ten examples of study hours and their corresponding
exam scores. The model is trained using `fit()` and makes predictions
using `predict()`.

The program accepts study hours from the user and displays the predicted
exam score to two decimal places. Matplotlib is used to plot the actual
scores and the regression line.

## 2. Unsupervised Machine Learning: Customer Segmentation

This project uses K-Means clustering to group supermarket customers
according to monthly spending and monthly shopping visits.

The dataset contains ten customers. StandardScaler is used to scale
the features before training the K-Means model with three clusters.

The program displays each customer's cluster, the number of customers
in each cluster, and a scatter plot of the resulting groups.

## 3. Requirements

- Python 3
- scikit-learn
- Matplotlib

## 4. Installation and Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-machine-learning-assignment.git
cd python-machine-learning-assignment
```

### Step 2: Create a virtual environment

Ubuntu/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the supervised program

```bash
python supervised_ml.py
```

### Step 5: Run the unsupervised program

```bash
python unsupervised_ml.py
```

## 5. Theory Questions and Answers

### 1. What is supervised machine learning?

Supervised machine learning is a type of machine learning in which
a model learns from labelled data containing inputs and their known
correct outputs. It uses these examples to predict outputs for new data.

### 2. What is unsupervised machine learning?

Unsupervised machine learning is a type of machine learning in which
a model works with data that has no predefined target labels. It
discovers patterns, structures, or groups within the data.

### 3. Explain the difference between supervised and unsupervised learning.

Supervised learning uses labelled data and learns to predict known
targets. Unsupervised learning uses data without target labels and
discovers patterns or groups automatically.

### 4. Why is Linear Regression considered supervised learning?

Linear Regression is supervised because it learns the relationship
between input features and known target values. In this project,
the inputs are study hours and the target values are exam scores.

### 5. Why is K-Means considered unsupervised learning?

K-Means is unsupervised because it groups data according to similarities
without needing predefined customer categories or target labels.

### 6. What is the difference between fit() and predict()?

The `fit()` method trains a model using the supplied data. The
`predict()` method uses the trained model to estimate outputs or assign
clusters to data points.

For K-Means, `fit()` discovers cluster centres, while `predict()`
assigns observations to the nearest cluster centre.

### 7. Give two real-world applications of supervised learning
and two of unsupervised learning.

Supervised learning:
- Predicting house prices from labelled property data.
- Detecting spam emails using labelled spam and non-spam examples.

Unsupervised learning:
- Grouping supermarket customers according to shopping behaviour.
- Grouping news articles according to similarities in their content.

## 6. Conclusion

This assignment demonstrates how Linear Regression can predict
numerical values and how K-Means can discover groups in a dataset.
Both programs use Python and scikit-learn, with Matplotlib providing
visual representations of their results.
