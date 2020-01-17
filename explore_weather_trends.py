

import numpy as np
import pandas as pd
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_source = os.path.join(BASE_DIR + "/1_Sources/")

print(path_source)

df_city_data_hamburg = pd.read_csv(path_source+"city_data_hamburg.csv")
df_city_data_hamburg.sort_values("year")

df_city_data_hamburg_without_na = df_city_data_hamburg.dropna()

df_city_data_hamburg_without_na['rolling_avg'] = df_city_data_hamburg_without_na['avg_temp'].rolling(window=7, center=False).mean()




def _main():
    print(df_city_data_hamburg)
    print(df_city_data_hamburg_without_na)

if __name__ == "__main__":
    _main()
