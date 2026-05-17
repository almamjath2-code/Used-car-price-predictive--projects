# 🚗 Car Price Prediction
# 📌 Overview

This project predicts used car prices using Machine Learning.
The application analyzes different car features such as brand, fuel type, kilometers driven, city, and car age to estimate the market price of a used car.

# The project includes:

Data Cleaning
Data Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Machine Learning Model Training
Model Evaluation
Model Deployment
# 🌐 Live Demo  
Frontend Application 

Car Price Prediction App: http://car-price-frontend-app.s3-website.ap-south-1.amazonaws.com/

🖥️ Project Architecture
User → Frontend (AWS S3)
      ↓
Frontend sends request to Backend API
      ↓
Backend (FastAPI/Flask on AWS Elastic Beanstalk)
      ↓
ML Model predicts car price
      ↓
Prediction returned to Frontend
📊 Dataset Features

# The dataset contains the following features:

Feature	Description
brand	Car brand name
car_model	Model name
fuel_type	Fuel type
kms_driven	Total kilometers driven
city	City where the car is available
car_age	Age of the car
car_price	Target variable

# ⚙️ Project Workflow
1️⃣ Data Cleaning
Removed missing values
Removed duplicates
Fixed inconsistent data
2️⃣ Data Preprocessing
Label Encoding
Target Encoding
Feature Preparation
3️⃣ Exploratory Data Analysis (EDA)
Brand-wise price analysis
Fuel type analysis
Correlation analysis
Price distribution visualization
4️⃣ Feature Engineering

Created meaningful features to improve prediction performance.

5️⃣ Model Building

Machine Learning algorithm used:

Random Forest Regressor
6️⃣ Model Evaluation

# Evaluation Metrics:

R² Score
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
7️⃣ Model Saving

Saved trained model and encoders using Pickle.

# 📁 Saved Files
File Name	Description
car_price_model.pkl	Trained ML model
brand_encoder.pkl	Brand encoder
fuel_encoder.pkl	Fuel type encoder
x_train_columns.pkl	Training columns
target_mean.pkl	Target encoding values
📈 Results
Metric	Score
R² Score	0.94

The model achieved high prediction accuracy on the test dataset.

# 🛠️ Technologies Used
Programming Language
Python
Libraries
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
joblip
Backend
FastAPI / Flask
Frontend
HTML
CSS
JavaScript
Cloud & Deployment
AWS S3
AWS Elastic Beanstalk
GitHub Actions
# ☁️ Deployment
Frontend Deployment

Frontend is hosted using:

AWS S3 Static Website Hosting
Backend Deployment

Backend API is deployed using:

AWS Elastic Beanstalk
CI/CD

Automated deployment using:

# GitHub Actions
▶️ How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/almamjath2-code/Used-car-price-predictive--projects.git
cd car-price-prediction
2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Requirements
pip install -r requirements.txt
4️⃣ Run Backend
python app.py

OR

uvicorn app:app --reload
5️⃣ Open Application
http://127.0.0.1:5000

OR

http://127.0.0.1:8000
📡 API Example
Prediction Endpoint
POST /predict
Sample Request
{
  "brand": "Tata",
  "fuel_type": "Diesel",
  "car_model": "Safari XZ Plus",
  "car_age": 3,
  "kms_driven": 12999,
  "city": "Bangalore"
}
Sample Response
{
  "predicted_price": "18.5 Lakhs"
}
📷 Screenshots

Add screenshots inside an images folder.

# Example:

![Home Page](images/homepage.png)
![Prediction Result](images/result.png)
🚀 Future Improvements
Add Deep Learning models
Improve UI/UX
Add user authentication
Deploy custom domain
Add real-time car market API
Add more advanced feature engineering
🤝 Contributing

Contributions are welcome.

Steps:

Fork the repository
Create a new branch
Commit changes
Push branch
Create Pull Request
📜 License

# This project is licensed under the MIT License.

👨‍💻 Author

Developed by amjath

GitHub:https://github.com/almamjath2-code

