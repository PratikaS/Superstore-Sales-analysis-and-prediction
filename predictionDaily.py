import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
df = pd.read_csv("static/datafile3.csv",header=0)
    # print(df)

    # print(df.info())
x = df.iloc[:, [0,1,2,3,4,5,6,7,9,10,11]].values
y = df.iloc[:,13].values
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
# print(df1[15][6])

x[:, 0] = encoder.fit_transform(x[:, 0])  # segment
x[:, 1] = encoder.fit_transform(x[:, 1])  # region
x[:, 2] = encoder.fit_transform(x[:, 2])  # Country
# x[:, 2] = encoder.fit_transform(x[:, 2])
x[:, 3] = encoder.fit_transform(x[:, 3]) # city
x[:, 4] = encoder.fit_transform(x[:, 4])  # category
x[:, 5] = encoder.fit_transform(x[:, 5])  # sub-category

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=123456)

def accuaracy(regressor):
    accuracy = round(regressor.score(x_train, y_train) * 100, 2)
    # print(f"Predictions Random Forest: {predictions}")
    print(f"Random Forest, accuracy : {accuracy} %")
    return accuracy

def model_lm():
    from sklearn.linear_model import LinearRegression
    classifier = LinearRegression()
    classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)

    rf_accuracy = round(classifier.score(x_train, y_train) * 100, 2)
    print(f"Predictions Linear Regression : {predictions}")
    # print(f"Linear Regression accuracy : {rf_accuracy} %")
    return predictions

def test_rf():
    from sklearn.ensemble import RandomForestRegressor
    classifier = RandomForestRegressor()
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)

    return classifier

def model_rf(x_train, y_train):
    from sklearn.ensemble import RandomForestRegressor
    classifier = RandomForestRegressor()
    return classifier.fit(x_train, y_train)
def model_dt(x_train, y_train):
    from sklearn.tree import DecisionTreeRegressor
    classifier = DecisionTreeRegressor()
    return classifier.fit(x_train, y_train)
def test_adaboost():
    from sklearn.ensemble import AdaBoostRegressor
    classifier = AdaBoostRegressor()
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    rf_accuracy = round(classifier.score(x_train, y_train) * 100, 2)
    print(f"Predictions adaboost: {predictions}")
    print(f"adaboost accuracy : {rf_accuracy} %")

def test_gradient_boost():
    from sklearn.ensemble import GradientBoostingRegressor
    classifier = GradientBoostingRegressor()
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    rf_accuracy = round(classifier.score(x_train, y_train) * 100, 2)
    print(f"Predictions gradient_boost: {predictions}")
    print(f"gradient_boost accuracy : {rf_accuracy} %")

def test_xgboost():
    from xgboost import XGBRegressor
    classifier = XGBRegressor()
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    rf_accuracy = round(classifier.score(x_train, y_train) * 100, 2)
    print(f"Predictions xgboost: {predictions}")
    print(f"xgboost accuracy : {rf_accuracy} %")

def test_dt():
    from sklearn.tree import DecisionTreeRegressor
    classifier = DecisionTreeRegressor()
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    rf_accuracy = round(classifier.score(x_train, y_train) * 100, 2)
    # print(f"Predictions Decision Tree: {predictions}")
    print(f"Mean square error is in Descision Tree : {mean_squared_error(y_test, predictions)}")
    print(f"Decision Tree accuracy : {rf_accuracy} %")
    return classifier
def test_nb():
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    rf_accuracy = round(classifier.score(x_train, y_train) * 100, 2)
    print(f"Predictions Decision Tree: {predictions}")
    print(f"Naive Bayes accuracy : {rf_accuracy} %")

def cross_validate(algorithm,classifier,x_test,y_test):
    predictions = classifier.predict(x_test)
    accuracy = round(classifier.score(x_train, y_train) * 100, 2)
    print( f"predictions : {predictions}")
    print(f"Accuracy of {algorithm} algorithm :  {accuracy} %")
    return accuracy


#     print(f"Price : {price[i]}    Discount : {discount[i]}  Quantity : {predictions[i]}  Total Sale : {total_sale}")
def predict(pr):
    list1 = []
    for i in pr:
        # print(f"{int(i)} \t")
        list1.append(int(i))

# pr2 = test_dt()
# # list2 = predict(pr2)
# accuaracy1 = accuaracy(pr2)
# # predict(pr2)
# pr3 = test_rf()
# # list3 = predict(pr3)
# accuaracy1 = accuaracy(pr3)
# # test_nb()
# # test_xgboost()
# test_adaboost()
# test_gradient_boost()
print(" * * * * * Daily Prediction * * * * * ")

classifier_dt = model_dt(x_train, y_train)
dt_accuracy = cross_validate('Decision tree', classifier_dt, x_test, y_test)

#Random Forest
classifier_rf = model_rf(x_train, y_train)
rf_accuracy = cross_validate('Random Forest', classifier_rf, x_test, y_test)

test_adaboost()
test_gradient_boost()
test_xgboost()
# classfier_adaboost=test_adaboost(x_train,y_train)
# ada_accuracy=cross_validate("Adaboost",classfier_adaboost,x_test,y_test)

