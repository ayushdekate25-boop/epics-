import pandas as pd
import numpy as np

# ==========================================
# STEP 1: LOAD CLEANED DATA
# ==========================================

df = pd.read_csv("dataset/cleaned_water_data.csv")

print("Dataset loaded:", df.shape)

# ==========================================
# STEP 2: SELECT SENSOR FEATURES
# ==========================================

features = [
    "Flow_Rate",
    "Discharge_Pressure",
    "TMP",
    "ORP",
    "FAC",
    "Filtration_Flux"
]

df = df[["Date"] + features].copy()

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Convert sensor values to numeric
for col in features:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Sort chronologically
df = df.sort_values("Date")

# Remove rows with missing sensor values
df = df.dropna(subset=features)

# Exclude zero-flow records from this initial
# synthetic degradation simulation.
df = df[df["Flow_Rate"] > 0].copy()

print("Records after cleaning:", df.shape)

# ==========================================
# STEP 3: NORMALIZE SENSOR VALUES
# ==========================================

# Percentile ranks map values between 0 and 1.
# These are relative scores, not physical limits.

df["TMP_Score"] = df["TMP"].rank(pct=True)

df["Flow_Score"] = df["Flow_Rate"].rank(pct=True)

# Higher TMP score = higher simulated degradation
# Lower flow score = higher simulated degradation

df["Degradation_Score"] = (
    0.5 * df["TMP_Score"]
    + 0.5 * (1 - df["Flow_Score"])
)

# ==========================================
# STEP 4: GENERATE SYNTHETIC RUL
# ==========================================

# Assumption for prototype:
# Maximum simulated RUL = 180 days

MAX_RUL_DAYS = 180

df["Synthetic_RUL_Days"] = (
    MAX_RUL_DAYS * (1 - df["Degradation_Score"])
)

df["Synthetic_RUL_Days"] = (
    df["Synthetic_RUL_Days"].clip(1, MAX_RUL_DAYS)
)

# ==========================================
# STEP 5: SAVE DATASET
# ==========================================

df.to_csv(
    "dataset/synthetic_rul_data.csv",
    index=False
)

print("\nSynthetic RUL dataset created!")

print("\nFirst 5 rows:")
print(df.head())

print("\nRUL statistics:")
print(df["Synthetic_RUL_Days"].describe())

print("\nSaved to dataset/synthetic_rul_data.csv")