import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import os

# Sample training data
X = np.array([
    [35, 85, 12, 200],
    [30, 70, 5, 10],
    [40, 90, 20, 300],
    [25, 60, 3, 5]
])
y = [1, 0, 1, 0]  # 1 = Disaster, 0 = No disaster

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save to realtime_help/disaster_predictor.pkl
output_path = os.path.join('realtime_help', 'disaster_predictor.pkl')
joblib.dump(model, output_path)

print(f"✅ Model saved to {output_path}")
