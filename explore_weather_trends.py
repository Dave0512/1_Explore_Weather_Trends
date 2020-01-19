

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
sns.set(style='darkgrid')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_source = os.path.join(BASE_DIR + "/")
# path_source = os.path.join(BASE_DIR + "/1_Sources/")

print(path_source)

class roll_avg:
    """class to calculate roll_avg"""

    def __init__(self,
                 load_source,
                 data_type_source,
                 load_column_to_sort,
                 loaded_column_for_calc,
                 created_column,
                 period_window):

        """ Constructor method """
        self.load_source = load_source # file
        self.data_type_source = data_type_source
        self.load_column_to_sort = load_column_to_sort # year
        self.loaded_column_for_calc = loaded_column_for_calc # avg_temp
        self.created_column = created_column # roll average
        self.period_window = period_window # time for calculation roll average (7 days)

    def _load_df(self):
        """ load desired data """
        df = pd.read_csv(path_source+self.load_source+self.data_type_source)
        return df

    def _sort_df(self):
        """ sort df by given column - normally by year """
        df = self._load_df()
        df = df.sort_values(self.load_column_to_sort)
        return df

    def _execute_calc(self):
        """ calc rolling avg """
        df = self._sort_df()
        df[self.created_column] = df[self.loaded_column_for_calc].rolling(window=self.period_window, center=False).mean()
        return df

    def _drop_na(self):
        """ drop_na in the col with data for calculation to recieve correct results """
        df = self._execute_calc()
        df = df.dropna()
        return df

    def _add_col_source(self):
        df = self._drop_na()
        df['file'] = pd.Series()
        df['file'] = df['file'].replace(np.NaN,self.load_source)
        return df

    def final(self):
        """ returns the final df to main """
        df_final = self._add_col_source()
        return df_final

def create_vlookup():
    """ def to join global and local roll_avg for visualisation """

    city_data = roll_avg("city_data_hamburg",".csv","year",'avg_temp','created_col_rol_avg',7)
    global_data = roll_avg("global_data",".csv","year",'avg_temp','created_col_rol_avg',7)

    df_local = pd.DataFrame(city_data.final())
    df_global = pd.DataFrame(global_data.final())

    df_merged = df_local.merge(df_global, on = "year", how='left')
    df_merged.rename(columns={'created_col_rol_avg_x':'roll_avg_local','created_col_rol_avg_y':'roll_avg_global'},inplace=True)
    df_merged = df_merged[['year','roll_avg_local','roll_avg_global']]
    print(df_merged.info())
    return df_merged

def add_visualisation():
    """ add line plot """
    df = create_vlookup()
    x_1 = df["year"]
    y_1 = df["roll_avg_local"]
    x_2 = df["year"]
    y_2 = df["roll_avg_global"]

    label_line_1 = "city_data_hamburg"
    label_line_2 = "global_data"
    plt.plot(x_1,y_1,label=label_line_1,color='blue',linewidth=2, markersize=12)
    plt.plot(x_2,y_2,label=label_line_2,color='green',linewidth=2, markersize=12)
    plt.xlabel("year")
    plt.ylabel("temperature (rolling_average)")
    plt.legend(loc="upper left")
    plt.show()

def main():

    add_visualisation()

if __name__ == "__main__":
    main()
