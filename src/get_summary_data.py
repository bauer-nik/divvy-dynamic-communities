import pandas as pd
import os
import pickle

ALL_YEARS = ["2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"]
PROCESSED_PATH = "D:/analytics_projects/divvy/processed_data/"


def get_station_names(df):
    to_names = df["TO STATION NAME"].drop_duplicates().tolist()
    from_names = df["FROM STATION NAME"].drop_duplicates().tolist()

    return list(set(from_names + to_names))


if __name__ == "__main__":
    station_names = []
    graph_data = []
    num_stations = {}
    trip_durations = {}

    for file_name in os.listdir(PROCESSED_PATH):
        file_ = file_name.split(".")[0]
        year = file_.split("_")[-1]
        # get df
        df = pd.read_csv(os.path.join(PROCESSED_PATH, file_name), low_memory=False)

        # get unique stations and their Ids
        yr_station_names = get_station_names(df)
        station_names.append(yr_station_names)

        # GET N UNIQUE STATION IDS
        nmstns = len(yr_station_names)
        num_stations[year] = nmstns

        # GET RIDE LENGTHS (UNDER 1 HOUR)
        under_hr_df = df[df['TRIP DURATION']<=3600]
        trip_durations[year] = under_hr_df['TRIP DURATION'].tolist()

        usr_types = df['USER TYPE'].unique()
        for user_type in usr_types:
            # GET TOTAL NUMBER OF RIDES
            num_rides = df[df["USER TYPE"]==user_type].shape[0]
            # GET AVERAGE RIDE LENGTH AND STANDARD DEVIATION (UNDER 1 HOUR)
            avg_trip = under_hr_df[under_hr_df["USER TYPE"]==user_type]['TRIP DURATION'].mean()
            sd_trip = under_hr_df[under_hr_df["USER TYPE"]==user_type]['TRIP DURATION'].std()
            data_for_graph = [year,user_type,num_rides,avg_trip,sd_trip]
            print(data_for_graph)
            graph_data.append(data_for_graph)

        del df

    graph_df = pd.DataFrame(
        {
            "Year": [x[0] for x in graph_data],
            "User Type": [x[1] for x in graph_data],
            "Number of Rides": [x[2] for x in graph_data],
            "Avg Trip Duration": [x[3] for x in graph_data],
            "Std Trip Duration": [x[4] for x in graph_data],
        }
    )

    graph_df.to_csv("data/processed/per_year_vals.csv", index=False)

    # output year-specific values as pickle files for EDA
    with open('data/processed/num_stations_per_year.pkl', 'wb') as f:
        pickle.dump(num_stations, f)

    with open('data/processed/trip_durations_under1hr_per_year.pkl', 'wb') as f:
        pickle.dump(trip_durations, f)

    #generate unique id for each station and create mapping back and forth
    ids_ = list(range(1, len(station_names)+1))
    names_to_ids = dict(zip(station_names, ids_))
    ids_to_names = dict(zip(ids_, station_names))

    with open('data/util_files/station_ids_to_names.pkl', 'wb') as f:
        pickle.dump(ids_to_names, f)

    with open('data/util_files/station_names_to_ids.pkl', 'wb') as f:
        pickle.dump(names_to_ids, f)
