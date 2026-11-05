import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_water_data.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Basic statistics
print("\nDataset Statistics:")
print(df.describe())

# Plot Flow Rate
plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Flow_Rate"])
plt.title("Water Flow Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Flow Rate")
plt.show()

# Plot TMP
plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["TMP"])
plt.title("Transmembrane Pressure Over Time")
plt.xlabel("Date")
plt.ylabel("TMP")
plt.show()

# Plot Filtration Flux
plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Filtration_Flux"])
plt.title("Filtration Flux Over Time")
plt.xlabel("Date")
plt.ylabel("Filtration Flux")
plt.show()