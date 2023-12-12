import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles(000)","age"]].values
y = data["Price"].values

#split the data into training and testing data

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)

#create linear regression model

model = LinearRegression().fit(xtrain, ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 

coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y), 2)

#Linear Equation and rsquared value

print(f"Linear Equation of Model: y={coef[0]}x1 + {coef[1]}x2 + {intercept}")
print("R Squared Value:", r_squared)

#Get predicted y values for the xtest values
#Round to two decimal places
predict = model.predict(xtest)
predict = np.around(predict, 2)
print(predict)

#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")
print("\nTesting Multivariable Model with Testing Data:")
for index in range (len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
    print(f"Miles: {x_coord[0]} Age: {x_coord[1]} Actual: {actual} Predicted: {predicted_y}")

cars = [[89, 10], [150, 20]]
myPredictions = model.predict(cars)
print(myPredictions)

#Visual Graph
# fig, graph = plt.subplots(2)
# graph[0].scatter(x[0], y)
# graph[0].set_xlabel("Total Miles")
# graph[0].set_ylabel("Price")

# graph[1].scatter(x[1], y)
# graph[1].set_ylabel("Price")
# graph[1].set_xlabel("Car Age")

# print(f"Correlation between Total Miles and Car Price: {round(x[0].corr(y), 3)}")
# print(f"Correlation between Age and Car Price: {round(x[1].corr(y), 3)}")

# plt.tight_layout
# plt.show