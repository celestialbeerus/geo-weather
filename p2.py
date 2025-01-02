import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
url = 'https://example.com/car_prices.csv'  # Replace with actual dataset URL
data = pd.read_csv(url)

# Data cleaning (example)
data = data.dropna()  # Drop rows with missing values

# Feature selection
features = ['make', 'model', 'year', 'mileage']  # Replace with actual features
X = pd.get_dummies(data[features])  # One-hot encode categorical variables
y = data['price']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict car prices
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Example prediction for a new car
new_car = pd.DataFrame({
    'make': ['Toyota'],  # Replace with new data
    'model': ['Corolla'],
    'year': [2021],
    'mileage': [5000]
})
new_car_encoded = pd.get_dummies(new_car)
predicted_price = model.predict(new_car_encoded)
print(f'Predicted Price: {predicted_price[0]}')
