# 🍽️ Zomato Restaurant Rating Prediction

A Machine Learning project that predicts the expected rating of a restaurant based on restaurant characteristics such as location, cuisines, votes, online ordering, table booking, and approximate cost for two people.

The project includes **Exploratory Data Analysis, Data Preprocessing, Feature Engineering, Machine Learning Model Comparison, Hyperparameter Tuning, and a Streamlit Web Application**.

---

## 📌 Project Overview

Restaurant ratings are influenced by several factors including customer votes, restaurant type, cuisines, location, online ordering facilities, table booking availability, and pricing.

The objective of this project is to build a Machine Learning regression model that can estimate a restaurant's rating based on these features.

### 🎯 Objective

> Predict a restaurant's rating on a scale of **0 to 5** using Machine Learning.

---

## 📊 Dataset

The original dataset contains:

* **51,717 rows**
* **17 columns**

The dataset contains information about restaurants including:

* Restaurant name
* Location
* Online ordering
* Table booking
* Rating
* Votes
* Restaurant type
* Cuisines
* Approximate cost
* City/listing information

After data cleaning and removing rows without usable ratings, the final modeling dataset contains approximately **41,585 records**.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Removed unnecessary columns.
2. Handled missing rating values.
3. Extracted numerical ratings from the `rate` column.
4. Converted categorical information into machine-learning-friendly features.
5. Separated input features and target variable.
6. Split the dataset into training and testing sets.

### Columns Removed

The following columns were removed because they were not required for the prediction task:

* `url`
* `address`
* `phone`
* `rate`
* `dish_liked`
* `reviews_list`
* `menu_item`
* `name`

---

## 🔍 Features Used

The final model uses the following features:

### Numerical Features

* `online_order`
* `book_table`
* `votes`
* `approx_costfor_two_people`

### Categorical Features

* `location`
* `rest_type`
* `cuisines`
* `listed_intype`
* `listed_incity`

### Target

* `rating`

---

## 📈 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand:

* Rating distribution
* Restaurant locations
* Restaurant types
* Cuisine popularity
* Votes distribution
* Approximate cost distribution
* Relationship between votes and ratings
* Online ordering availability
* Table booking availability

The analysis helped identify patterns and understand the important characteristics of restaurants.

---

## ⚙️ Machine Learning Workflow

The project follows this workflow:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Selection
     ↓
Train-Test Split
     ↓
Data Preprocessing
     ↓
One-Hot Encoding
     ↓
Model Training
     ↓
Model Comparison
     ↓
Hyperparameter Tuning
     ↓
Final Random Forest Model
     ↓
Streamlit Application
```

---

## 🤖 Models Tested

Three regression models were evaluated:

### 1. Linear Regression

Performance:

* MAE: **0.2053**
* RMSE: **0.2872**
* R²: **0.5714**

---

### 2. Random Forest Regression

Performance:

* MAE: **0.1804**
* RMSE: **0.2619**
* R²: **0.6434**

Random Forest performed better than Linear Regression.

---

### 3. Gradient Boosting Regression

Performance:

* MAE: **0.2196**
* RMSE: **0.3032**
* R²: **0.5222**

---

## 🏆 Model Comparison

| Model             |    MAE |   RMSE |     R² |
| ----------------- | -----: | -----: | -----: |
| Linear Regression | 0.2053 | 0.2872 | 0.5714 |
| Random Forest     | 0.1804 | 0.2619 | 0.6434 |
| Gradient Boosting | 0.2196 | 0.3032 | 0.5222 |

Based on the evaluation results, **Random Forest Regression** was selected as the final model.

---

## 🎯 Hyperparameter Tuning

RandomizedSearchCV was used to improve the Random Forest model.

### Search Configuration

* Cross-validation: **5-fold**
* Number of iterations: **20**
* Scoring metric: **R²**
* Random state: **42**
* Parallel processing: `n_jobs=-1`

### Best Parameters

```text
n_estimators = 200
max_depth = None
min_samples_split = 2
min_samples_leaf = 1
max_features = log2
```

---

## 🏅 Final Model Performance

After hyperparameter tuning:

| Metric   |      Score |
| -------- | ---------: |
| MAE      | **0.1603** |
| RMSE     | **0.2233** |
| R² Score | **0.7409** |

### Final Model

**Tuned Random Forest Regression**

The model achieved an R² score of approximately **0.741** on the test dataset.

---

## 🔄 Preprocessing Pipeline

The final model is stored as a complete Scikit-learn Pipeline.

```text
Input Data
     ↓
