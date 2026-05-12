import os

from fastapi import FastAPI, Header, HTTPException
import pandas as pd
import joblib
from dotenv import load_dotenv #this is used to load environment variables from a .env file to getenv
load_dotenv()





app = FastAPI()
# 👉 CORS must be here (immediately after app creation)
from fastapi.middleware.cors import CORSMiddleware# this is use for frontend and backend communication if they are on different domains or ports

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("API_KEY")


# 1. Load models
train_columns = joblib.load("x_train_columns.pkl")
le_brand = joblib.load("brand_encoded.pkl")
le_fuel = joblib.load("fuel_type_encoded.pkl")
car_name_model = joblib.load("target_mean.pkl")
model = joblib.load("USED_CAR_price_model.pkl")


# 🔐 API KEY CHECK
def verify_api_key(x_api_key):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.get("/")
def home():
    return {"status": "OK", "message": "Backend is running"}

@app.get("/health")
def health():
    return {"health": "good "}



# 🚀 2. Prediction API
@app.post("/predict")
def predict_car_price(data: dict, x_api_key: str = Header(None)):

    # check api key
    verify_api_key(x_api_key)

    new_car = data

    # Encode brand
    if new_car["brand"] in le_brand.classes_:
        brand_encoded = le_brand.transform([new_car["brand"]])[0]
    else:
        brand_encoded = -1

    # Encode fuel
    if new_car["fuel_type"] in le_fuel.classes_:
        fuel_encoded = le_fuel.transform([new_car["fuel_type"]])[0]
    else:
        fuel_encoded = -1

    # Target encoding
    target_model_name = car_name_model.get(
        new_car["car_model_name"], car_name_model.mean()
    )

    # Feature engineering
    car_age = 2024 - new_car['year_of_manufacture']

    # Create dataframe
    input_df = pd.DataFrame([{
        "kms_driven": new_car['kms_driven'],
        "car_age": car_age,
        "brand_encoded": brand_encoded,
        "fuel_type_encoded": fuel_encoded,
        "model_target_encoded": target_model_name
    }])

    # One-hot city
    for col in train_columns:
        if col.startswith("city_"):
            input_df[col] = 0

    city_col = "city_" + new_car['city']
    if city_col in input_df.columns:
        input_df[city_col] = 1

    # Reindex
    input_df = input_df.reindex(columns=train_columns, fill_value=0)

    # Predict
    price = model.predict(input_df)[0]

    return {
        "predicted_price": round(price, 2)
    }

   # uvicorn api:app --reload
   #__pycache__
# *.pyc
# .env not need in docker ignore file indeat use envirment properties in elastic beanstalke 
# .git
# venv this is add in doker ignor fill
  #this hash not add in docker ignore file 