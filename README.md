# 📈 Sales Forecasting & Analytics Engine

## 🎯 Project Overview
This project was developed to automate revenue forecasting . By moving away from manual Excel tracking, we implemented a machine learning pipeline that provides data-driven insights for quarterly planning.

## 🚀 Technical Features
* **Machine Learning:** Implemented a **Random Forest Regressor** to handle non-linear business trends.
* **Feature Engineering:** Created **Lag Features** (Previous Month Sales) and **3-Month Rolling Averages** to capture seasonality.
* **Prevention of Data Leakage:** Utilized time-series splitting (non-shuffled) to ensure realistic production testing.
* **Interactive Dashboard:** Built with **Streamlit** to allow stakeholders to filter results by region.

## 🛠️ Tech Stack
* **Python** (Pandas, Scikit-Learn, NumPy)
* **Streamlit** (Frontend Dashboard)
* **Git/GitHub** (Version Control)

## 📊 Results
The model achieved an **88% R-squared accuracy** on unseen data, significantly improving the reliability of monthly sales targets.
