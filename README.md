# 🔋 Battery Health Prediction and Anomaly Detection System for EVs

## Overview
This project implements an end-to-end AI system to monitor EV battery behavior, predict battery health (SoH), detect anomalies, estimate remaining useful life (RUL), and explain model decisions using Explainable AI.

## Problem
EV batteries degrade unpredictably, leading to safety risks, sudden failures, and high replacement costs. Existing systems often fail to detect early degradation.

## Solution
We built an ML-based system that:
- Predicts battery State of Health (SoH)
- Detects abnormal battery behavior
- Estimates Remaining Useful Life (RUL)
- Explains predictions using SHAP (Explainable AI)
- Visualizes results on a dashboard

## Tech Stack
- Python
- Pandas, NumPy, scikit-learn
- Flask (Backend API)
- Streamlit (Frontend Dashboard)
- SHAP (Explainable AI)
- GitHub (Version Control)

## Dataset
Battery sensor dataset containing:
- Voltage, Current, Temperature
- Charging voltage and current
- Time (used as usage proxy)

## How to Run
1. Create and activate virtual environment

2. Install dependencies:pip install pandas numpy matplotlib scikit-learn flask streamlit shap joblib

3. Start backend:python backend/api.py

4. Start frontend:streamlit run frontend/app.py


## Outputs
- Battery Health (%)
- Status: Normal / Warning / Critical
- Anomaly Detection
- Remaining Useful Life (RUL)
- Explainable AI visualizations

## Sustainability Impact
Early detection extends battery life, reduces waste, and supports greener EV adoption.

## Author
Internship Project – Python Green AI


