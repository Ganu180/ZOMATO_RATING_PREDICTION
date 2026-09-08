# 🍽️ Zomato Restaurant Analytics & Rating Prediction

A complete **Data Analytics + Machine Learning project** that analyzes restaurant data and predicts restaurant ratings using a trained **Random Forest Regression** model.

The project combines:

- 📊 Exploratory Data Analysis
- 📈 Power BI Dashboard
- 🤖 Machine Learning
- ⚙️ Feature Engineering & Preprocessing
- 🔍 Hyperparameter Tuning
- 🌐 Streamlit Web Application
- 🚀 Model Deployment

---

## 📌 Project Overview

Restaurant ratings are influenced by several factors such as location, restaurant type, cuisines, online ordering, table booking, customer votes, and approximate cost.

This project analyzes these factors and builds a machine learning model to predict the expected restaurant rating.

The project has two major components:

1. **Restaurant Analytics Dashboard** — Business insights using Power BI.
2. **Restaurant Rating Prediction** — Machine learning model deployed through Streamlit.

---

## 🎯 Objectives

- Analyze restaurant distribution and characteristics.
- Identify important restaurant-related patterns.
- Study ratings, votes, cost, cuisines, and services.
- Analyze online ordering and table booking.
- Build a machine learning model for rating prediction.
- Compare multiple regression algorithms.
- Tune the best-performing model.
- Deploy the final model as an interactive web application.

---

# 📊 Power BI Dashboard

## Zomato Restaurant Analysis

The Power BI dashboard provides an interactive overview of the restaurant dataset.

### Key KPIs

| Metric | Value |
|---|---:|
| Total Restaurants | 41.59K |
| Average Rating | 3.70 |
| Total Votes | 15M |
| Average Cost for Two | ₹602.33 |
| Restaurants Offering Online Order | 65.28% |

### Dashboard Analysis

The dashboard includes:

- Restaurant count by location
- Average rating by location
- Top restaurant types
- Top cuisines
- Online order analysis
- Table booking analysis
- Cost vs. average rating
- Restaurant distribution
- Interactive filters

### Dashboard Filters

Users can filter the dashboard by:

- Location
- Online Order
- Restaurant Type
- Cuisine
- Table Booking

---

# 🤖 Machine Learning

## Problem Statement

Predict the restaurant's **aggregate rating** based on restaurant characteristics and customer engagement information.

### Problem Type

**Supervised Machine Learning → Regression**

### Target Variable

```text
rate
