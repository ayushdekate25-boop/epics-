import pandas as pd
import numpy as np
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# =====================================
# STEP 1: LOAD DATASET
# =====================================

df = pd.read_csv("dataset/synthetic_rul_data.csv")

print("Dataset loaded:", df.shape)

# =====================================
# STEP 2: SELECT FEATURES AND TARGET
# =====================================

features = [
    "Flow_Rate",
    "Discharge_Pressure",
    "TMP",
    "ORP",
    "FAC",
    "Filtration_Flux"
]

X = df[features]

y = df["Synthetic_RUL_Days"]

# =====================================
# STEP 3: SPLIT DATA
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# =====================================
# STEP 4: TRAIN XGBOOST
# =====================================

model = xgb.XGBRegressor(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    objective="reg:squarederror",
    random_state=42
)

print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed!")

# =====================================
# STEP 5: PREDICTIONS
# =====================================

y_pred = model.predict(X_test)

# =====================================
# STEP 6: EVALUATION
# =====================================

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)

r2 = r2_score(y_test, y_pred)

print("\nMODEL PERFORMANCE")

print("MAE:", round(mae, 2), "days")
print("RMSE:", round(rmse, 2), "days")
print("R2 Score:", round(r2, 4))

# =====================================
# STEP 7: SAVE MODEL
# =====================================

model.save_model("xgboost_rul_model.json")

print("\nModel saved successfully!")