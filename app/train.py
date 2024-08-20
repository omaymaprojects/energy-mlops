import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load the processed data
X_train = pd.read_csv('data/X_train_scaled.csv')
X_val = pd.read_csv('data/X_val_scaled.csv')
y_train = pd.read_csv('data/y_train.csv').values.ravel()
y_val = pd.read_csv('data/y_val.csv').values.ravel()

# Initialize and train the model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_val)
mse = mean_squared_error(y_val, y_pred)
print(f'Mean Squared Error: {mse}')

# Save the trained model
joblib.dump(model, 'app/model.pkl')
