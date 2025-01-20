import pandas as pd
import os


YEARS = ["2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"]
IN_PATH = "D:/analytics_projects/divvy/processed_data/"
OUT_PATH = "data/network_graphs/"

if __name__ == "__main__":
    for year in YEARS:
        df = pd.read_csv(os.path.join(IN_PATH,f"divvy_trips_{year}.csv"))
