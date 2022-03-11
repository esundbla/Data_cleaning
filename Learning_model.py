""" Program to pull in individula averaged csv's use linear regresion with
an exponetial function to get continous y values.  Then applying machine learning
on features (heat, hydration) to get estimates of w values and draw conclusions."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn import linear_model
from sklearn.preprocessing import MinMaxScaler
import math


def dataRead():
    growth = pd.read_csv('SPLIT\SPLITS002.csv')
    #data = pd.read_csv()
    return growth #data


def expoLinear(growth):
    min_max_scaler = MinMaxScaler()
    size = np.asarray(growth.Value) #min_max_scaler.fit_transform(np.asarray(growth.Value).reshape(-1, 1))
    #print(size)
    y_transform = []
    x_as_dates = []
    for num in size:
        y_transform.append(np.log(num))
    for day in np.asarray(growth.Date):
        date = day.split('-')
        #print(date)
        x_as_dates.append((int(date[0]) * 30) + int(date[1]))
    zipped = list(zip(x_as_dates, y_transform))
    modd = pd.DataFrame(zipped, columns=['Day', 'Value'])
    #print(modd)
    reg = linear_model.LinearRegression().fit(np.asarray(modd.Day).reshape(-1,1), np.asarray(modd.Value).reshape(-1,1))
    expon = -reg.intercept_*(math.e**(reg.coef_*x_as_dates))
    #for x in x_as_dates:
        #expon.append(-reg.intercept_*(2.718281**(reg.coef_*x)))
    plt.scatter(x_as_dates, expon)
    plt.show()
    return reg.coef_, reg.intercept_



if __name__ == "__main__":
    growth = dataRead()
    coef, intercpt =expoLinear(growth)
    print(coef, -intercpt)