

import numpy as np
import pandas as pd
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_source = os.path.join(BASE_DIR + "/1_Sources/")

print(path_source)

df_city_data_hamburg = pd.read_csv(path_source+"city_data_hamburg.csv")


def _main():
    print(df_city_data_hamburg)

if __name__ == "__main__":
    _main()
