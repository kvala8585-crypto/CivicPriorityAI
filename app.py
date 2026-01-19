# Streamlit library import (web app banane ke liye)

import streamlit as st

# Data handling ke liye pandas import

import pandas as pd

# Trained ML model load karne ke liye pickle

import pickle

# File paths handle karne ke liye os module

import os

# PROJECT PATHS SETUP

# Project ka base directory path

BASE_PATH = r"C:\Users\kavi vala\Desktop\CivicPriorityAI"

# Trained ML model ka path

MODEL_PATH = os.path.join(BASE_PATH, "model", "priority_model.pkl")

# Cleaned dataset ka path

DATA_PATH = os.path.join(BASE_PATH, "data", "raw", "cleaned_complaints.csv")


# LOAD TRAINED MODEL

# Pickle file se trained model load karna

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# LOAD DATA (COLUMN STRUCTURE KE LIYE)
# CSV data load karna (sirf input fields ke structure ke liye)

df = pd.read_csv(DATA_PATH)

# PAGE CONFIGURATION

# Page ka title aur layout set karna

st.set_page_config(page_title="CivicPriorityAI", layout="centered")

# CUSTOM CSS DESIGN


st.markdown("""

<style>
body {
    background-color: #0e1117;
}
h1 {
    color: #00e5ff;
    text-align: center;
}
div.stButton > button {
    background-color: #2563eb;
    color: white;
    padding: 10px 24px;
    border-radius: 8px;
    font-size: 16px;
}
div.stButton > button:hover {
    background-color: #1e40af;
}
</style>

""", unsafe_allow_html=True)

# App ka main heading display karna

st.title("🏛️ Citizen Complaint Priority Prediction")


# USER INPUT SECTION
# User ke inputs store karne ke liye empty dictionary

inputs = {}

# Priority label ko drop karke baaki sab columns ke input fields banana

for col in df.drop("priority_label", axis=1).columns:

# Har feature ke liye numeric input lena
    inputs[col] = st.number_input(col, value=0)

# PREDICTION SECTION
# Predict button create karna

if st.button("Predict Priority"):
# User inputs ko DataFrame me convert karna
    input_df = pd.DataFrame([inputs])

# Model se prediction nikalna
prediction = model.predict(input_df)[0]

# Prediction result success message ke sath dikhana
st.success(f"Predicted Priority label: {prediction}")

