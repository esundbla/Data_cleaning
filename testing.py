import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix

column_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree',
'age', 'labelvalue']

pima = pd.read_csv("pima-indians-diabetes-database.csv", header=None, names=column_names)
print(pima.head())

pima.hist(bins=15, figsize=(10,10))
pd.plotting.scatter_matrix(pima, figsize=(10,10))
plt.figure()


corr_matrix = pima.corr()
sns.heatmap(corr_matrix, annot=True)

feature_columns = ['pregnant', 'insulin', 'glucose', 'bmi']
X = pima[feature_columns]
mins = X.min(axis=0)
maxes = X.max(axis=0)
X = (X - mins) / (maxes - mins)
pd.set_option("display.max_rows", None, "display.max_columns", None)
X.head()

y = np.arange(len(X))

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
x_train.head(25)

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(y_test)
print(y_pred)

confusion_mat = confusion_matrix(y_test, y_pred)
print(confusion_mat)

