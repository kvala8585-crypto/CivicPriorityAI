import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

# Project ka base folder path

BASE_PATH = r"C:\Users\kavi vala\Desktop\CivicPriorityAI"

# Cleaned dataset ka path

DATA_PATH = os.path.join(BASE_PATH, "data", "raw", "cleaned_complaints.csv")

# CSV file ko DataFrame me load karna

df = pd.read_csv(DATA_PATH)

# LabelEncoder object banana (text ko number me convert karne ke liye)

le = LabelEncoder()

# Har column par loop chalana

for col in df.columns:

# Agar column categorical (text/object) type ka ho
    if df[col].dtype == "object":
    
    # Text values ko numeric labels me convert karna
         df[col] = le.fit_transform(df[col])


# Encoded data ko wapas same CSV file me save karna

df.to_csv(DATA_PATH, index=False)

# Feature engineering completion message

print("✅ Feature Engineering Done")
#LabelEncoder categorical data (High, Medium, Low) ko numbers (0,1,2) me convert karta hai

#ML models sirf numeric data samajhte hain

#Ye step model training se pehle mandatory hota hai
