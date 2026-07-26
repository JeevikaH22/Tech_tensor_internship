# Sales Prediction using Machine Learning

## Overview

This model predicts sales based on advertising expenditure on different media platforms. The model takes advertising budgets for TV, Radio, and Newspaper as input and estimates the expected sales.

The application is built using **Python**, **Scikit-learn**, and **Streamlit**.

---
## Dataset
Note- Dataset file is not provided due to large size.
link - https://www.kaggle.com/code/ashydv/sales-prediction-simple-linear-regression/input

---

## Features

- Predict sales using advertising budgets
- Simple and interactive Streamlit interface
- Machine learning model trained on advertising dataset
- Instant predictions

---

**Target Variable**

- Sales

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## Project Structure

```
Sales_Prediction/
│
├── app.py
├── sales.pkl
├── requirements.txt
├── README.md
└── Advertising.csv
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/JeevikaH22/Tech_tensor_internship.git
```

Move into the project directory:

```bash
cd Sales_Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your default web browser.


---

## Model Input

The application requires the following inputs:

- TV Advertising Budget
- Radio Advertising Budget
- Newspaper Advertising Budget

After entering the values, click **Predict Sales** to obtain the estimated sales.

---

## Model Performance

Evaluation Metrics:

- Mean Absolute Error (MAE): **1.27**
- Mean Squared Error (MSE): **2.91**
- R² Score: **0.91**

---

## Future Improvements

- Deploy the application
- Add data visualization
- Compare multiple regression algorithms

---

## Author

**Jeevika Hunnurkar**
 Aspiring Machine Learning Engineer and Data Science Enthusiast.
 Intern at Tech Tensor