from sklearn.preprocessing import MinMaxScaler
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

if __name__ == "__main__":
    min_max_scaler = MinMaxScaler()
    directory = 'SPLIT'
    for sample in os.listdir(directory):
        if sample.__contains__('.csv'):
            sample_path = os.path.join(directory, sample)
            data = pd.read_csv(sample_path)
            x_val = []
            dates = np.asarray(data.Date)
            for vals in dates:
                val = vals.split('-')
                x_val.append(datetime.datetime(int(val[2]), int(val[0]), int(val[1])))
            #normal_growth = min_max_scaler.fit_transform(np.asarray(data.Value).reshape(-1, 1))
            #x_val.sort
            plt.title(sample)
            plt.plot_date(x_val, data.Value,)
    plt.show()

        #plt.show()
