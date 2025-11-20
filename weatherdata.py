# weather data report

import pandas as pd


def weather_report(df: pd.DataFrame, date_col='date', temp_col='temp'):
    df = df.copy()
    df[date_col] = pd. to_datetime(df[date_col])
    df.set_index(date_col, inplace=True)
    monthly = df[temp_col].resample('M').agg(['mean',max,'min'])
    print(monthly.head())

    return monthly