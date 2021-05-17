# %%
import os
import pandas as pd
import urllib.request
from zipfile import ZipFile
from daipecore.decorator.notebook_function import notebook_function
from daipedemo.lib.read_csv import read_csv
from daipedemo.lib.keboola_writer import keboola_writer

# %%
@notebook_function()
def download_data():
    opener = urllib.request.URLopener()
    # Bondora server checks User-Agent and forbids the default User-Agent of urllib
    opener.addheader(
        "User-Agent",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    )

    opener.retrieve("https://www.bondora.com/marketing/media/LoanData.zip", "data/loanData.zip")

# %%
@notebook_function()
def unpack_data():
    with ZipFile("data/loanData.zip", "r") as zip_obj:
        zip_obj.extractall("data/")

# %%
@notebook_function(read_csv("data/loanData.csv"))
def load_csv(df: pd.DataFrame):
    return df["ReportAsOfEOD"]

# %%
@notebook_function(load_csv)
@keboola_writer("data/silver.csv")
def write(df: pd.DataFrame):
    return df
