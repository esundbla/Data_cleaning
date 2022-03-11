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


def dataRead(g_path, d_path):
    """ Tool to read in given path and return dataframes of csv values  """
    growth = pd.read_csv(g_path)
    data = pd.read_csv(d_path)
    return growth #data


def expoLinear(growth):
    """ From Growth vs time data pull use regression to estimate an exponential curve with the form b*e^(ax)
      Where b is the intercept an a is the coeficiant return a, b"""
    size = np.asarray(growth.Value)
    # We transform out y data by taking the natural log
    # This allows us to use linear regression
    y_transform = np.log(size)
    # From the date info we get an integer representation for regression calculation
    x_as_dates = []
    for day in np.asarray(growth.Date):
        date = day.split('-')
        x_as_dates.append((int(date[0]) * 30) + int(date[1]))

    # zip the modified values as a dataframe and run linear regression
    zipped = list(zip(x_as_dates, y_transform))
    modd = pd.DataFrame(zipped, columns=['Day', 'Value'])
    reg = linear_model.LinearRegression().fit(np.asarray(modd.Day).reshape(-1,1), np.asarray(modd.Value).reshape(-1,1))

    # Graph the resulting exponential equation as a function of time
    expon = -reg.intercept_*(math.e**(reg.coef_*x_as_dates))
    plt.scatter(x_as_dates, expon)
    plt.show()
    return reg.coef_, reg.intercept_



if __name__ == "__main__":
    growth = dataRead()
    coef, intercpt =expoLinear(growth)
    print(coef, -intercpt)