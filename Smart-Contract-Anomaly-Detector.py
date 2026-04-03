import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import onnx

# ==========================================
# 1. Data Preparation
# ==========================================
# Features:
# [Gas_Used, Gas_Price, Method_Call_Frequency, Value_Transferred]
# Method_Call_Frequency: Number of times the same function has been called within the last 10 blocks.

X_train = np.array([
    # Normal Transactions -> Label 0
    [50000, 20.0, 1, 0.5],    # Normal gas usage, low frequency
    [100000, 25.0, 2, 1.0],   # Moderate contract interaction
    [60000, 15.0, 1, 0.1],    # Simple transfer

    # Suspicious Patterns/Exploits -> Label 1
    [800000, 100.0, 15, 0.0],  # Very high gas usage, high frequency (Reentrancy or DoS attempt)
    [500000, 150.0, 10, 0.01], # High gas, rapid function calls (potential exploit)
    [900000, 50.0, 20, 0.0]    # Abnormal gas consumption with high frequency
], dtype=np.float32)

# Labels: 0 = Normal, 1 = Anomaly/Suspicious
y_train = np.array([0, 0, 0, 1, 1, 1], dtype=np.int64)

# ==========================================
# 2. Model Creation and Training
# ==========================================
print("[System] Training the Smart Contract Anomaly Detector model...")
# Using RandomForest as it is robust for small datasets and provides good accuracy.
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)
print("[System] Model training complete.")

# ==========================================
# 3. Convert the Model to ONNX format (Required for OpenGradient)
# ==========================================
print("[System] Converting model to ONNX format...")

# Define the input type: variable rows with 4 features of type Float.
initial_type = [('float_input', FloatTensorType([None, 4]))]

# Convert the Scikit-learn model to ONNX.
onx = convert_sklearn(model, initial_types=initial_type)

# ==========================================
# 4. Save the final ONNX file
# ==========================================
model_filename = "smart_contract_anomaly_detector.onnx"
with open(model_filename, "wb") as f:
    f.write(onx.SerializeToString())

print(f"✅ Success! Created: '{model_filename}'")
print("[System] The model is now ready for deployment to the OpenGradient Model Hub.")
