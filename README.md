# 🍽️ Zomato Restaurant Analytics & Rating Prediction

### 📊 Data science • 🤖 Machine Learning • 📈 Power BI • 🌐 Streamlit

An end-to-end **Data Analytics and Machine Learning project** that analyzes restaurant data, uncovers patterns affecting restaurant ratings, and predicts ratings using a tuned **Random Forest Regressor**.

The project demonstrates a complete data science workflow — from **data cleaning and exploratory analysis to dashboard development, machine learning, model evaluation, and cloud deployment**.

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)

---

## 📌 Project Overview

Restaurant platforms contain valuable information about **cuisines, pricing, locations, online ordering, table booking, customer preferences, and ratings**.

This project uses that information to:

- Analyze restaurant trends and customer preferences
- Discover factors associated with restaurant ratings
- Build an interactive **Power BI dashboard**
- Develop a Machine Learning model for rating prediction
- Optimize the model using hyperparameter tuning
- Deploy the final prediction system as a **Streamlit web application**

---

## 🎯 Project Objectives

- Perform data cleaning and preprocessing
- Conduct Exploratory Data Analysis (EDA)
- Analyze restaurant and customer-related patterns
- Visualize business insights using Power BI
- Perform feature engineering for Machine Learning
- Build a restaurant rating prediction model
- Tune and evaluate the final model
- Create an interactive prediction application
- Deploy the application to the cloud

---

## 🛠️ Tech Stack

| Area | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Business Intelligence | Power BI |
| Machine Learning | Scikit-learn, Random Forest |
| Model Optimization | Hyperparameter Tuning |
| Web Application | Streamlit |
| Development | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

---

## 📊 Exploratory Data Analysis

The dataset was cleaned and explored to understand restaurant characteristics and rating patterns.

### Key Areas Analyzed

- Restaurant rating distribution
- Online ordering availability
- Table booking availability
- Cost distribution
- Location-wise restaurant performance
- Cuisine patterns
- Relationship between restaurant features and ratings

EDA helped identify meaningful patterns and provided the foundation for **feature engineering and model development**.

---

# 📈 Power BI Dashboard

An interactive **Power BI dashboard** was created to convert restaurant data into meaningful business insights.

The dashboard provides insights into:

- Overall restaurant performance
- Rating distribution
- Location-wise trends
- Online ordering behavior
- Table booking trends
- Cost patterns
- Cuisine-level insights

### 📊 Dashboard Preview

![Power BI Dashboard](screenshots/powerbi_dashboard.png)

---

# 🤖 Machine Learning Model

The Machine Learning stage focused on predicting restaurant ratings using restaurant-related features.

After model development and optimization, the final prediction system uses a tuned **Random Forest Regressor**.

## 🎯 Final Model Performance

| Metric | Score |
|---|---:|
| MAE | **0.1603** |
| RMSE | **0.2233** |
| R² Score | **0.7409** |

### 📌 Performance Interpretation

- **MAE = 0.1603** — predictions differ from actual ratings by approximately **0.16 rating points on average**.
- **RMSE = 0.2233** — indicates relatively low overall prediction error.
- **R² = 0.7409** — the model explains approximately **74.09% of the variation in restaurant ratings** in the evaluation data.

---

## 🔄 Model Workflow

The complete Machine Learning pipeline covers preprocessing, feature engineering, model development, optimization, evaluation, and deployment.

![Model Workflow](screenshots/model_workflow.png)

### End-to-End Workflow

```text
Raw Dataset
      ↓
Data Cleaning & Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Train-Test Split
      ↓
Random Forest Regression
      ↓
Hyperparameter Tuning
      ↓
Model Evaluation
      ↓
Model Serialization
      ↓
Streamlit Application
      ↓
Cloud Deployment
```

---

# 🌐 Streamlit Prediction Application

The trained model was integrated into an interactive **Streamlit web application**.

Users can provide restaurant-related information and receive a predicted restaurant rating from the trained Random Forest model.

### ✨ Application Features

- Simple and interactive user interface
- Restaurant feature input
- Real-time rating prediction
- Pre-trained Random Forest model
- Input validation
- Cloud deployment

### 🖥️ Application Preview

![Streamlit Prediction App](screenshots/streamlit_app.png)

### 🎯 Prediction Result

![Prediction Result](screenshots/prediction_results.png)

### 🚀 Live Application

[![Open Streamlit App](https://img.shields.io/badge/Launch-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](LIVE_APP_URL)

---

# 📁 Repository Structure

```text
ZOMATO_RATING_PREDICTION/
│
├── Dashboard/
│
├── notebooks/
│   └── Zomato_Rating_Prediction.ipynb
│
├── screenshots/
│   ├── powerbi_dashboard.png
│   ├── model_workflow.png
│   ├── streamlit_app.png
│   └── prediction_results.png
│
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
├── zomato_cleaned.csv
└── zomato_rating_model.pkl
```

---

# 🚀 Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ganu180/ZOMATO_RATING_PREDICTION.git
```

### 2️⃣ Navigate to the Project

```bash
cd ZOMATO_RATING_PREDICTION
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open locally in your browser.

---

# 💡 Key Learnings

Through this project, I gained hands-on experience in:

- Cleaning and preprocessing real-world data
- Performing Exploratory Data Analysis
- Identifying meaningful patterns in data
- Creating interactive Power BI dashboards
- Feature engineering for Machine Learning
- Building regression models
- Hyperparameter tuning
- Evaluating models using MAE, RMSE, and R²
- Integrating trained models with Streamlit
- Deploying Machine Learning applications
- Managing large serialized model files
- Using Git and GitHub for version control

---

# 🔮 Future Improvements

Potential future enhancements include:

- Compare additional regression algorithms
- Explore advanced feature engineering techniques
- Add model explainability using SHAP
- Enhance Streamlit UI/UX
- Add additional restaurant analytics
- Automate model retraining
- Develop a prediction API
- Explore containerized deployment

---

# 👨‍💻 Author

## Ganesh Gokhale

**Data Analyst | Aspiring Data Scientist**

Python • SQL • Power BI • Machine Learning • Data Analytics

💼 **LinkedIn:** [Ganesh Gokhale](https://www.linkedin.com/in/ganesh-gokhale-g18/)

📧 **Email:** [iamganeshgokhale180@gmail.com](mailto:iamganeshgokhale180@gmail.com)

🐙 **GitHub:** [Ganu180](https://github.com/Ganu180)

---

## ⭐ Support

If you found this project interesting, consider giving the repository a ⭐.

**Thanks for visiting!**
