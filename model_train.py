import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

BASE_PATH = r"C:\Users\kavi vala\Desktop\CivicPriorityAI"
DATA_PATH = os.path.join(BASE_PATH, "data","raw", "cleaned_complaints.csv")
MODEL_PATH = os.path.join(BASE_PATH, "model", "priority_model.pkl")

df = pd.read_csv(DATA_PATH)

# Dataset me available columns dekhne ke liye

print("Columns:", df.columns)

# Dataset me priority target column automatically detect karne ke liye

possible_targets = ["priority", "priority_label", "complaint_priority"]

# Target column ko initially None set karna

TARGET = None

# Possible target names me se jo column dataset me mile use select karna

for col in possible_targets:
    if col in df.columns:
        TARGET = col
        break

# Agar priority related koi column na mile to error raise karna

if TARGET is None:
    raise ValueError("❌ No priority column found in dataset")

# Final target column print karna

print("🎯 Target Column:", TARGET)

# Features (input data) aur target (output label) separate karna

X = df.drop(TARGET, axis=1)
y = df[TARGET]

# Data ko training aur testing set me divide karna

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

# Random Forest classification model initialize karna

model = RandomForestClassifier(random_state=42)

# Training data par model train karna

model.fit(X_train, y_train)

# Test data par prediction nikalna

pred = model.predict(X_test)

# Model accuracy calculate karna

print("✅ Accuracy:", accuracy_score(y_test, pred))

# Trained model ko pickle file me save karna

with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

# Model training aur saving confirmation

print("🎉 Model Trained & Saved Successfully")
