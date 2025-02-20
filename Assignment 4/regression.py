import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Load the data
file_path = 'StudentsPerformance.csv'
data = pd.read_csv(file_path)


data = pd.get_dummies(data, drop_first=True)

# Define the features and the target variable
X = data.drop(['math score', 'reading score', 'writing score'], axis=1)
y = data[['math score', 'reading score', 'writing score']]

print(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
print(f'R² score: {r2}')

# Plot the results
plt.figure(figsize=(15, 5))

# Plot for math score
plt.subplot(1, 3, 1)
plt.scatter(y_test['math score'], y_pred[:, 0], alpha=0.5)
plt.xlabel('Actual Math Score')
plt.ylabel('Predicted Math Score')
plt.title('Math Score')

# Plot for reading score
plt.subplot(1, 3, 2)
plt.scatter(y_test['reading score'], y_pred[:, 1], alpha=0.5)
plt.xlabel('Actual Reading Score')
plt.ylabel('Predicted Reading Score')
plt.title('Reading Score')

# Plot for writing score
plt.subplot(1, 3, 3)
plt.scatter(y_test['writing score'], y_pred[:, 2], alpha=0.5)
plt.xlabel('Actual Writing Score')
plt.ylabel('Predicted Writing Score')
plt.title('Writing Score')

plt.tight_layout()
plt.show()