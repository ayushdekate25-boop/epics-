import pandas as pd
import numpy as np

# =====================================
# STEP 1: LOAD DATA
# =====================================

df = pd.read_csv("dataset/water_data.csv")

print("Dataset loaded successfully!")
print("Original shape:", df.shape)

# =====================================
# STEP 2: CLEAN COLUMN NAMES
# =====================================

df.columns = df.columns.str.strip()

# =====================================
# STEP 3: CONVERT DATE
# =====================================

df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

# =====================================
# STEP 4: CHECK MISSING VALUES
# =====================================

print("\nMissing values:")
print(df.isnull().sum())

# =====================================
# STEP 5: REMOVE INVALID DATES
# =====================================

df = df.dropna(subset=["Date"])

# =====================================
# STEP 6: SORT BY DATE
# =====================================

df = df.sort_values("Date")

# =====================================
# STEP 7: CHECK DATA
# =====================================

print("\nCleaned dataset shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
df.info()

# =====================================
# STEP 8: SAVE CLEANED DATA
# =====================================

df.to_csv("dataset/cleaned_water_data.csv", index=False)

print("\nCleaned dataset saved successfully!")