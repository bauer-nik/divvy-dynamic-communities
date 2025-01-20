from datetime import datetime

COL_MAP = {
    'ride_id':'TRIP ID',
    'started_at':'START TIME',
    'ended_at':'STOP TIME',
    'start_station_name':'FROM STATION NAME',
    'start_station_id':'FROM STATION ID',
    'end_station_name':'TO STATION NAME',
    'end_station_id':'TO STATION ID',
    'member_casual':'USER TYPE'
}

COMMON_COLS = ['TRIP ID', 'START TIME','STOP TIME','TRIP DURATION','FROM STATION NAME',
               'FROM STATION ID','TO STATION NAME','TO STATION ID','USER TYPE']

USER_MAP = {
    "member":"Subscriber",
    "casual":"Customer"
}

def get_duration(start_str, end_str):
    st = datetime.strptime(start_str, '%Y-%m-%d %H:%M:%S')
    et = datetime.strptime(end_str, '%Y-%m-%d %H:%M:%S')
    change = et-st
    return change.seconds


def process_raw_data(df):
    df = df.drop_duplicates()
    df = df.rename(columns=COL_MAP)
    df['TRIP DURATION'] = df.apply(lambda row: get_duration(row['START TIME'], row['STOP TIME']), axis=1)
    df['USER TYPE'] = df['USER TYPE'].map(USER_MAP)
    return df[COMMON_COLS]
