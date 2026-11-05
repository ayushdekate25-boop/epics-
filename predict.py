import xgboost as xgb
import pandas as pd

# =====================================
# STEP 1: LOAD TRAINED MODEL
# =====================================

model = xgb.XGBRegressor()

model.load_model("xgboost_rul_model.json")

print("Aqua Twin RUL model loaded successfully!")

# =====================================
# STEP 2: ENTER SENSOR VALUES
# =====================================

flow_rate = float(input("Enter Flow Rate: "))
pressure = float(input("Enter Discharge Pressure: "))
tmp = float(input("Enter TMP: "))
orp = float(input("Enter ORP: "))
fac = float(input("Enter FAC: "))
flux = float(input("Enter Filtration Flux: "))

# =====================================
# STEP 3: PREPARE INPUT
# =====================================

input_data = pd.DataFrame([{
    "Flow_Rate": flow_rate,
    "Discharge_Pressure": pressure,
    "TMP": tmp,
    "ORP": orp,
    "FAC": fac,
    "Filtration_Flux": flux
}])

# =====================================
# STEP 4: PREDICT RUL
# =====================================

predicted_rul = model.predict(input_data)[0]

predicted_rul = max(1, min(180, predicted_rul))

print("\n========== AQUA TWIN ==========")

print(f"Predicted Synthetic RUL: {predicted_rul:.2f} days")

if predicted_rul < 30:
    print("Maintenance Status: Maintenance Alert")
else:
    print("Maintenance Status: Normal")

print("==============================")
