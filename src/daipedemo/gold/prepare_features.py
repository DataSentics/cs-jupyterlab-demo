# %%
import pandas as pd
from daipecore.decorator.notebook_function import notebook_function
from daipedemo.lib.read_csv import read_csv

# %%
@notebook_function(read_csv("data/gold.csv"))
def prepare_features(df: pd.DataFrame):
    return df
