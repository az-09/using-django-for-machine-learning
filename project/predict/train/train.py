import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

dataset = pd.read_csv('./project/predict/train/data.csv')
X = dataset.iloc[:, :-1].values
#print(X) # YearsExperience, vertical
y = dataset.iloc[:, 1].values
#print(y) # Salary, horizontal

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

print("X_test")
print(X_test)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(y_pred)

filename = './project/predict/model.pkl'

pickle.dump(regressor, open(filename, 'wb'))