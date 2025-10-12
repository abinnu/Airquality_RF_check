# Airquality_RF_check

🌿 Air Quality Classification using Random Forest

📌 Overview : 

The Airquality_RF_check project is a Machine Learning-based classification system that predicts air quality levels based on various environmental factors. Using a Random Forest Classifier, the model analyzes pollutant concentrations and weather conditions to classify air quality into different categories.


This project focuses on :

  🧹 Cleaning and preprocessing real-world air quality data

  🌳 Training a Random Forest model for classification

  📊 Evaluating performance using multiple metrics 

  🌐 Deploying the model for real-time predictions


📂 Dataset :

  * Source: [Kaggle - Air Quality Data](https://www.kaggle.com/datasets)
  
  * Shape:  52705 rows × 10 features

  * Features :
  
       PM2.5, PM10, NO2, CO, SO2, O3 – pollutant levels
  
       Temperature, Humidity, Wind Speed – weather indicators

       Air Quality Index (AQI) – target label

  * Target Classes :
  
    🌿 Good,
    🌤 Moderate,
    🌫 Unhealthy,
    🌪 Very Unhealthy,
    ☠️ Hazardous


🚀 Features :

   ✅ Data Cleaning & Missing Value Handling

   ✅ Feature Engineering & Label Encoding

   ✅ Model Training using Random Forest

   ✅ Hyperparameter Tuning for Better Accuracy

   ✅ Model Evaluation using Multiple Metrics

   ✅ Dockerized Deployment for Real-time Predictions


🧠 Tech Stack :

   * Programming Language → Python 

   * Machine Learning → Scikit-learn

   * Data Processing → Pandas, NumPy

   * Visualization → Matplotlib, Seaborn

   * Deployment → Docker


📊 Model Evaluation :

| Metric        | Score |
| ------------- | ----- |
| **Accuracy**  | 93%   |
| **Precision** | 93%   |
| **Recall**    | 93%   |
| **F1-Score**  | 93%   |


🌐 Deployment (Dockerized) :

   1️⃣ Build Docker Image
   
   docker build -t ml-airquality-app .

  2️⃣ Run Docker Container

   docker run -d -p 5000:5000 ml-airquality-app

3️⃣ Access the App

   Open your browser and visit:http://localhost:5000

## Air Quality Classification Dashboard

This interactive Tableau dashboard visualizes air quality data and AQI classification using a Random Forest model. It includes:

- City-wise AQI levels
- AQI trends over time
- Pollutant contributions (PM2.5, PM10, NO2, SO2)
- KPI cards showing model accuracy

🔗 [View Dashboard on Tableau Public](https://public.tableau.com/app/profile/abinnu.peter/viz/Airquality_Dashboard/Dashboard1)


🤝 Contribution :

   Contributions are welcome! 🎉, If you'd like to improve this project, Feel free to :

   - **Fork** the repository 🍴  
   - **Create a feature branch**  
   - **Submit a pull request** 🚀  

Your feedback, ideas, and suggestions are always appreciated! 🙌


👨‍💻 Author :

   Abinnu John Peter.P

   📧 Email: abinnu75@gmail.com

   🔗 LinkedIn : www.linkedin.com/in/abinnu
