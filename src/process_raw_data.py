import pandas as pd
import os
from scripts.data_processing.transform import process_raw_data

YEARS1 = ["2013","2014","2015","2016","2017","2018","2019"]
YEARS2 = ["2020","2021","2022","2023"]
# TODO: add to bashrc & use var references (DIVVY_DATA_PATH), not full pathways
IN_PATH = "D:/analytics_projects/divvy/raw_data/"
OUT_PATH = "D:/analytics_projects/divvy/processed_data/"


if __name__=='__main__':

    # 2013-2019 in one file --> split into per year files
    divvy_df = pd.read_csv(os.path.join(IN_PATH, "Divvy_Trips_2013_2019.csv"))
    for year in YEARS1:
        year_df = divvy_df[divvy_df['STOP TIME'].str.contains(year)]
        year_df.to_csv(os.path.join(OUT_PATH, f"divvy_trips_{year}.csv"), index=False)

    # 2020 + in monthly batches grouped by year in external hard drive
    for year in YEARS2:
        yr_dfs = []
        for file in os.listdir(os.path.join(IN_PATH, year)):
            df = pd.read_csv(os.path.join(IN_PATH, year, file))
            yr_dfs.append(df)

        year_df = pd.concat(yr_dfs)
        # formats direct from divvy data pulls to naming conventions of initial 2013 - 2019 processed file
        year_df = process_raw_data(year_df)
        year_df.to_csv(os.path.join(OUT_PATH,f"divvy_trips_{year}.csv"),index=False)
