import pandas as pd
import numpy as np

# 1. Load the raw dataset using relative path
df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# 2. Fix the TotalCharges text trap
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# 3. Fill any missing TotalCharges values with 0
df['TotalCharges'] = df['TotalCharges'].fillna(0)

# 4. Create clean Tenure Groups
def categorize_tenure(months):
    if months <= 12:
        return '0-1 Year'
    elif months <= 24:
        return '1-2 Years'
    elif months <= 48:
        return '2-4 Years'
    else:
        return '4+ Years'

df['Tenure_Group'] = df['tenure'].apply(categorize_tenure)

# 5. Export clean dataset
df.to_csv("data/processed/Clean_Telco_Customer_Churn.csv", index=False)
print("Data cleaned successfully! Ready for Tableau.")