ColumnTransformer
     ↓
Categorical Features
     ↓
One-Hot Encoding
     ↓
Numerical Features
     ↓
Random Forest Regression
     ↓
Predicted Rating
```

The use of a complete Pipeline ensures that the same preprocessing used during training is applied during prediction.

---

## 🌐 Streamlit Web Application

A Streamlit web application was developed to allow users to enter restaurant information and receive a predicted rating.

### User Inputs

The application accepts:

* Online Order Availability
* Table Booking Availability
* Location
* Restaurant Type
* Cuisines
* Listed In Type
* Listed In City
* Number of Votes
* Approximate Cost for Two

### Output

The application displays:

* Predicted rating
* Star-based rating
* Rating category
* Restaurant statistics
* Model information
* Model performance

---

## 🖥️ Application Architecture

```text
User
  ↓
Streamlit UI
  ↓
Restaurant Input
  ↓
Input Validation
  ↓
Preprocessing Pipeline
  ↓
Random Forest Model
  ↓
Predicted Rating
  ↓
Streamlit Result
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Random Forest
* Linear Regression
* Gradient Boosting
* RandomizedSearchCV

### Deployment / Web Application

* Streamlit

### Model Serialization

* Joblib

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📁 Project Structure

```text
ZOMATO_RATING_PREDICTION/
│
├── app.py
├── zomato_rating_model.pkl
├── file(3).ipynb
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    ├── home.png
    └── prediction.png
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Ganu180/ZOMATO_RATING_PREDICTION.git
```

### 2. Open the Project

```bash
cd ZOMATO_RATING_PREDICTION
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Required Libraries

Example `requirements.txt`:

```text
streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
```

---

## 💡 Example Prediction

Example input:

```text
Online Order       : Yes
Table Booking      : Yes
Location           : Banashankari
Restaurant Type    : Casual Dining
Cuisines           : North Indian, Chinese
Listed In Type     : Delivery
Listed In City     : Banashankari
Votes              : 500
Cost for Two       : ₹800
```

The trained model generates an estimated restaurant rating between **0 and 5**.

---

## 📌 Key Learnings

Through this project, I worked with:

* Data cleaning
* Missing value handling
* Exploratory Data Analysis
* Feature selection
* Categorical encoding
* Train-test splitting
* Regression algorithms
* Random Forest
* Hyperparameter tuning
* Model evaluation
* Scikit-learn Pipelines
* Model serialization
* Streamlit application development

---

## 🔮 Future Improvements

Possible improvements include:

* Deploy the application online
* Add interactive EDA dashboards
* Add restaurant recommendation functionality
* Include sentiment analysis from customer reviews
* Experiment with XGBoost and LightGBM
* Add feature importance visualization
* Improve model validation using cross-validation within the complete pipeline
* Add confidence/uncertainty information to predictions

---

## ⚠️ Disclaimer

This application provides an **estimated restaurant rating based on the trained Machine Learning model**.

The prediction should not be considered a guaranteed actual restaurant rating.

---

## 👨‍💻 Author

**Ganesh Gokhale**

Computer Science & Engineering

### Project

**Zomato Restaurant Rating Prediction using Machine Learning**

---

⭐ If you found this project useful, consider giving the repository a star.
