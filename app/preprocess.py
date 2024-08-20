import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

import os
path = r'C:/Users/USER/Downloads/synthetic_energy_consumption_large (1).csv'
print(os.path.exists(path))  # This should return True

data = pd.read_csv(path)

data['Date'] = pd.to_datetime(data['Date'])

# Now you can extract the month
data['Month'] = data['Date'].dt.month

# Similarly, you can extract the year
data['Year'] = data['Date'].dt.year

X = data[['Year', 'Month', 'Electricity', 'Gas', 'Oil']]
y= data['Total_Consumption']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()

# Fit and transform the training data
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)  # Also transform the validation set

# Save the processed data and the scaler for future use
pd.DataFrame(X_train_scaled).to_csv('data/X_train_scaled.csv', index=False)
pd.DataFrame(X_val_scaled).to_csv('data/X_val_scaled.csv', index=False)
pd.DataFrame(y_train).to_csv('data/y_train.csv', index=False)
pd.DataFrame(y_val).to_csv('data/y_val.csv', index=False)

import joblib
joblib.dump(scaler, 'app/scaler.pkl')

