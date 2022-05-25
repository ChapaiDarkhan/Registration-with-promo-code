from datetime import datetime

import pandas as pd


def get_coldest_month(file_path):
    data = pd.read_csv(file_path, index_col=[0], parse_dates=[0], usecols=[0, 1])

    temperature = data.groupby([data.index.strftime('%m-%Y')]).mean()
    time_max_temp = temperature['temp'].idxmax(), temperature['temp'].mean()
    return time_max_temp


def get_windy_month(file_path):
    data = pd.read_csv(file_path, index_col=[0], parse_dates=[0], usecols=[0, 7])

    wind = data.groupby([data.index.strftime('%m-%Y')]).mean()
    windy_month = wind['WIND_SPD'].idxmax(), wind['WIND_SPD'].mean()
    return windy_month


def get_cold_day(file_path):
    data = pd.read_csv(file_path, index_col=[0], parse_dates=[0], usecols=[0, 1])

    temperature = data.groupby([data.index.strftime('%d-%m-%Y')]).min()
    temperature = temperature['temp'].idxmax(), temperature['temp'].min()
    return temperature


def get_warm_month(file_path):
    data = pd.read_csv(file_path, index_col=[0], parse_dates=[0], usecols=[0, 1])

    temperature = data.groupby([data.index.strftime('%m-%Y')]).mean()
    temperature = temperature['temp'].idxmax(), temperature['temp'].mean()
    return temperature


def get_warm_day(file_path):
    data = pd.read_csv(file_path, index_col=[0], parse_dates=[0], usecols=[0, 1])

    temperature = data.groupby([data.index.strftime('%d-%m-%Y')]).max()
    temperature = temperature['temp'].idxmax(), temperature['temp'].max()
    return temperature


def get_rainy_week_and_period_and_rainfall(file_path):
    data = pd.read_csv(file_path, index_col=[0], parse_dates=[0], usecols=[0, 5])

    temp = data.groupby([data.index.strftime('%Y-%W')]).mean()
    data = temp['U'].idxmax().split('-')
    rainfall = temp['U'].max()
    year, week = int(data[0]), int(data[1])
    period = [datetime.strptime(f'{year}-W' + str(week) + str(x), "%Y-W%W-%w").strftime('%d.%m.%Y') for x in range(-5, 0)]
    return {'period': period, 'rainfall': rainfall}
