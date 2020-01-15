
"""
utility functions for working with DataFrames
"""

import pandas as pd
import numpy as np

TEST_DF = pd.DataFrame([1, 2, 3, 4, 5, 6])

def train_val_test_split(df):
    """
    split DataFrame into trainin, validation and testing
    """
    from sklearn.model_selction import train_test_split
    train, test = train_test_split(df, train_size = 0.80, test_size=0.20,
    random_state = 42)
    train, val = train_test_split(train, train_size = 0.70,  val_size=0.30)
    print(train.shape, val.shape, test.shape)

    return train, val, test

def add_col_to_df(col, df):
    """
    add new column into DataFrame
    """
    series = pd.Series(col)
    df['new_column'] = series
    return df
