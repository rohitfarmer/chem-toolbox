#!/usr/bin/env python3

# Standard library.

# External lbrary.
import pandas as pd
import numpy as np

def add_indicator(df):
    """
    Purpose
    -------
    Add indicator column next to any column that has one or more NaNs.
    The indicator column contains 1 at the index that has NaN in the parent data column.
    The NaNs in the parent data columns are replaced with 0.

    Argument
    --------
    df: Pandas dataframe

    Return
    ------
    df: Pandas dataframe with the appended indicator columns
    """

    all_cols = list(df.columns)
    na_cols = df.columns[df.isna().any()].tolist()
    
    for i in na_cols:
        idx = all_cols.index(i)
        ind_name = i + '_Ind'
        df.insert(loc=idx+1, column=ind_name, value=np.where(df[i].isnull(), 1, 0))
        all_cols = list(df.columns)
    
    df = df.fillna(value=0)
   
    return df