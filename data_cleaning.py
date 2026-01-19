import pandas as pd
import os

# PATHS
BASE_PATH = r"C:\Users\kavi vala\Desktop\CivicPriorityAI"
RAW_DATA_PATH = os.path.join(BASE_PATH, "data", "raw","citizen_complaints.csv")

CLEAN_DATA_PATH = os.path.join(BASE_PATH, "data","raw", "cleaned_complaints.csv")

# LOAD DATA
df = pd.read_csv(RAW_DATA_PATH)

print("Initial Shape:", df.shape)

# STANDARDIZE COLUMN NAMES
df.columns = df.columns.str.lower().str.replace(" ", "_")

# DROP DUPLICATES
df.drop_duplicates(inplace=True)

# HANDLE MISSING VALUES
for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna("Unknown", inplace=True)
    else:
        df[col].fillna(df[col].median(), inplace=True)

# CREATE NEW FEATURE
if "complaint_description" in df.columns:
    df["description_length"] = df["complaint_description"].apply(len)

# SAVE CLEANED DATA
df.to_csv(CLEAN_DATA_PATH, index=False)

print("Cleaned Shape:", df.shape)
print("✅ Data Cleaning Completed & Saved")
