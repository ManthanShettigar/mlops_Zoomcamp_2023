import pandas as pd
from datetime import datetime



def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)



def prepare_data(df):
    # Transformation logic
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    return df

# Test data
data = [
    (None, None, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2), dt(1, 10)),
    (1, 2, dt(2, 2), dt(2, 3)),
    (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
    (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
]


def test_prepare_data():

    df = pd.DataFrame(data, columns=['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    actual_df = prepare_data(df)
    expected_data = [{'PULocationID': '-1', 'DOLocationID': '-1', 'tpep_pickup_datetime': pd.Timestamp('2022-01-01 01:02:00'), 'tpep_dropoff_datetime': pd.Timestamp('2022-01-01 01:10:00'), 'duration': 8.0},
            {'PULocationID': '1', 'DOLocationID': '-1', 'tpep_pickup_datetime': pd.Timestamp('2022-01-01 01:02:00'), 'tpep_dropoff_datetime': pd.Timestamp('2022-01-01 01:10:00'), 'duration': 8.0}, 
            {'PULocationID': '1', 'DOLocationID': '2', 'tpep_pickup_datetime': pd.Timestamp('2022-01-01 02:02:00'), 'tpep_dropoff_datetime': pd.Timestamp('2022-01-01 02:03:00'), 'duration': 1.0}]

    expected_columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'duration']
    expected_df = pd.DataFrame(expected_data, columns=expected_columns)

    print(len(expected_df)) # 3 rows

    

    pd.testing.assert_frame_equal(expected_df, actual_df)







