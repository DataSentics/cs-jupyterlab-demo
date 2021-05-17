# %%
import pandas as pd
from daipecore.decorator.notebook_function import notebook_function
from daipedemo.lib.keboola_writer import keboola_writer
from daipedemo.lib.read_csv import read_csv

# %%
@notebook_function(read_csv("data/silver.csv"))
@keboola_writer("data/gold.csv")
def silver_read_output(df: pd.DataFrame):
    return df
