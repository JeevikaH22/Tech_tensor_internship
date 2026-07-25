# 💳 Credit Card Fraud Detection using Machine Learning

A Machine Learning project that detects fraudulent credit card transactions using supervised learning algorithms. The project compares **Random Forest** and **XGBoost** classifiers and deploys the best-performing model using **Streamlit**.

---

## 📌 Project Overview

Credit card fraud is a significant challenge due to the highly imbalanced nature of transaction data. In this project, 2 machine learning models were trained and evaluated to accurately identify fraudulent transactions while minimizing false positives.

The project also evaluated **SMOTE (Synthetic Minority Over-sampling Technique)** to determine whether oversampling improves model performance.

---

##  Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Handles highly imbalanced dataset
- Model comparison:
  - Random Forest
  - XGBoost
- Evaluation using multiple metrics
- Streamlit web application for real-time prediction
- Comparison between Class Weighting and SMOTE

---

## 🛠️ Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Imbalanced-learn (SMOTE)
- Streamlit
- Pickle

---

##  Dataset

The dataset contains anonymized credit card transactions with the following features:

- Time
- V1 – V28 (PCA-transformed features)
- Amount
- Target:
  - 0 → Legitimate Transaction
  - 1 → Fraudulent Transaction

The dataset is highly imbalanced, making fraud detection a challenging classification problem.
Note- dataset.csv was not added to repository due to large size.

---

##  Models Used

### Random Forest

- Ensemble learning method
- Uses multiple decision trees
- Handles nonlinear relationships well

### XGBoost

- Gradient Boosting algorithm
- Optimized for speed and performance
- Supports imbalance handling using `scale_pos_weight`

---

# Model Performance (XGBoost)

| Metric   | Random Forest | XGBoost |
|----------|---------------|---------|
| Accuracy | 0.999471      |0.999595 |
| Precision| 0.985075      | 0.973684|
| Recall   | 0.694737      | 0.778947|
| F1 Score | 0.814815      | 0.865497|

**Final Selected Model:**  XGBoost

Reason:
- Highest Recall
- Highest F1 Score
- Excellent Precision
- Best overall fraud detection performance

---

#  SMOTE Experiment

Since the dataset was highly imbalanced, **SMOTE (Synthetic Minority Over-sampling Technique)** was evaluated to determine whether generating synthetic fraud samples would improve model performance.
---

## Results

After applying SMOTE:

- Random Forest showed no significant improvement.
- XGBoost experienced a noticeable decrease in Precision and F1-score while Recall remained unchanged.

### Observation

SMOTE did **not** outperform the original class-weighting approach.

Instead, using:

- `class_weight='balanced'` for Random Forest
- `scale_pos_weight` for XGBoost

produced better overall performance on the original dataset.

Therefore, the final deployed model was trained **without SMOTE**.

This experiment demonstrates that oversampling techniques should be validated rather than assumed to improve performance.

---

### Conclusion

The original class-weighting strategy produced superior results than smote+Xgboost and random forest; hence was selected for the final model.

---

#  Streamlit Application

The application allows users to enter transaction details and predicts whether the transaction is:

-  Legitimate Transaction
-  Fraud Transaction

---

## ▶️ Run Locally

Clone the repository

```bash
git clone https://github.com/JeevikaH22/Tech_tensor_internship.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Credit_Card_Fraud_Detection/
│
├── app.py
├── credit_card_fraud.pkl
├── credit_card_model.ipynb
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## 👩‍💻 Author

**Jeevika Hunnurkar**

Data Science & Machine Learning Enthusiast
Tech Tensor virtual intern (july 2026-august 2026)
