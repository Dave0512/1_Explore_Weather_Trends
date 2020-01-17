

import numpy as np
import pandas as pd
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_source = os.path.join(BASE_DIR + "/1_Sources/")

print(path_source)

class roll_avg:
    """class to calculate roll_avg"""

    def __init__(self, l_sour,l_c_t_sort,l_c_f_c,c_c,p_w):
        """ Constructor method """
        self.load_source = l_sour
        self.load_column_to_sort = l_c_t_sort
        self.loaded_column_for_calc = l_c_f_c
        self.created_column = c_c
        self.period_window = p_w

    def _load_df(self):
        """ load desired data """
        df = pd.read_csv(path_source+self.load_source)
        return df

    def _sort_df(self):
        """ sort df by given column - normally by year """
        df = self._load_df()
        df = df.sort_values(self.load_column_to_sort)
        return df

    def _drop_na(self):
        """ drop_na in the col with data for calculation to recieve correct results """
        df = self._sort_df()
        df = df.dropna()
        return df

    def _execute_calc(self):
        """ calc rolling avg """
        df = self._drop_na()
        df[self.created_column] = df[self.loaded_column_for_calc].rolling(window=self.period_window, center=False).mean()
        return df

    def _final(self):
        """ returns the final df to main """
        df_final = self._execute_calc()
        return df_final

def _main():
    """ def to create objects and execute """
    df_for_calc = roll_avg("city_data_hamburg.csv","year",'avg_temp','created_col_rol_avg',7)
    print(df_for_calc._final())

if __name__ == "__main__":
    _main()
