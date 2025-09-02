# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 12:33:01 2025

@author: abinnu
"""

import pandas as pd 

Data = pd.read_csv("D:/project_classification/dataset/Air_Quality.csv")


Data.drop("Date",axis = 1,inplace = True)
Data.drop("CO2",axis = 1,inplace = True)


from sklearn.preprocessing import LabelEncoder

LE = LabelEncoder()
Data["City"] = LE.fit_transform(Data["City"])


def Aqi(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Bad"
    else:
        return "Very Bad"

Data["Aqi"] = Data["AQI"].apply(Aqi)

Data.drop("AQI",axis = 1,inplace = True)


x = Data.drop("Aqi",axis = 1)
y= Data["Aqi"]


from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.2,random_state=0)


from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100,random_state=0)
clf.fit(xtrain,ytrain)


import joblib 

path = "D:/project_classification/deployment/ml-airquality-app/model/RandomForest.pkl"
joblib.dump(clf,path)

ypred = clf.predict(xtest)

from sklearn.metrics import accuracy_score

Acc = accuracy_score(ytest,ypred)
acc = Acc *100
print(f"Accuracy:{acc:.2f}%")


from sklearn.metrics import confusion_matrix

CM = confusion_matrix(ytest,ypred)
CM 


from sklearn.metrics import classification_report

CR = classification_report(ytest,ypred) 
CR




