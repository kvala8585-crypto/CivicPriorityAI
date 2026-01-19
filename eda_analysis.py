import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_PATH = r"C:\Users\kavi vala\Desktop\CivicPriorityAI"
DATA_PATH = os.path.join(BASE_PATH, "data","raw", "cleaned_complaints.csv")

df = pd.read_csv(DATA_PATH)

print(df.head())
print(df.info())

# PRIORITY DISTRIBUTION
if "priority" in df.columns:
    df["priority"].value_counts().plot(kind="bar")
    plt.title("Complaint Priority Distribution")
    plt.xlabel("Priority Level")
    plt.ylabel("Count")
    plt.show()

# COMPLAINT TYPE DISTRIBUTION
if "complaint_type" in df.columns:
    df["complaint_type"].value_counts().head(10).plot(kind="bar")
    plt.title("Top Complaint Types")
    plt.show()

# DESCRIPTION LENGTH ANALYSIS
if "description_length" in df.columns:
    df["description_length"].hist(bins=30)
    plt.title("Complaint Description Length")
    plt.show()

print("✅ EDA Completed")
