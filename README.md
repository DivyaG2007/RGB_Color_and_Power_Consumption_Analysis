# Power Consumption Prediction Using RGB Values

## Project Overview
This project uses **Machine Learning (ML)** to predict power consumption based on **RGB color intensity, brightness levels, ambient light, and temperature**.  
It builds on the earlier analysis of color and brightness by adding predictive modeling, hyperparameter tuning, and a deployable Streamlit interface for real-time visualization and prediction.

---

## Objectives
- Build predictive ML models to estimate power consumption from RGB and environmental factors.  
- Compare regression algorithms for performance and accuracy.  
- Optimize the best model using **Grid Search CV**.  
- Create a deployable and interactive **Streamlit dashboard** for real-time insights.

---

## Data Overview
- **Dataset:** 100 RGB color samples with ambient light and temperature readings.  
- **Features Used:**
  - R, G, B intensity  
  - Original Brightness  
  - Ambient Lux  
  - Temperature  
- **Target Variable:** Estimated Power (W)

---

## Technical Workflow
1. **Data Preprocessing**
   - Cleaned and standardized input data using `StandardScaler`.
2. **Feature Selection**
   - Selected six key features influencing power consumption.
3. **Model Building**
   - Trained multiple regression models:
     - Linear Regression  
     - Random Forest Regressor  
     - Gradient Boosting Regressor  
     - Neural Network (MLP Regressor)
4. **Evaluation Metrics**
   - R² Score  
   - RMSE (Root Mean Square Error)  
   - MAE (Mean Absolute Error)
5. **Hyperparameter Tuning**
   - Performed **Grid Search** on the Random Forest model to identify the best configuration.
6. **Deployment**
   - Streamlit app hosted via **Ngrok tunnel** for public access.  
   - Model and scaler saved using `joblib` for future inference.

---

## Visual Insights
- **Model Comparison Bar Chart** — R² scores for each model.  
- **Feature-Impact Visualization** — Correlation between RGB and power.  
- **Interactive Streamlit Dashboard** — Input color and environment to predict power.

---

## Key Features
- Intelligent **ML-driven prediction** of power usage.  
- Automated **model optimization** using Grid Search.  
- **Reusable trained models** stored as `.pkl` files.  
- **Deployed Streamlit interface** for live predictions.

---

## Skills Demonstrated
- Machine Learning model development  
- Hyperparameter optimization (GridSearchCV)  
- Data preprocessing and scaling  
- Model evaluation and visualization  
- Deployment using Streamlit + Ngrok  
- Analytical reasoning for energy efficiency

---

## Future Enhancements
- Integrate **Deep Learning models** for complex RGB–power relationships.  
- Add **real-time brightness sensor data** for IoT-based energy analysis.  
- Implement **auto-optimization algorithms** for adaptive brightness control.

---

## Dependencies
Install the required libraries:
```bash
pip install scikit-learn streamlit joblib pandas numpy matplotlib seaborn openpyxl
