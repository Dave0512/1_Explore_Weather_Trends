

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
sns.set(style='darkgrid')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_source = os.path.join(BASE_DIR + "/1_Sources/")

print(path_source)

class roll_avg:
    """class to calculate roll_avg"""

    def __init__(self, load_source,data_type_source,load_column_to_sort,loaded_column_for_calc,created_column,period_window):

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

    def _add_col_source(self):
        df = self._execute_calc()
        df['file'] = pd.Series()
        df['file'] = df['file'].replace(np.NaN,self.load_source)
        return df

    def final(self):
        """ returns the final df to main """
        df_final = self._add_col_source()
        return df_final



    def add_visualisation(self):
        """ add line plot """
        df = self.final()
        x = df[self.load_column_to_sort]
        y = df[self.created_column]
        label_line_1 = self.load_source # Line 1
        plt.plot(x,y,label=label_line_1,color='blue',linewidth=2, markersize=12)
        # plt.plot(x,y,label=label_line_2,color='green', linestyle='dashed',linewidth=2, markersize=12)
        plt.xlabel(self.load_column_to_sort)
        plt.ylabel(self.created_column)
        plt.legend(loc="upper left")
        plt.show()

def main():
    """ def to create objects and execute class methods """
    city_data = roll_avg("city_data_hamburg",".csv","year",'avg_temp','created_col_rol_avg',7)
    global_data = roll_avg("global_data",".csv","year",'avg_temp','created_col_rol_avg',7)

    # Build a final df based on the global and local temp data
    # Visualisation
    # Based on final df
    frames = [city_data.final(),global_data.final()]
    df_total = pd.concat(frames,sort=False)
    print(df_total)

    # city_data.add_visualisation()
    # global_data.add_visualisation()



if __name__ == "__main__":
    main()

    # join or merge year local global
    # name.split(".")[1] - datafile type (csv)
    # class method start with _
    # methods used outside - interface methods, public methods
    # magic methods __ - automatically called
    # add more comments: The reason why i wrote the code
    # submit also a pdf - transfer .py to jupyter notebook (2 chapter)
