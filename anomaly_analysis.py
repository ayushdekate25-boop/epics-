import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_water_data.csv")

# Select sensor columns
sensor_columns = [
    "Flow_Rate",
    "Discharge_Pressure",
    "TMP",
    "ORP",
    "FAC",
    "Filtration_Flux",
    "UF_ MP"
]

# Check minimum and maximum values
print("\nSensor minimum values:")
print(df[sensor_columns].min())

print("\nSensor maximum values:")
print(df[sensor_columns].max())

# Plot TMP distribution
plt.figure(figsize=(8, 5))
plt.hist(df["TMP"].dropna(), bins=50)

plt.title("TMP Distribution")
plt.xlabel("TMP")
plt.ylabel("Frequency")

plt.show()

# Plot Flow Rate distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Flow_Rate"].dropna(), bins=50)

plt.title("Flow Rate Distribution")
plt.xlabel("Flow Rate")
plt.ylabel("Frequency")

plt.show()
