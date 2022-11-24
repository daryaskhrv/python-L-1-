import pandas as pd
import numpy as np


def add_number_class (df: pd.DataFrame):
    """Adding a column with numeric labels"""
    i=0
    empty_list = []
    while i < len (df):
        empty_list.append(int(df['class'].iloc[i] == 'bay horse'))
        i+=1
    print(empty_list)
    df["numerical_class"] = empty_list
    #df.to_csv('new.csv')

if __name__ == "__main__":
    df = pd.read_csv("Lab4/data.csv", usecols = ['Абсолютный путь','Метка'])
    df = df.rename(columns={'Абсолютный путь': 'absolute_path', 'Метка': 'class'})
    #df.to_csv('properties.csv')
    add_number_class(df)